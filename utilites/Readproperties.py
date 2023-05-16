import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\mukes\\PycharmProjects\\pythonpytest\\Configurations\\config.ini")



class Readconfig():

    @staticmethod
    def geturl():
        url = config.get('common info', 'Url')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'Username')
        return username


    @staticmethod
    def getpassword():
        password = config.get('common info', 'Password')
        return password
