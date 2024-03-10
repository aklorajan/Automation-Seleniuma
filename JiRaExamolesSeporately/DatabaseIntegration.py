import mysql.connector


class DatabaseIntegration:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(host=host, user=username, password=password, database=database)
        self.cursor = self.conn.cursor()

    def create_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (username, email, password))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
