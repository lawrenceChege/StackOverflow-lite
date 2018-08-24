import psycopg2
import os
from psycopg2.extras import RealDictCursor


class Database:
    conn = None
    cursor = None
    app = None

    def init_app(self, app):
        self.app = app
        self.conn = psycopg2.connect(conn_string = "dbname='stackoverflow' user='postgres' password='12345678' host='localhost'")
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def connectTODB(self):
        
        try:
            print("connecting to database ...")
            return self.conn
        except:
            print("Connection to database failed!")
        