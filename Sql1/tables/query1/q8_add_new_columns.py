import cx_Oracle
import petl as etl
import pandas as pd
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'alter table demo_3 add salary number(5)'

try:
    # connect to the Oracle Database
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            # fetch all rows
            rows = cursor.fetchall()
            table1=etl.fromdb(connection.cursor, sql)
            table2=etl.sort(table1,'ENO')
            #table3=(('ENO, ENAME, CITY'),('6','rahul','ahmedabad'))
            #etl.appenddb(table3,cursor,'DEMO_3')
            print(table2)
except cx_Oracle.Error as error:
    print(error)