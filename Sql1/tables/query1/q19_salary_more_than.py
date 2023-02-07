import oracledb
import config
import petl as etl
import pandas as pd
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
salary_amount=int(input("Enter Salary Amount =>"))
sql = 'select empno,salary from empdept where salary> :salary_amount order by salary'


try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,{'salary_amount':salary_amount})
            rows=cursor.fetchall()
            table1 = etl.fromdb(connection.cursor, sql,{'salary_amount':salary_amount})
            nr = etl.nrows(table1)
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)