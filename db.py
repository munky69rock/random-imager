import sqlite3

class Db:

    def __init__(self, dbname = 'database.db'):
        self.dbname = 'database.db'
        self.conn = sqlite3.connect(self.dbname)
        self.c = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def execute(self, sql, values = None):
        if values != None:
            return self.c.execute(sql, values)
        else:
            return self.c.execute(sql)

    def commit(self):
        self.conn.commit()
