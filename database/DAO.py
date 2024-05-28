from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.go_retailer import Go_retailer


class DAO():
    @staticmethod
    def getAllRetailer():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """
        select gr.*
        from go_retailers gr 
        order by gr.Country  """

        cursor.execute(query)

        for row in cursor:
            result.append(Go_retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """
            select gr.*
            from go_retailers gr 
            where gr.Country = %s   """

        cursor.execute(query,(nazione,))

        for row in cursor:
            result.append(Go_retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(anno, r1 , r2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)

        query = """
                select count(distinct gp0.Product_number) as peso
                from go_daily_sales gp0 , go_daily_sales gp3
                where gp0.Product_number = gp3.Product_number and gp0.Retailer_code=%s and  gp3.Retailer_code=%s and year(gp0.Date)= %s and year(gp0.Date)=year(gp3.Date)
                """

        cursor.execute(query, (r1.Retailer_code,r2.Retailer_code,anno,))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result
