import psycopg2

class bd:
    def __init__(self):
        self.database = ''
        self.user = 'postgres'
        self.host = 'localhost'
        self.port = 5432
        self.password = ''


    def inserir(self, comando):
        self.conn = psycopg2.connect(database=self.database, user=self.user, host=self.host, port=self.port,
                                     password=self.password)
        self.cur = self.conn.cursor()
        self.cur.execute(f'{comando}')
        self.conn.commit()
        self.cur.close()
        self.conn.close()



    def get_rows(self, comando):
        self.conn = psycopg2.connect(database=self.database, user=self.user, host=self.host, port=self.port,
                                     password=self.password)
        self.cur = self.conn.cursor()
        self.cur.execute(f'{comando}')
        self.row = self.cur.fetchall()
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return self.row








