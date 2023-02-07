import cx_Oracle
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")

sql = 'select *' \
    'from demo_3' \

try:
    rn=0
    l1=[]
    with cx_Oracle.connect(
                config.username,
                config.password,
                config.dsn,
                encoding=config.encoding) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                rn=rn+1
                if row is None:
                    break
                rl = len(row)
                #for i in (0, rl - 1):
                    #print(row[i], " - ", end="")
                print(row[0]," - ",row[1]," - ",row[2])

except cx_Oracle.Error as error:
    print(error)
