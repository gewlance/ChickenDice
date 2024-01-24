from BackGround import Players
from BackGround import Turns
from BackGround import CoinToss
from BackGround import Pot

TurnCount = 0
StartingTurn = 0

def getCurrentPlayer():
    pCount = Players.getPlayerCount()
    x = TurnCount % pCount
    return Players.getPlayer(x)

def round():
    global TurnCount
    global StartingTurn
    CoinToss.firstToss()
    Pot.initPot()
    Turns.startRoll()
    #create Pot start and clear functions for every round
    TurnCount += 1
    pCount = Players.getPlayerCount()

    while TurnCount % pCount != StartingTurn:
        print(Turns.Turn())
        TurnCount += 1
    
    print(Turns.lastRoll())

    Players.awardPlayer(Turns.getWinner(),Pot.GetPot())
    
    Players.printPlayers()
    Players.printPlayerBank()
    Pot.resetPot()
    print(f"BIG WINNER IS... {Players.getPlayer(Turns.getWinner())}")
    #print(f"rC is ...{Turns.getRC()}")
    Turns.reset()
    
    StartingTurn += 1
    TurnCount = StartingTurn

def fullRound():
    global StartingTurn
    global TurnCount
    StartingTurn = 0 
    TurnCount = 0
    Turns.resetLastRound()
    for i in range(Players.getPlayerCount() -1):
        round()
    Turns.setLastRound()
    round()

#def win():