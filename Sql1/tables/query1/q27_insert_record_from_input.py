import oracledb
import petl as etl
import pandas as pd
import numpy as np
import config
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
emp_no=int(input("Enter Employee Number =>"))
emp_name=input("Enter Employee Name =>")
emp_city=input("Enter City =>")
emp_salary=int(input("Enter Employee Salary =>"))
sql = "insert into demo_3 values(:emp_no,"':emp_name'","':emp_city'",:emp_salary)"
print(sql)

try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql,{'emp_no':emp_no,'emp_name':emp_name,'emp_city':emp_city,'emp_salary':emp_salary})
            # fetch all rows
            connection.commit()
            rows = cursor.fetchall()
            table1=etl.fromdb(connection.cursor, sql,{'emp_no':emp_no,'emp_name':emp_name,'emp_city':emp_city,'emp_salary':emp_salary})
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)
