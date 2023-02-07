import cx_Oracle
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select * from demo_3'

try:
    dic1={}
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
            if rows:
                for i in rows:
                    rl=len(i)
                    for j in i:
                        print(j)

except cx_Oracle.Error as error:
    print(error)
