import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        try:
            distanza_minima = float(self._view._txtDistanza.value)
        except ValueError:
            self._view.create_alert("Inserisci una distanza valida")
            return

        self._model.buildGraphPesato(distanza_minima)

        self._view.lst_result.controls.clear()

        self._view.lst_result.controls.append(
            ft.Text(f"Numero vertici: {self._model.getNumNodi()}")
        )

        self._view.lst_result.controls.append(
            ft.Text(f"Numero archi: {self._model.getNumArchi()}")
        )

        self._view.lst_result.controls.append(
            ft.Text("Archi:")
        )

        for u, v, data in self._model.getEdges():
            peso = data["weight"]
            self._view.lst_result.controls.append(
                ft.Text(f"{u.AIRPORT} -- {v.AIRPORT} | distanza media: {peso:.2f}")
            )

        self._view.update_page()

    def loaddistanza(self, e):
        try:
            x = float(self._view._txtDistanza.value)
        except:
            self._view.create_alert("Inserisci un numero valido!")
            return

        print(f"Distanza inserita: {x}")
