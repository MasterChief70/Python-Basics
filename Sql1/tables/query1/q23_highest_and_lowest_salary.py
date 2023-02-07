import oracledb
import config
import petl as etl
import pandas as pd
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")

sql1 = 'select edid,empno,deptno,salary from empdept where salary=(select max(salary) from empdept) '
sql2 = 'select edid,empno,deptno,salary from empdept where salary=(select min(salary) from empdept) '
x=int(input("1 for Max, 2 for Min =>"))
try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            if x==1:
                cursor.execute(sql1)
                table1 = etl.fromdb(connection.cursor, sql1)
            elif x==2:
                cursor.execute(sql2)
                table1 = etl.fromdb(connection.cursor, sql2)
            rows=cursor.fetchall()
            nr = etl.nrows(table1)
            table2 = etl.look(table1, limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)



"""min_salary=int(input("Enter Minimum Salary =>"))
max_salary=int(input("Enter Maximum Salary =>"))
,{'min_salary':min_salary,'max_salary':max_salary}"""