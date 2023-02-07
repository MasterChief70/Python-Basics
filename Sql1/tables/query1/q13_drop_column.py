import cx_Oracle
import petl as etl
import pandas as pd
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'alter table demo_3 drop column salary'

try:
    # connect to the Oracle Database
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            rows=cursor.fetchall()
except cx_Oracle.Error as error:
    print(error)