import pymysql
from app.config import config

class Db():
    def __init__(self):
        self.db = config['database']

    def connect(self):
        return pymysql.connect(**self.db)


class MacineVision(Db):
    def __init__(self):
        super().__init__()

    def execute(self,sql):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()


    def fetchone(self, sql):
        with self.connect() as conn:
            cursor = conn.cursor()
            rst = cursor.execute(sql)
            rst = cursor.fetchone()
        return rst[0]

    def find_result_by_id(self, id):
        sql = f"select url_result from URL where id ='{id}'"
        return self.fetchone()[0]


db = MacineVision()