import cx_Oracle
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
sql = 'select * from demo_1'

try:
    nr = 0
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
            l1=[]
            rows = cursor.fetchall()
            l1.append(rows)
            if rows:
                for row in rows:
                    nr=nr+1
                    rl=len(row)
                    for i in range(0,nr):
                        for j in range(0,rl):
                            #if i==j:
                               print(row[j],end=" - ")

                        print("")
        #print(l1)
except cx_Oracle.Error as error:
    print(error)
