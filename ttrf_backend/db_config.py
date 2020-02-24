DB_IP = "localhost"
DB_NAME = "db_ttrf"
DB_USER = "root"
DB_PASS = "R@ou56206161"
DB_PORT = "3306"


DB_CONN_STR = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    DB_USER, DB_PASS, DB_IP, DB_PORT, DB_NAME
)