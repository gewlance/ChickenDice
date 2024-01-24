from BackGround import CoinToss

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
        return 15
    if x == 2:
        return 55
    else:
        return 100 + StartPot(x-1)
    
def initPot():
    addPot(StartPot(CoinToss.getRoundCount()))
    return (f'pot is ... {GetPot()}')