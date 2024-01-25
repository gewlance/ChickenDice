from BackGround import Players
from BackGround import Round
from BackGround import Turns

continuePlaying = True

Players.initPlayers()

while continuePlaying == True: 
    Round.fullRound()
    continuePlaying = Turns.anotherFullRound()