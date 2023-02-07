import config
import oracledb
import petl as etl
import pandas
import numpy as np
oracledb.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql="create table bookstatus(bsid number(2) primary key, mid number(2) references members(mid), bid number(2) references books(bid), " \
    "doi date, dor date, doar date, fine number(5))"
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



