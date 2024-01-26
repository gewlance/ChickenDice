import random
from BackGround import Round
from BackGround import Pot
from BackGround import Players
from BackGround import CoinToss

highestRoll = 0
winner = 0
rC = 0
isBeat = False
lastRound = False
naturalOrBoosted = "natural"

def resetNaturalOrBoosted():
    global naturalOrBoosted
    naturalOrBoosted = "natural"

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
    #thisRoll = random.randint(1,20)
    resetNaturalOrBoosted()
    thisRoll = roll()
    highestRoll = thisRoll
    if lastRound == True:
        winner = Players.getPlayerCount() - 1
    else:
        winner = rC % Players.getPlayerCount() - 1
    thisPlayer = Round.getCurrentPlayer()
    print(f"\n{thisPlayer} goes for free... his roll is a {naturalOrBoosted} {thisRoll}\n")

def Turn():
    global highestRoll
    global winner
    global isBeat
    roundCount()
    if decision() == True:
        thisPlayer = rC % Players.getPlayerCount() - 1
        Players.challengePayment(thisPlayer, 5)
        Pot.addPot(5)
        #thisRoll = random.randint(1,20)
        resetNaturalOrBoosted()
        thisRoll = roll()
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            winner =  rC % Players.getPlayerCount() - 1
            isBeat = True
            #win()
            return (f"you rolled a {naturalOrBoosted} {thisRoll}! Cross your fingers!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else: 
            return (f"you rolled a {naturalOrBoosted} {thisRoll}, better luck next time\n")
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
        thisPlayer = Round.getStartingTurn()
        Players.challengePayment(thisPlayer,10)
        Pot.addPot(10)
        #thisRoll = random.randint(1,20)
        resetNaturalOrBoosted()
        thisRoll = roll()
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            winner = Round.getStartingTurn()
            return (f"you rolled a {naturalOrBoosted} {thisRoll}! You win the Pot!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else:
            return (f"you rolled a {naturalOrBoosted} {thisRoll}, better luck next time\n")
    else:
        #if tie breaker exists
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
    
def roll():
    global naturalOrBoosted

    newRoll = random.randint(1,20)
    
    if (CoinToss.getBoosted() == 1) & (newRoll % 2 == 1):
        naturalOrBoosted = "boosted"
        return newRoll + 1
    elif (CoinToss.getBoosted() == 0) & (newRoll % 2 == 0):
        naturalOrBoosted = "boosted"
        return newRoll + 1
    else:
        return newRoll