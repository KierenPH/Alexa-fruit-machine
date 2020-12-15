import random

Item = {
    "1": "Cherry",
    "2": "Bell",
    "3": "Lemon",
    "4": "Orange",
    "5": "Star",
    "6": "Skull"
}


def Roll():
    rolled = []
    for i in range(1, 4):
        randomint = str(random.randint(1, 6))
        roll = Item[randomint]
        rolled.append(roll)
    return rolled


def CalculateWin(topitem, Money):
    if topitem[1] == 2:
        if topitem[0] == 'Skull':
            Money = Money - 1
        else:
            Money = Money + 0.5
    elif topitem[1] == 3:
        if topitem[0] == 'Skull':
            Money = 0
        elif topitem[0] == 'Bell':
            Money = Money + 5
        else:
            Money = Money + 1
    return Money


def countroll(Rolled, Money):
    Money = Money - 0.2
    itemcounts = [0, 0, 0, 0, 0, 0]
    topitem = [0, 0]
    for item in Rolled:
        if item == 'Skull':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[5] = 1
            else:
                itemcounts[5] = itemcounts[5] + 1
            if topitem[1] < itemcounts[5]:
                topitem[0] = 'Skull'
                topitem[1] = itemcounts[5]
        if item == 'Star':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[4] = 1
            else:
                itemcounts[4] = itemcounts[4] + 1
            if topitem[1] < itemcounts[4]:
                topitem[0] = 'Star'
                topitem[1] = itemcounts[4]
        if item == 'Orange':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[3] = 1
            else:
                itemcounts[3] = itemcounts[3] + 1
            if topitem[1] < itemcounts[3]:
                topitem[0] = 'Orange'
                topitem[1] = itemcounts[3]
        if item == 'Lemon':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[2] = 1
            else:
                itemcounts[2] = itemcounts[2] + 1
            if topitem[1] < itemcounts[2]:
                topitem[0] = 'Lemon'
                topitem[1] = itemcounts[2]
        if item == 'Bell':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[1] = 1
            else:
                itemcounts[1] = itemcounts[1] + 1
            if topitem[1] < itemcounts[1]:
                topitem[0] = 'Bell'
                topitem[1] = itemcounts[1]
        if item == 'Cherry':
            if topitem[0] == 0:
                topitem[0] = item
                topitem[1] = 1
                itemcounts[0] = 1
            else:
                itemcounts[0] = itemcounts[0] + 1
            if topitem[1] < itemcounts[0]:
                topitem[0] = 'Cherry'
                topitem[1] = itemcounts[0]
    Money = CalculateWin(topitem, Money)
    return topitem, Money


def createmessage(Rolled, topitem, Money):
    Message = " You rolled, " + Rolled[0] + " , " + Rolled[1] + " , " + Rolled[2] + " "
    if topitem[1] < 2:
        Message = Message + ". Unfortunately you didn't win anything this time. "
    else:
        if topitem[0] == "Skull":
            if topitem[1] == 2:
                Message = Message + " You had 2 skulls, this means you lost £1. "
            elif topitem[1] == 3:
                Message = Message + " You had 3 skulls, this means you lost all your money!"
            else:
                Message = Message + " There was an error with this bit, please contact the developer. "
        elif topitem[1] == 2:
            Message = Message + " You got two of " + topitem[0] + "s this means you won 50p. "
        elif topitem[1] == 3:
            if topitem[0] == "Bell":
                Message = Message + " You got 3 Bells! This means you win £5. "
            else:
                Message = Message + " You got three " + topitem[0] + "s this means you win £1. "
        else:
            Message = Message + " Error, please contact the developer. "

    if Money == 0:
        Message = Message + " You have no money left, unfortunately you can't play anymore. "
    else:
        Message = Message + " "
    return Message


def Game(Money):
    Rolled = Roll()
    topitem, Money = countroll(Rolled, Money)
    Message = createmessage(Rolled, topitem, Money)
    return Money, Message
