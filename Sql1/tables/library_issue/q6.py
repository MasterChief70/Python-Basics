import config
import oracledb
import petl as etl
import pandas
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
a=int(input("Enter Book ID =>"))
b=input("Enter Book Name =>")
c=input("Enter Price =>")
sql="insert into books values(:a,"':b'","':c'")"
try:
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'a':a,'b':b,'c':c})
            connection.commit()
            table1 = etl.fromdb(connection.cursor, sql,{'a':a,'b':b,'c':c})
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)



