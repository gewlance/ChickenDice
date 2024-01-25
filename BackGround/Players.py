from BackGround import Round

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

def challengePayment(playerPos,x):
    newAmount = playerBanks[playerPos] - x
    playerBanks[playerPos] = newAmount

def printPlayers():
    print(playerArray)

def printPlayerBank():
    print(playerBanks)

def initPlayers():
    numOfPlayers = int(input("How many players would you like to have? Must be an even number\t"))
    for i in range(numOfPlayers):
        createPlayer()
    startAmount = int(input("\nHow much will each player start with? $5 = 500\t"))
    initPlayerBanks(startAmount)
    #print(playerArray)

def createPlayer():
    playerName = input("What is the name of the player?\t")
    playerArray.append(playerName)

def initPlayerBanks(x):
    for i in range(getPlayerCount()):
        playerBanks.append(x)