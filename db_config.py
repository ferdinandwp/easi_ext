DB_IP = "10.140.9.15"
DB_NAME = "datacentralserver"
DB_USER = "mikeez"
DB_PASS = "maikil"
DB_PORT = "3306"


DB_CONN_STR = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    DB_USER, DB_PASS, DB_IP, DB_PORT, DB_NAME
)