import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):


        self._aeroporti = DAO.getAllAeroporti()
        self._grafo = nx.DiGraph()  # istanziare il grafo--> poi variabile visibile a tutti ( come self nell'init)
        self._idMapAeroporti = {}
        for a in self._aeroporti:
            self._idMapAeroporti[a.ID] = a


    def buildGraphPesato(self, distanza_minima):
        # come un grafo non pesato
        self._grafo.clear()
        edges = DAO.getAllEdgesPesati(distanza_minima)

        for id1, id2, peso in edges:
            a1 = self._idMapAeroporti[id1]
            a2 = self._idMapAeroporti[id2]

            self._grafo.add_node(a1)
            self._grafo.add_node(a2)

            self._grafo.add_edge(a1, a2, weight=peso)

    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()

    def getEdges(self):
        return self._grafo.edges(data=True)

    def addEdgesPesati(self):
       #riutilizzo il funzionamento di addedges3 ma contando quante volte provo ad aggiungere l'arco
        self._grafo.clear_edges()
        alledges = DAO.getAllEdgesPesati()
       #delle quiri per ottenere il peso degli arhci sarà difficile
       #quindi li utilizziamo in questo modo qui
        for conn in alledges:
            u = self._idMapAeroporti[conn.ORIGIN_AIRPORT_ID]
            v = self._idMapAeroporti[conn.DESTINATION_AIRPORT_ID]

            if self._grafo.has_edge(u, v):#se c'è già
                self._grafo[u][v]['weight'] += 1
            else:
                self._grafo.add_edge(u, v, weight=1)
