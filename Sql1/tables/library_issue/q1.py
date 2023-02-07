import config
import oracledb
import petl as etl
import pandas
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql="create table members(mid number(2)primary key, username varchar2(25)unique, pass varchar2(25), fname varchar2(15), lname varchar2(15))"
try:
    with oracledb.connect(
            user=config.username,
            password=config.password,
            dsn=config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
except oracledb.Error as error:
    print(error)



