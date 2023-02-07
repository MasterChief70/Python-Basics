import cx_Oracle
import petl as etl
import pandas as pd
import config
cx_Oracle.init_oracle_client(lib_dir=r"E:\Downloads\instantclient_21_6")
def update_salary(eno,salary):
    """
    update new amount for salary
    :param eno:
    :param salary:
    :return:
    """
    sql = 'update demo_3 set salary= :salary where eno= :eno'

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
                connection.commit()
                table1=etl.fromdb(connection.cursor, sql)
                table2=etl.sort(table1,'ENO')
                table3=etl.addfield('demo_3','SALARY',10000)
                #table3=(('ENO, ENAME, CITY'),('6','rahul','ahmedabad'))
                #etl.appenddb(table3,cursor,'DEMO_3')
                print(table2)
    except cx_Oracle.Error as error:
        print(error)

if __name__ == '__main__':
    update_salary(1,10000)