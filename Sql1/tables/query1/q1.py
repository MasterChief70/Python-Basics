import cx_Oracle
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")

sql = 'select *' \
    'from demo_3 ' \

try:
    with cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                print(row)
except cx_Oracle.Error as error:
    print(error)
