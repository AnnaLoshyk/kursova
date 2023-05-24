import sqlite3
class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM appointments")