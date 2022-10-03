import random
from Terminal import terminal


class Game:
    def __init__(self) -> None:
        # Computer wins | Player wins
        self.__TYPES_OF_ROL = ['rock', 'paper', 'scissors']
        self.__victoriesToWin = 1
        self.__machineScore = 0
        self.__playerScore = 0
        self.__machinePlay = ''
        self.__gameStatus = 'on'
        self.__playerName = 'You'
        self.__playerWon = False
        pass

    def __setUpGame(self, playerName):
        self.__machineScore = 0
        self.__playerScore = 0
        self.__machinePlay = ''
        self.__gameStatus = 'on'
        self.__playerName = playerName
        self.__playerWon = False
        self.__generateComputerPlay()

    def startGame(self, playerName):
        self.__setUpGame(playerName)
        while self.__gameStatus == 'on':
            self.__cleanTerminalAndShowMatchScore()
            self.playerInput()

        terminal.cleanScreen_and_sayHowToQuit(2)
        return self.__playerWon

    def __generateComputerPlay(self):
        self.__machinePlay = random.choice(self.__TYPES_OF_ROL)

    def __checkRound(self, playerPlay):

        if (playerPlay == 'rock'):
            if (self.__machinePlay == 'paper'):
                self.__machineScore += 1
            if (self.__machinePlay == 'scissors'):
                self.__playerScore += 1

        elif (playerPlay == 'paper'):
            if (self.__machinePlay == 'rock'):
                self.__playerScore += 1
            if (self.__machinePlay == 'scissors'):
                self.__machineScore += 1

        elif (playerPlay == 'scissors'):
            if (self.__machinePlay == 'rock'):
                self.__machineScore += 1
            if (self.__machinePlay == 'paper'):
                self.__playerScore += 1

        terminal.writeText('You choosed: {0} | The machine choosed: {1}'.format(
            playerPlay, self.__machinePlay))

        self.__checkGameStatus()
        self.__generateComputerPlay()

    def __checkGameStatus(self):
        if (self.__machineScore >= self.__victoriesToWin):
            self.__playerWon = False
            terminal.writeText('Nice try, but you lose this time!')
            self.__gameStatus = 'off'

        elif (self.__playerScore >= self.__victoriesToWin):
            self.__playerWon = True
            terminal.writeText('Congratulations, you won this time!')
            self.__gameStatus = 'off'

    def playerInput(self):
        validAns = ['rock', 'paper', 'scissors']
        ans = input(
            'Time to make a play {0}: Rock - Paper - Scissors\n'.format(self.__playerName)).lower()
        if ans == 'exit' or ans == 'quit':
            self.endGame()
        elif (ans not in validAns):
            terminal.writeText(
                'Not a valid input. Please try again!')
        else:
            self.__checkRound(ans)

    def __cleanTerminalAndShowMatchScore(self):
        terminal.cleanScreen_and_sayHowToQuit(1.5)
        terminal.writeText('Current score: {0}: {1} | Machine: {2}'.format(self.__playerName.capitalize(),
                                                                           self.__playerScore, self.__machineScore))

    def endGame(self):
        terminal.exitProgram()


game = Game()
