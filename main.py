from BackGround import Players
from BackGround import Round
from BackGround import Turns

continuePlaying = True

Players.initPlayers()

while continuePlaying == True: 
    Round.fullRound()
    continuePlaying = Turns.anotherFullRound()

print("\nTime to divvy up the money!")
for i in range(Players.getPlayerCount()):
    if Players.playerBanks[i]> Players.startAmount:
        difference = Players.playerBanks[i] - Players.startAmount
        print(f"{Players.getPlayer(i)} gets paid {difference}!")
    elif Players.playerBanks[i] >= 0:
        difference = Players.startAmount - Players.playerBanks[i] 
        print(f"{Players.getPlayer(i)} pays {difference}!")
    else:
        difference = Players.startAmount - Players.playerBanks[i]
        print(f"{Players.getPlayer(i)} is in debt! And pays {difference}")