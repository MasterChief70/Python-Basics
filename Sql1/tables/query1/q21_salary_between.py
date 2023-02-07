import oracledb
import config
import petl as etl
import pandas as pd
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
min_salary=int(input("Enter Minimum Salary =>"))
max_salary=int(input("Enter Maximum Salary =>"))
sql = 'select empno,salary from empdept where salary> :min_salary and salary< :max_salary'


try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'min_salary':min_salary,'max_salary':max_salary})
            rows=cursor.fetchall()
            table1 = etl.fromdb(connection.cursor, sql,{'min_salary':min_salary,'max_salary':max_salary})
            nr = etl.nrows(table1)
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)