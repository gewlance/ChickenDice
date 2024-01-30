playerArray = []
playerBanks = []

def getPlayerCount():
    count = len(playerArray)
    return count

def getPlayer(x):
    if x == -1:
        y = getPlayerCount() - 1
        return getPlayer(y)
    else:
        return playerArray[x]

def awardPlayer(x,y):
    newAmount = y + playerBanks[x]
    playerBanks[x] = newAmount

def challengePayment(playerPos,x):
    newAmount = playerBanks[playerPos] - x
    playerBanks[playerPos] = newAmount

def printPlayers():
    print(playerArray)

def printPlayerBank():
    print(playerBanks)

def initPlayers():
    numOfPlayers = int(input("\nHow many players would you like to have? Must be an even number\t"))
    print()
    for i in range(numOfPlayers):
        createPlayer()
    startAmount = int(input("\nHow much will each player start with? $5 = 500\t"))
    initPlayerBanks(startAmount)

def createPlayer():
    playerName = input("What is the name of the player?\t")
    playerArray.append(playerName)

def initPlayerBanks(x):
    for i in range(getPlayerCount()):
        playerBanks.append(x)