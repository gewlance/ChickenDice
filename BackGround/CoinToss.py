import random
from BackGround import Pot

RoundCount = 1
allTheSame = True
EvensBoosted = False
OddsBoosted = False
tossResults = []

def getRoundCount():
    return RoundCount

def toss():
    x = random.randint(0,1)
    return x

def tossFor(x):
    for i in range(x):
        y = toss()
        #print(f'toss {i+1} is... {y}') toss verifivation
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
    total = 0
    for i in range(3):
        total += tossResults[i]
    if total//2 == 1:
        OddsBoosted == True
        print("Odds Boosted")
    else:
        EvensBoosted == True
        print("Evens Boosted")
        
def firstToss():
    tossFor(3)
    scan()
    global RoundCount 
     
    if allTheSame == False:
        boosted()
        #print(f'pot size is... {Pot.StartPot(RoundCount)}')
    else:
        preGameToss()

def preGameToss():
    global tossResults 
    tossResults = []
    while allTheSame == True:
        tossFor(4)
        global RoundCount 
        RoundCount += 1
        scan()
    print(f"round count is... {RoundCount}")
    print(Pot.initPot())