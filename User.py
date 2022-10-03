class User:
    def __init__(self, name='', email='', password='', victories=0) -> None:
        self.__name = name
        self.__email = email
        self.__password = password
        self.__victories = victories
        pass

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getVictories(self):
        return self.__victories

    def setVictories(self, vic):
        self.__victories = vic
