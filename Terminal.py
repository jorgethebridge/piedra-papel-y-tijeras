import os
import sys
from time import sleep


class Terminal:
    def __init__(self) -> None:
        pass

    def __clearTerminalScreen(self):
        # posix is os name for linux or mac
        if (os.name == 'posix'):
            os.system('clear')
        # else screen will be cleared for windows
        else:
            os.system('cls')

    def exitProgram(self):
        self.__sayGoodBye()
        os._exit(0)

    def __sayGoodBye(self):
        print('Closing program...')
        sleep(.5)
        self.__clearTerminalScreen()

    def cleanScreen_and_sayHowToQuit(self, timeToWait=0.5):
        sleep(timeToWait)
        self.__clearTerminalScreen()
        print('Write "Quit" or "Exit" to close the game!')

    def writeText(self, textToShow, timeToWait=0):
        print(textToShow)
        sleep(timeToWait)


terminal = Terminal()
