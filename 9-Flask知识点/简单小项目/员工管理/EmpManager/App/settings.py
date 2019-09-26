
def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    driver = DATABASE.get('driver') or 'pymysql'
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,password,host,port,database)



class Config():
    Test = False
    Debug = False

    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevelopConfig(Config):

    DATABASE={
        'dialect':'mysql',
        'driver':'pymysql',
        # access xxxx @localhost:password
        'username':'root',
        'password':'1234',
        'host':'localhost',
        'port':'3306',
        'database':'day071905'
    }

    SQLALCHEMY_DATABASE_URI=get_database_uri(DATABASE)

class TestConfig(Config):

    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        # access xxxx @localhost:password
        'username': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'day071905'
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class ShowConfig(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        # access xxxx @localhost:password
        'username': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'day071905'
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class ProductConfig(Config):
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        # access xxxx @localhost:password
        'username': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': '3306',
        'database': 'day071905'
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


ENV_NAME = {
    'develop':DevelopConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':ProductConfig
}