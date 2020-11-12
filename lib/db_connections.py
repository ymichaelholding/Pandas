import configparser
import cx_Oracle

config = configparser.ConfigParser()
configfile='C:/Users/Michael/PycharmProjects/Python/lib/db_properties.ini'
test = config.read(configfile)


class DBconnections():
    def __init__(self,env):
        self.env = env

    def set_variables(self):
        hostname = ""
        sid = ""
        port = ""
        username = ""
        password = ""
        service = ""

    def db_get_properties(self):
        self.set_variables()
        if self.env=='ORACLE':
             hostname=config['ORACLE']['hostname']
             sid=config['ORACLE']['sid']
             port=config['ORACLE']['port']
             username=config['ORACLE']['username']
             password=config['ORACLE']['password']
             service = hostname + ':' + port + '/' + sid
        return username,password,service

    def oracle_set_connections(self):
        self.set_variables()
        username, password, service = self.db_get_properties()
        conn=cx_Oracle.connect(username,password,service)
        return conn

    def query_result_set(self,sql):
        connection = self.oracle_set_connections()
        cursor = connection.cursor()
        result_set = cursor.execute(sql)
        return result_set
