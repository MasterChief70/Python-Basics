import oracledb
import petl as etl
import pandas as pd
import numpy as np
import config
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'alter table demo_3 add salary number(5)'

try:
    # connect to the Oracle Database
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            # fetch all rows
            rows = cursor.fetchall()
            table1=etl.fromdb(connection.cursor, sql)
            table2=etl.look(table1,limit=30)
            print(table2)
except oracledb.Error as error:
    print(error)