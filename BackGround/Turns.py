import random
from BackGround import Round
from BackGround import Pot

highestRoll = 0

def startRoll():
    global highestRoll
    thisRoll = random.randint(1,20)
    highestRoll = thisRoll
    thisPlayer = Round.getCurrentPlayer()
    print(f"\n{thisPlayer} goes for free... his roll is {thisRoll}\n")

def Turn():
    global highestRoll
    if decision() == True:
        Pot.addPot(5)
        thisRoll = random.randint(1,20)
        if thisRoll > highestRoll:
            highestRoll = thisRoll 
            return (f"you rolled a {thisRoll}! Cross your fingers!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else: 
            return (f"you rolled a {thisRoll}, better luck next time\n")
    else:
        return ("passed\n")
    
def lastRoll():
    global highestRoll
    if finalDecision() == True:
        Pot.addPot(10)
        thisRoll = random.randint(1,20)
        if thisRoll > highestRoll:
            highestRoll = thisRoll
            return (f"you rolled a {thisRoll}! You win the Pot!\n")
        elif thisRoll == highestRoll:
            return ("enter tie function here\n")
        else:
            return (f"you rolled a {thisRoll}, better luck next time\n")
    else:
        return ("passed\n")
    
def decision():
    cent_symbol = "\u00A2"
    thisPlayer = Round.getCurrentPlayer()
    choice = int(input(f"It is {thisPlayer}'s turn. Pass for free (0), or pay 5{cent_symbol} to challenge (1). Enter a 1 or a 0..."))
    if choice == 1:
        return True
    else:
        return False
    
def finalDecision():
    cent_symbol = "\u00A2"
    thisPlayer = Round.getCurrentPlayer()
    choice = int(input(f"It is {thisPlayer}'s turn. Pass for free (0), or pay 10{cent_symbol} to Re-Roll (1). Enter a 1 or a 0..."))
    if choice == 1:
        return True
    else:
        return False