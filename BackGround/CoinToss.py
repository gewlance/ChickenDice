import random

RoundCount = 1
allTheSame = True
EvensBoosted = False
OddsBoosted = False
tossResults = []

def toss():
    x = random.randint(0,1)
    return x

def tossFor(x):
    for i in range(x):
        y = toss()
        print(f'toss {i+1} is... {y}')
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
        print("Odd")
    else:
        EvensBoosted == True
        print("Even")
        
def firstToss():
    tossFor(3)
    scan()
    global RoundCount 
     
    if allTheSame == False:
        boosted()#odds or even()
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