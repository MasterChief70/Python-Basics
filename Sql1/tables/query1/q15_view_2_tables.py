import cx_Oracle
import petl as etl
import pandas as pd
import config
import numpy as np
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select empl.ename,empdept.empno,empdept.deptno,empdept.salary from empl join empdept on empl.empno=empdept.empno'

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
            table2=etl.sort(table1,'EMPNO')
            print(table2)
except cx_Oracle.Error as error:
    print(error)
