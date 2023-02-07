import config
import oracledb
import petl as etl
import pandas
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
a=input("Enter Username =>")
b=input("Enter Password =>")
sql="select members.mid,members.username,members.fname, books.bid,books.bname," \
    "bookstatus.doi, bookstatus.dor, bookstatus.doar,bookstatus.fine from bookstatus join members on " \
    "members.mid=bookstatus.mid " \
    "join books on books.bid=bookstatus.bid" \
    " where members.mid=(select mid from members where username="':a'" and pass="':b'")"
try:
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'a':a,'b':b})
            connection.commit()
            table1=etl.fromdb(connection.cursor,sql,{'a':a,'b':b})
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)




