def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect')
    driver = DATABASE.get('driver')
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,driver,username,password,host,port,database)
class Config():
    Test = False
    Debug = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    Debug = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'ccq',
        'password':'123',
        'host':'localhost',
        'port':'3306',
        'database':'day06flask1'
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class TestConfig(Config):
    Test = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'ccq',
        'password':'123',
        'host':'localhost',
        'port':'3306',
        'database':'day06flask1'
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class ShowConfig(Config):
    Debug = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'ccq',
        'password':'123',
        'host':'localhost',
        'port':'3306',
        'database':'day06flask1'
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class Product(Config):
    Debug = True
    DATABASE = {
        'dialect':'mysql',
        'driver':'pymysql',
        'username':'ccq',
        'password':'123',
        'host':'localhost',
        'port':'3306',
        'database':'day06flask1'
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

ENV_NAME = {
    'develop':DevelopConfig,
    'test':TestConfig,
    'show':ShowConfig,
    'product':Product
}