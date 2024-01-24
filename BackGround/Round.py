from BackGround import Players
from BackGround import Turns

TurnCount = 0
StartingTurn = 0

def getCurrentPlayer():
    pCount = Players.getPlayerCount()
    x = TurnCount % pCount
    return Players.getPlayer(x)

def round():
    global TurnCount
    global StartingTurn
    Turns.startRoll()
    #create Pot start and clear functions for every round
    TurnCount += 1
    pCount = Players.getPlayerCount()

    while TurnCount % pCount != StartingTurn:
        x = TurnCount % pCount 
        print(Turns.Turn())
        TurnCount += 1
    print(Turns.lastRoll())

    #win()
    
    StartingTurn += 1
    TurnCount = StartingTurn

def fullRound():
    for i in range(Players.getPlayerCount()):
        round()