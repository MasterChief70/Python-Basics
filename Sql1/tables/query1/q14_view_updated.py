import cx_Oracle
import petl as etl
import pandas as pd
import numpy as np
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select * from demo_4'

try:
    # connect to the Oracle Database
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows=cursor.fetchall()
            table1=etl.fromdb(connection.cursor,sql)
            table2=etl.sort(table1,'ENO')
            print(table2)
except cx_Oracle.Error as error:
    print(error)