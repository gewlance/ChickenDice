playerArray = []
playerBanks = []

def getPlayerCount():
    count = len(playerArray)
    return count

def getPlayer(x):
    return playerArray[x]

def awardPlayer(x,y):
    #oldAmount = playerArray[]
    newAmount = y + playerBanks[x]
    playerBanks[x] = newAmount

def printPlayers():
    print(playerArray)

def printPlayerBank():
    print(playerBanks)

def initPlayers():
    numOfPlayers = int(input("How many players would you like to have? Must be an even number"))
    for i in range(numOfPlayers):
        createPlayer()
    startAmount = int(input("How much will each player start with? $5 = 500"))
    initPlayerBanks(startAmount)
    #print(playerArray)

def createPlayer():
    playerName = input("What is the name of the player?")
    playerArray.append(playerName)

def initPlayerBanks(x):
    for i in range(getPlayerCount()):
        playerBanks.append(x)