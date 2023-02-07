import cx_Oracle
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select * from demo_3 order by ename'

batch_size = 30
try:
    with cx_Oracle.connect(
            config.username,
            config.password,
            config.dsn,
            encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            # execute the SQL statement
            cursor.execute(sql)
            while True:
                # fetch rows
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                # display rows
                for row in rows:
                    print(row)
except cx_Oracle.Error as error:
    print(error)
