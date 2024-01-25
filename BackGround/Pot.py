from BackGround import CoinToss
from BackGround import Players
from BackGround import Round

Pot = 0

def GetPot():
    return Pot

def setPot(x):
    global Pot 
    Pot = x

def addPot(x):
    global Pot
    Pot += x 

def resetPot():
    global Pot
    Pot = 0

def StartPot(x):
    if x == 1:
        for i in range(Players.getPlayerCount()):
            if i != Round.getStartingTurn():
                #print(f"charging... {Players.getPlayer(i)}")
                Players.challengePayment(i,5)
                #charge func()
            else:
                continue
        return 15
    if x == 2:
        for i in range(Players.getPlayerCount()):
            Players.challengePayment(i,10)
        return 40 + StartPot(x-1)
    else:
        for i in range(Players.getPlayerCount()):
            Players.challengePayment(i,25)
        return 100 + StartPot(x-1)
    
def initPot():
    addPot(StartPot(CoinToss.getRoundCount()))
    return (f'pot is ... {GetPot()}')