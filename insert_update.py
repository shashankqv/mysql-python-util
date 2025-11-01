import MySQLdb
import sys
import argparse
from mysql_config import DB_MYSQL

def get_db_connection():
    """
    Establish and return a new MySQL database connection.
    """
    return MySQLdb.connect(
        host=DB_MYSQL['host'],
        user=DB_MYSQL['user'],
        passwd=DB_MYSQL['passwd'],
        db=DB_MYSQL['database']
    )

def execute_update_query(query: str) -> bool:
    """
    Executes an INSERT or UPDATE query with manual commit confirmation.

    Args:
        query (str): The SQL query to execute.

    Returns:
        bool: True if committed, False if rolled back.
    """
    db = get_db_connection()
    try:
        with db.cursor() as cur:
            cur.execute(query)
            nums_of_rows_effected = cur.rowcount
            print("Total number of rows to be committed is: %s" % nums_of_rows_effected)
            user_input = raw_input("Proceed with committing (y/n): ")
            if user_input.lower() == 'y':
                db.commit()
                print("Committed!")
                return True
            elif user_input.lower() == 'n':
                db.rollback()
                print("Rolled Back")
                return False
            else:
                print("Invalid Option. Valid Options are y and n")
                db.rollback()
                sys.exit(1)
    except KeyboardInterrupt:
        db.rollback()
        print("Interrupted. Rolled Back")
        sys.exit(1)
    except Exception as e:
        db.rollback()
        print("Error:", e)
        sys.exit(1)
    finally:
        db.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert / Update MySQL queries from here.')
    parser.add_argument('--query', required=True, type=str, help='MySQL query to execute')
    args = parser.parse_args()
    execute_update_query(args.query)