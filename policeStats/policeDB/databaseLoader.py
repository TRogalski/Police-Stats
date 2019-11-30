import pymysql
import csv
import datetime

class DatabaseLoader():
    
    def __init__(self, host, user, port, passwd, db):
            self.host = host
            self.user = user
            self.port = port
            self.passwd = passwd
            self.db = db


    def upload_into_db(self, scrap_dict):
        
        db_conn = self.get_connection()
        cur = db_conn.cursor()
        
        self.create_db_if_not_exists(cur)
        
        try:
            cur.execute("USE police_stats")
            self.create_serials_table(cur)
            for key in scrap_dict:
                query = "INSERT INTO stats(DAY, ZNGU, ZP, ZNK, WD, ZWD, RWD) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                cur.execute(query, (key, scrap_dict[key]['Zatrzymani na gorącym uczynku'],
                                         scrap_dict[key]['Zatrzymani poszukiwani'],
                                         scrap_dict[key]['Zatrzymani nietrzeźwi kierujący'], 
                                         scrap_dict[key]['Wypadki drogowe'],
                                         scrap_dict[key]['Zabici w wypadkach drogowych'],
                                         scrap_dict[key]['Ranni w wypadkach drogowych']))
            cur.connection.commit()
        finally:
            db_conn.close()
            cur.close()
    
    
    def get_connection(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            port = self.port,
            passwd = self.passwd,
            db = self.db)
    
    
    def create_db_if_not_exists(self, db_cursor):
        db_cursor.execute("""CREATE DATABASE IF NOT EXISTS police_stats 
                             CHARACTER SET = utf8mb4 
                             COLLATE  = utf8mb4_unicode_ci""")


    def create_serials_table(self, db_cursor):
        db_cursor.execute("""CREATE TABLE IF NOT EXISTS stats(id BIGINT(7) NOT NULL AUTO_INCREMENT,
                                                                DAY DATE,
                                                                ZNGU VARCHAR(200),
                                                                ZP VARCHAR(200),
                                                                ZNK VARCHAR(200),
                                                                WD VARCHAR(200),
                                                                ZWD VARCHAR(200),
                                                                RWD VARCHAR(200),
                                                                PRIMARY KEY (id))""")





    
    
    
