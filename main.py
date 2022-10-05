## Import libraries
import random as rd
## Import validations file
import validations

## Rounds of game
rnd = 0
pointsPayer = 0
pointsMachine = 0
localUser = input('Elige tu nombre de Usuario: ')
localEmail = input('Escribe tu Email: ')
localPass = input('Escribe tu Contraseña: ')




def validationForm():
    global localUser
    global localEmail
    global localPass
    
    while True:
        if (validations.validateWords(localUser, 5) == False or len(localUser.strip()) >= 40):
            print('El nombre es demasiado largo')
            localUser = input('Vuelve a escribir el nombre: ')
        if (validations.validateWords(localUser, 5) == True and len(localUser.strip()) < 40):
            break
    
    while True:
        if (validations.checkEmail(localEmail) == False):
            print('El email no es correcto')
            localEmail = input('Vuelve a escribir tu Email: ')
        if (validations.checkEmail(localEmail) == True):
            break
        
    while True:
        if (len(localPass.strip()) >= 10):
            print('La contraseña no puede tener mas de 10 carácteres')
            localUser = input('Vuelve a escribir la contraseña: ')
        if (validations.validateWords(localPass, 1) == False):
            print('La contraseña no puede tener espacios')
            localUser = input('Vuelve a escribir la contraseña: ')
        if (validations.validateWords(localPass, 1) == True and len(localPass.strip()) < 10):
            break
        
    return True

if validationForm() == True:

    ## Class of Game
    
    class game:
        
        actionsList = ['piedra', 'papel', 'tijera']
        
        def __init__ (self, player1):
            ## Variables
            self.actList = self.actionsList
            self.player1 = player1
        
        def randomNum (self):
            return rd.randrange(3)
        
        def chooseRandAction (self):
            return str(self.actionsList[self.randomNum()])
        
        def chooseWinner (self):
            if (self.player1.upper() == self.chooseRandAction().upper()):
                return 'Empate!'
            elif (self.player1.upper() == 'PIEDRA'):
                return 'Has ganado!'
            elif (self.chooseRandAction().upper() == 'PIEDRA'):
                return 'Has perdido!'
            elif (self.player1.upper() == 'PAPEL' and self.chooseRandAction().upper() == 'PIEDRA'):
                return 'Has ganado!'
            elif (self.player1.upper() == 'TIJERA' and self.chooseRandAction().upper() == 'PAPEL'):
                return 'Has ganado!'
            elif (self.player1.upper() == 'PAPEL' and self.chooseRandAction().upper() == 'TIJERA'):
                return 'Has perdido!'
            elif (self.player1.upper() == 'TIJERA' and self.chooseRandAction().upper() == 'PIEDRA'):
                return 'Has perdido!'
            else:
                return 'No has escrito ninguna opción'
    
    
    ## Game loop
    
    def repeatGame():
        ## Declare global variable rnd
        global rnd
        global pointsPayer
        global pointsMachine
        
        
        while True:
            if rnd > 0 and rnd < 5 :
                again = input("¿Pasamos a la siguiente ronda? Escribe y/n: ")
            elif rnd == 5:
                again = input("¿Quieres jugar otra vez? Escribe y/n: ")
            else:
                again = input("¿Empezamos a jugar? Escribe y/n: ")
    
            if again == "n":
                print ("!Gracias por jugar!")
                return
            elif again == "y":
                rnd += 1 
                if rnd <= 5:
                    #variables
                    inputPlayer1 = input('Elige tu acción: piedra, papel, tijera ')
                    
                    nPlay = game(inputPlayer1)
                    nChooseWin = nPlay.chooseWinner()
                    
                    ## Sum victories
                    if (nChooseWin.upper() == 'HAS GANADO!'):
                        pointsPayer += 1
                    elif (nChooseWin.upper() == 'HAS PERDIDO!'):
                        pointsMachine += 1
                    elif (nChooseWin.upper() == 'EMPATE!'):
                        pointsMachine += 1
                        pointsPayer += 1
    
                    
                    ## Print Info
                    print('Vas por la ronda: ' + str(rnd) + '/5')
                    print(nChooseWin)
                    print('Máquina: ' + str(pointsMachine))
                    print(localUser + ': ' + str(pointsPayer))
                    if rnd == 5:
                        
                        infoGame = ''
                        ## printeamos infromación de la partida
                        infoGame += '\nHAS FINALIZADO LA PARTIDA\n'
                        infoGame += 'Información de la partida:\n'
                        infoGame += 'Victorias por la máquina: ' + str(pointsMachine )+ '\n'
                        infoGame += 'Victorias por ' + localUser + ': ' + str(pointsPayer) + '\n'
                        if pointsPayer > pointsMachine :
                            infoGame += 'GANADOR: ' + localUser
                        else:
                            infoGame += 'GANADOR: La máquina'
                            
                        print(infoGame)
                        
                elif rnd == 6:
                    ## Reseteamos el round
                    rnd = 0
                    ## reseteamos puntos
                    pointsMachine = 0
                    pointsPayer = 0
                else:
                    print('Has terminado la partida')
                
            else:
                print ("Tienes que escribir \"y\" o \"n\".")
                
    
    ## Call to validation function
    validationForm()
    ## Call to Game function
    repeatGame()
    