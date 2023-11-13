import os
from dotenv import load_dotenv
import psycopg2


def db_connect(db_name, db_user, db_pass):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=db_user,
            password=db_pass,
            port='5432'
        )
        print('Connection set up successfully!!!')
        return conn
    except Exception as e:
        print('There was an error trying to connect to db: ', str(e))
        exit()


def execute_db_setup(conn):
    try:
        cur = conn.cursor()
        cur.execute(open("car_offer_db_schema.sql", "r").read())
        cur.close()
        conn.commit()
        print('Operations executed and commited!')
    except Exception as e:
        print('There was an error trying to execute to set up .sql commands: ', str(e))
    finally:
        close_db_connection(conn)


def close_db_connection(conn):
    conn.close()
    print('Connection closed!')


if __name__=='__main__':
    load_dotenv()

    db = os.getenv('POSTGRES_DB', None)
    user = os.getenv('POSTGRES_USER', None)
    password = os.getenv('POSTGRES_PASSWORD', None)

    # print('db: ', db)
    # print('user: ', user)
    # print('password: ', password)

    conn = db_connect(db, user, password)
    execute_db_setup(conn)
