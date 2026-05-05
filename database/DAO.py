from database.DB_connect import DBConnect
from model.Aeroporti import Aeroporti


class DAO():


    @staticmethod
    def getAllEdgesPesati(distanza_minima):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = (""" SELECT 
        LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a1,
        GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a2,
        AVG(DISTANCE) AS peso
        FROM flights
        GROUP BY a1, a2
        HAVING peso >= %s
        ORDER BY peso DESC"""
                     )
        cursor.execute(query,(distanza_minima,))

        for row in cursor:
            result.append((row["a1"], row["a2"], row["peso"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporti(**row))
        cursor.close()
        conn.close()
        return result






