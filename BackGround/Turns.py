import random
from BackGround import Round
from BackGround import Pot
from BackGround import Players

highestRoll = 0
winner = 0
rC = 0
isBeat = False
lastRound = False

def reset():
    global winner
    global rC
    winner = 0

def resetLastRound():
    global lastRound
    lastRound = False

def setLastRound():
    global lastRound
    lastRound = True

def getWinner():
    return winner

def getRC():
    return rC

def startRoll():
    global highestRoll
    global winner
    global isBeat
    isBeat = False
    roundCount()
    thisRoll = random.randint(1,20)
    highestRoll = thisRoll
    if lastRound == True:
        winner = Players.getPlayerCount() - 1
    else:
        winner = rC % Players.getPlayerCount() - 1
    thisPlayer = Round.getCurrentPlayer()
    print(f"\n{thisPlayer} goes for free... his roll is {thisRoll}\n")

def Turn():
    global highestRoll
    global winner
    global isBeat
    roundCount()
    if decision() == True:
        Pot.addPot(5)
        thisRoll = random.randint(1,20)
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            winner =  rC % Players.getPlayerCount() - 1
            isBeat = True
            #win()
            return (f"you rolled a {thisRoll}! Cross your fingers!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else: 
            return (f"you rolled a {thisRoll}, better luck next time\n")
    else:
        return ("passed\n")
    
def lastRoll():
    global highestRoll
    global winner
    global isBeat
    roundCount()
    
    if isBeat == False:
        return(f"{Round.getCurrentPlayer()} remains undefeated!")
    elif finalDecision() == True:
        Pot.addPot(10)
        thisRoll = random.randint(1,20)
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            winner = Players.getPlayerCount() - 1
            return (f"you rolled a {thisRoll}! You win the Pot!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else:
            return (f"you rolled a {thisRoll}, better luck next time\n")
    else:
        return ("passed\n")
    
def decision():
    cent_symbol = "\u00A2"
    thisPlayer = Round.getCurrentPlayer()
    choice = int(input(f"It is {thisPlayer}'s turn. Pass for free (0), or pay 5{cent_symbol} to challenge (1). Enter a 1 or a 0..."))
    if choice == 1:
        return True
    else:
        return False
    
def finalDecision():
    cent_symbol = "\u00A2"
    thisPlayer = Round.getCurrentPlayer()
    choice = int(input(f"It is {thisPlayer}'s turn. Pass for free (0), or pay 10{cent_symbol} to Re-Roll (1). Enter a 1 or a 0..."))
    if choice == 1:
        return True
    else:
        return False

def roundCount():
    global rC
    rC += 1

def anotherFullRound():
    choice = int(input("\nDo you wish to play another set of rounds? Yes(1) No(0)"))
    if choice == 1:
        return True
    else:
        return False