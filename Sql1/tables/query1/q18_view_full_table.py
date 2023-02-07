import oracledb
import petl as etl
import pandas as pd
import config
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select empl.ename,empdept.empno,empdept.deptno,empdept.salary from empl join empdept on empl.empno=empdept.empno'

try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows=cursor.fetchall()
            table1=etl.fromdb(connection.cursor,sql)
            nr=etl.nrows(table1)
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)
