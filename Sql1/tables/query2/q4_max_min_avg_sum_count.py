import oracledb
import petl as etl
import pandas as pd
import numpy as np
import config
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
x=int(input("Enter 1 for max, 2 for min, 3 for avg, 4 for sum, 5 for count of Salary =>"))
if x==1:
    sql = 'select max(salary) from demo_4'
elif x==2:
    sql = 'select min(salary) from demo_4'
elif x==3:
    sql = 'select avg(salary) from demo_4'
elif x==4:
    sql = 'select sum(salary) from demo_4'
elif x==5:
    sql = 'select count(salary) from demo_4'
else:
    sql='select * from demo_4'

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
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)