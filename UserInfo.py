from User import User
from Terminal import terminal


class UserInfo:
    def __init__(self) -> None:
        pass

    def askForUserAccount(self, default='yes'):
        validAnswers = {"yes": True, "y": True,
                        "ye": True, "no": False, "n": False}
        while True:
            terminal.cleanScreen_and_sayHowToQuit(0)
            ans = input('Do you already have an account? [Y/n]').lower()
            if ans == 'exit' or ans == 'quit':
                return terminal.exitProgram()
            elif default is not None and ans == '':
                return validAnswers[default]
            elif ans in validAnswers:
                return validAnswers[ans]
            else:
                terminal.writeText(
                    'Please respond with "yes" or "no" (or "y" or "n")', 1)

    def getUserAccountData(self, alreadyAccount, database):
        # Ask for user Data
        userInput = self.askForUserData(alreadyAccount)

        # Log in user
        if alreadyAccount:
            return database.findUser((userInput.getEmail(),), userInput.getPassword())

        # Sign in user
        elif not alreadyAccount:
            dataArray = [
                (userInput.getName(), userInput.getEmail(), userInput.getPassword()), ]
            # DB Returning -1 if mail already exists
            return database.addUser(dataArray)

        terminal.writeText(
            'Debugging error... something got corrupted in UserInfo.py')
        return -1

    def askForUserData(self, alreadyAccount):
        name = ''
        if not (alreadyAccount):
            name = self.validateUserDataAnswer('Name')
        email = self.validateUserDataAnswer('Email')
        password = self.validateUserDataAnswer('Password')

        userInput = User(name, email, password)

        return userInput

    def validateUserDataAnswer(self, typeOfInput):
        ans = ''
        while ans == '':
            ans = input('{0}: '.format(typeOfInput))
            terminal.cleanScreen_and_sayHowToQuit(0.1)
            if ans.lower() == 'exit' or ans.lower() == 'quit':
                terminal.exitProgram()
            elif (ans != ''):
                return ans
            else:
                terminal.writeText('Please introduce a non empty asnwer!')


userInfo = UserInfo()
