from BackGround import Players
from BackGround import Turns
from BackGround import CoinToss
from BackGround import Pot

TurnCount = 0
StartingTurn = 0

def getStartingTurn():
    return StartingTurn

def getCurrentPlayer():
    pCount = Players.getPlayerCount()
    x = TurnCount % pCount
    return Players.getPlayer(x)

def round():
    global TurnCount
    global StartingTurn
    CoinToss.firstToss()
    print(Pot.initPot())
    
    Turns.startRoll()
    TurnCount += 1
    pCount = Players.getPlayerCount()

    while TurnCount % pCount != StartingTurn:
        print(Turns.Turn())
        TurnCount += 1
    
    print(Turns.lastRoll())

    Players.awardPlayer(Turns.getWinner(),Pot.GetPot())
    print(f"BIG WINNER IS... {Players.getPlayer(Turns.getWinner())}")
    
    Players.printPlayers()
    Players.printPlayerBank()
    
    Turns.reset()
    Pot.resetPot()
    CoinToss.resetToss()
    CoinToss.resetAllTheSame()
    CoinToss.resetRoundCount()
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