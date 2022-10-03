
from Game import game
from UserInfo import userInfo
from DB import database


def startGame(userName):
    gameResult = game.startGame(userName.capitalize())
    if (gameResult):
        database.updatePlayerScore()


def main():
    userName = -1
    ans = 'play'

    while userName == -1:
        # Returns True -> Has an account | False -> Does not have an account
        alreadyAccount = userInfo.askForUserAccount()
        # Check DB and insert or find for the user account
        # Return -1 if email was already used or something went wrong
        userName = userInfo.getUserAccountData(alreadyAccount, database)

    while (ans != 'exit' and ans != 'quit'):
        startGame(userName)
        database.showLeaderBoard()
        ans = input(
            'Press any key to restart the game: '.format(userName)).lower()

    game.endGame()


if __name__ == "__main__":
    main()
