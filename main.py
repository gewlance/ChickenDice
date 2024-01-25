from BackGround import CoinToss
from BackGround import Players
from BackGround import Round
from BackGround import Turns

continuePlaying = True

Players.initPlayers()

while continuePlaying == True: 
    #CoinToss.firstToss() #move into round
    Round.fullRound()
    continuePlaying = Turns.anotherFullRound()