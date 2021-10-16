from random import randint

class Useless_Machinery():
    def __init__(pointless):
        pointless.line,pointless.rolls,pointless.count,pointless.total_rolls = [],[],0,0

    def OneToSix_InARow(pointless):
        while True:
            chance = randint(1,6)
            pointless.rolls.append(chance)
            pointless.total_rolls += 1
            if chance != pointless.count+1:
                pointless.line.clear()
                pointless.count = 0
            if chance == pointless.count+1:
                pointless.line.append(chance)
                pointless.count += 1
            if pointless.count == 6:
                break

unneccessary = Useless_Machinery()
unneccessary.OneToSix_InARow()
print(unneccessary.line)
print(f"It took {unneccessary.total_rolls} rolls to get {unneccessary.line} in a row.")
print(
    f"There are {unneccessary.rolls.count(1)} ones.\n"+
    f"There are {unneccessary.rolls.count(2)} twos.\n"+
    f"There are {unneccessary.rolls.count(3)} threes.\n"+
    f"There are {unneccessary.rolls.count(4)} fours.\n"+
    f"There are {unneccessary.rolls.count(5)} fives.\n"+
    f"There are {unneccessary.rolls.count(6)} sixes.\n"
    )