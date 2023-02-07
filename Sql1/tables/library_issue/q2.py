import config
import oracledb
import petl as etl
import pandas
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
a=int(input("Enter Member ID =>"))
b=input("Enter Username =>")
c=input("Enter Password =>")
d=input("Enter First Name =>")
e=input("Enter Last Name =>")
sql="insert into members values(:a,"':b'","':c'","':d'","':e'")"
try:
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'a':a,'b':b,'c':c,'d':d,'e':e})
            connection.commit()
            table1 = etl.fromdb(connection.cursor, sql,{'a':a,'b':b,'c':c,'d':d,'e':e})
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)



