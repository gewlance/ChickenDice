playerArray = []

def getPlayerCount():
    count = len(playerArray)
    return count

def getPlayer(x):
    return playerArray[x]

def initPlayers():
    numOfPlayers = int(input("How many players would you like to have? Must be an even number"))
    for i in range(numOfPlayers):
        createPlayer()
    print(playerArray)

def createPlayer():
    playerName = input("What is the name of the player?")
    playerArray.append(playerName)