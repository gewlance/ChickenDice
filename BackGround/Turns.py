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
tiedPlayers = []
alreadyTied = False

def resetTie():
    global tiedPlayers
    global alreadyTied
    tiedPlayers = []
    alreadyTied = False

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

def getTie():
    global tiedPlayers
    if len(tiedPlayers)>0:
        return True
    else:
        return False

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
    global alreadyTied
    roundCount()
    if decision() == True:
        thisPlayer = rC % Players.getPlayerCount() - 1
        if hasMoney(thisPlayer,5) == False:
            return (f"{Players.getPlayer(thisPlayer)} is broke! You cannot roll!\n")
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
            resetTie()
            return (f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! Cross your fingers!\n")
        elif thisRoll == highestRoll and alreadyTied == False:
            tiedPlayers.append(getWinner())
            tiedPlayers.append(thisPlayer)
            print(f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! Tie!\n")
            alreadyTied = True
            return (f"Tied players are... {convertIndextoNames(tiedPlayers)}\n")
        elif thisRoll == highestRoll and alreadyTied == True:
            tiedPlayers.append(thisPlayer)
            print(f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! Tie!!!!\n")
            return (f"Tied players are... {convertIndextoNames(tiedPlayers)}\n")
        else: 
            return (f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}, better luck next time\n")
    else:
        return ("passed\n")
    
def lastRoll():
    global highestRoll
    global winner
    global isBeat
    global alreadyTied
    roundCount()
    thisPlayer = Round.getStartingTurn()

    if isBeat == False and tiedPlayers == []:
        return(f"{Round.getCurrentPlayer()} remains undefeated!")
    #enter condition that prevents a tied started player from rerolling
    
    if tieContainsFirstPlayer() == True:
        return (f"Starting player remains tied! Tied players are... {convertIndextoNames(tiedPlayers)}")

    elif finalDecision() == True:
        thisPlayer = Round.getStartingTurn()
        if hasMoney(thisPlayer,10) == False:
            return (f"{Players.getPlayer(thisPlayer)} is broke! You cannot roll!\n")
        Players.challengePayment(thisPlayer,10)
        Pot.addPot(10)
        resetNaturalOrBoosted()
        thisRoll = roll()
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            winner = Round.getStartingTurn()
            return (f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! You win the Pot!\n")
        elif thisRoll == highestRoll and alreadyTied == False:
            tiedPlayers.append(getWinner())
            tiedPlayers.append(thisPlayer)
            print(f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! Tie!\n")
            alreadyTied = True
            return (f"Tied players are... {convertIndextoNames(tiedPlayers)}\n")
        elif thisRoll == highestRoll and alreadyTied == True:
            tiedPlayers.append(thisPlayer)
            print(f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}! Tie!!!\n")
            return (f"Tied players are... {convertIndextoNames(tiedPlayers)}\n")
        else:
            return (f"{Players.getPlayer(thisPlayer)} rolled a {naturalOrBoosted} {thisRoll}, better luck next time\n")
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
    
def roll():
    global naturalOrBoosted

    newRoll = random.randint(1,5)

    if (CoinToss.getBoosted() == 1) & (newRoll % 2 == 1):
        naturalOrBoosted = "boosted"
        return newRoll + 1
    elif (CoinToss.getBoosted() == 0) & (newRoll % 2 == 0):
        naturalOrBoosted = "boosted"
        return newRoll + 1
    else:
        return newRoll

tieArray = []

def recursiveTieBreaker(Array):#this code is golden. Do not touch this code that has been tweaked for hours
    global winner
    global tieArray
    winner = 0
    winningRoll = 0
    
    #print(f"tie array is... {tieArray}")   #keep for debug purposes

    if len(Array) == 1: #base case, if tie array has one player left, designate that player as winner, exit function
        print (f"{Players.getPlayer(Array[0])} won the tie breaker")
        winner = Array[0]
        return
    
    #reroll if tie remains
    for i in range(len(Array)):
        thisRoll = roll()
        Players.challengePayment((Array[i]),75)
        Pot.addPot(75)
        #print(f"this roll issssss a {thisRoll}")    #keep for debug/ audit purposes
        
        print(f"{Players.getPlayer(Array[i])} rolled a {naturalOrBoosted} {thisRoll} to try to break the tie")
        if thisRoll > winningRoll:
            winningRoll = thisRoll
            winner = i
            print(f"winning roll is...{winningRoll}\n")
            tieArray = []               #reset tie array
            tieArray = [Array[i]]       #add the index of that player into tie array
        elif thisRoll == winningRoll:
            #print("tietietie called")
            tieArray.append(Array[i])   #if another tie occurs, add index of tying player into tie array
        
    #print(f"tie array is....{tieArray}")   #keep for debug purposes

    if len(tieArray) > 1:   #if another tie occurs, special message shows 
        print(f"Tied again! Rerolling for {convertIndextoNames(tieArray)}\n")
        recursiveTieBreaker(tieArray)   #recursion called
    elif len(tieArray) > 0: 
        recursiveTieBreaker(tieArray)   #recursion called

def tieContainsFirstPlayer():
    for i in tiedPlayers:
        if i == Round.getStartingTurn():
            return True
    else:
        return False

def hasMoney(player,x):
    if Players.playerBanks[player]>x:
        return True
    else:
        return False

def convertIndextoNames(Array):
    newList = []
    
    for x in (Array):
        thisPlayer = Players.getPlayer(x)
        newList.append(thisPlayer)

    return newList

def convertToSingleName(Array,index):
    name = Players.getPlayer(Array[index])
    
    return name