import random
from BackGround import Players

RoundCount = 1
allTheSame = True
EvensBoosted = False
OddsBoosted = False
tossResults = []

def getBoosted():
    if OddsBoosted == True:
        return 1
    elif EvensBoosted == True:
        return 0

def resetBoosted():
    global OddsBoosted
    global EvensBoosted
    EvensBoosted = False
    OddsBoosted = False

def resetAllTheSame():
    global allTheSame
    allTheSame = True

def resetToss():
    global tossResults
    tossResults = []

def resetRoundCount():
    global RoundCount
    RoundCount = 1

def getRoundCount():
    return RoundCount

def toss():
    x = random.randint(0,1)
    return x

def tossFor(x):
    for i in range(x):
        y = toss()
        tossResults.append(y)

def scan():
    firstFlip = tossResults[0]

    for x in tossResults:
        if x == firstFlip:
            continue
        else:
            global allTheSame
            allTheSame = False

def boosted():
    global OddsBoosted
    global EvensBoosted

    total = 0
    for i in range(3):
        total += tossResults[i]
    if total//2 == 1:
        OddsBoosted = True
        print(f"\nOdds Boosted...")
    else:
        EvensBoosted = True
        print(f"\nEvens Boosted...")
        
def firstToss():
    x = Players.getPlayerCount()
    x -= 1
    tossFor(x)
    scan()
    if allTheSame == False:
        boosted()
    else:
        preGameToss()

def preGameToss():
    global tossResults 
    tossResults = []
    while allTheSame == True:
        x = Players.getPlayerCount()
        tossFor(x)
        global RoundCount 
        RoundCount += 1
        scan()
    print(f"\nround count is... {RoundCount}")