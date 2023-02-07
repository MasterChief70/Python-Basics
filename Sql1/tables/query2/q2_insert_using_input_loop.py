import oracledb
import petl as etl
import pandas as pd
import numpy as np
import config
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")

x=int(input("Enter Number of Rcords to Insert =>"))
try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            for i in range(1, x + 1):
                print("For Record no.  ", i)
                e_no = int(input("Enter Employee Number =>"))
                e_name = input("Enter Employee Name =>")
                e_salary = int(input("Enter Employee Salary =>"))
                sql = "insert into demo_4 values(:e_no,"':e_name'",:e_salary)"
                cursor.execute(sql, {'e_no': e_no, 'e_name': e_name, 'e_salary': e_salary})
                connection.commit()
            rows = cursor.fetchall()
            table1=etl.fromdb(connection.cursor, sql,{'e_no':e_no,'e_name':e_name,'e_salary':e_salary})
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)
