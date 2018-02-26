DB_MYSQL = {"host": "",  # hostname
            "user": "",  # mysql username
            "passwd": "",  # password
            "database": ""  # Database name you want to connect.
            }

try:
    from mysql_config_local import *
except ImportError:
    pass