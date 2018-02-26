import MySQLdb
import sys
import argparse
from mysql_config import DB_MYSQL

db = MySQLdb.connect(host=DB_MYSQL['host'],
                     user=DB_MYSQL['user'],
                     passwd=DB_MYSQL['passwd'],
                     db=DB_MYSQL['database'])


def execute_update_query(query):
    try:
        cur = db.cursor()
        cur.execute(query)
        nums_of_rows_effected = cur.rowcount
        print "Total number of rows to be commited is : %s" % nums_of_rows_effected
        user_input = raw_input("Proceed with commiting (y/n) : ")
        if user_input.lower() == 'y':
            db.commit()
            print("Commited !!")
        elif user_input.lower() == 'n':
            db.rollback()
            print("Rolled Back")
        else:
            print("Invalid Option. \n Valid Options are y and n")
            db.rollback()
            sys.exit(1)
    except KeyboardInterrupt as ke:
        db.rollback()
        sys.exit(1)
    except Exception as e:
        print e

    finally:
        db.close()

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert / Update MySQL queries from here.')
    parser.add_argument('--query', required=True, type=str, help='MySQL query to execute')
    args = parser.parse_args()
    execute_update_query(args.query)