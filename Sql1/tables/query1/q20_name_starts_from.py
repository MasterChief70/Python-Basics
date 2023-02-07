import oracledb
import config
import petl as etl
import pandas as pd
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
start_char=input("Enter Starting Character =>")
sql = "select * from empl where ename like'"':start_char''%'"'"
print(sql)

try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'start_char':start_char})
            rows=cursor.fetchall()
            table1 = etl.fromdb(connection.cursor, sql,{'start_char':start_char})
            nr = etl.nrows(table1)
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)