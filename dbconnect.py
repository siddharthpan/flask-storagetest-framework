import pymysql

def connection():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           passwd="Rp11022000!",
                           db="users")
    c = conn.cursor()

    return c, conn
