import sqlite3
from User import User
from Terminal import terminal


class DB_Management:
    def __init__(self) -> None:
        self.__cursor = ''
        self.__connection = ''
        self.__createDB()
        self.__currentUser = User()
        self.__warningError = 'Something with the DB went wrong...'
        pass

    def __openConnection(self):
        try:
            self.__connection = sqlite3.connect('players.db')
            self.__cursor = self.__connection.cursor()
        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def __closeConnection(self):
        try:
            self.__connection.close()

        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def __createDB(self):
        try:
            self.__openConnection()
            self.__cursor.execute(
                'CREATE TABLE IF NOT EXISTS player (Name TEXT NOT NULL, Email TEXT NOT NULL UNIQUE, Password TEXT NOT NULL, Victories INT)')
            self.__connection.commit()
            self.__closeConnection()
        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def addUser(self, user):
        try:
            self.__openConnection()
            self.__cursor.executemany(
                'INSERT INTO player VALUES(?, ?, ?, 0)', user)
            self.__connection.commit()
            self.__closeConnection()
            self.__currentUser = User(user[0][0], user[0][1], user[0][2])
            terminal.writeText('Welcome {0}!'.format(
                self.__currentUser.getName().capitalize()), .5)
            return self.__currentUser.getName()

        except sqlite3.IntegrityError:
            terminal.writeText(
                'ERROR Signing In -> Email already used!')
            return -1
        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def findUser(self, email, inputPass):
        try:
            self.__openConnection()
            self.__cursor.execute(
                'SELECT * FROM player WHERE email = ?', email)
            res = self.__cursor.fetchall()
            self.__closeConnection()
            return self.__manageLoginAuth(res, inputPass)

        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def __manageLoginAuth(self, res, inputPass):
        if (res == []):
            terminal.writeText('User not found. Please try again!', 1.5)
            return -1
        if (self.__checkUserPassword(inputPass, res[0][2]) == -1):
            terminal.writeText(
                'Authentification failed -> Wrong password\nPlease, try introducing your credentials again', 1.5)
            return -1
        self.__currentUser = User(res[0][0], res[0][1], res[0][2], res[0][3])
        terminal.writeText('Welcome {0}!'.format(
            self.__currentUser.getName().capitalize()), .5)

        return self.__currentUser.getName()

    def __checkUserPassword(self, inputPass, userPassword):
        if (inputPass != userPassword):
            return -1
        return 0

    def updatePlayerScore(self):
        try:
            newVictories = self.__currentUser.getVictories() + 1
            self.__currentUser.setVictories(newVictories)
            self.__openConnection()
            self.__cursor.execute(
                'UPDATE player SET Victories = ? WHERE email = ?', (newVictories, self.__currentUser.getEmail(),))
            self.__connection.commit()
            self.__closeConnection()
        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def showLeaderBoard(self):
        try:
            self.__openConnection()
            self.__cursor.execute(
                'SELECT Name, Victories FROM player ORDER BY Victories DESC')
            results = self.__cursor.fetchall()
            self.__closeConnection()
            self.__printLeaderBoard(results)
        except sqlite3.Error as error:
            terminal.writeText(self.__warningError)
            terminal.writeText(error)
            return -1

    def __printLeaderBoard(self, data):
        terminal.writeText('\nLEADERBOARD\n-----------')
        currentPos = 0
        leaderboard_maxLength = 20

        for user in data:
            currentPos += 1
            numberOfPoints = '.' * (leaderboard_maxLength -
                                    len(str(currentPos)) - len(user[0]))
            terminal.writeText('{0}. {1} {2} {3}'.format(
                currentPos, str(user[0]).capitalize(), numberOfPoints, user[1]))
            if currentPos == 10:
                break
        terminal.writeText('')


database = DB_Management()
