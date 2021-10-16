from random import randint

line,line2,rolls,count,total_rolls = [],[],[],0,0

while True:
    chance = randint(1,6)
    rolls.append(chance)
    total_rolls += 1
    if chance != count+1:
        line.clear()
        count = 0
    if chance == count+1:
        line.append(chance)
        count += 1
    if count == 6:
        break

print(line)
print(f"It took {total_rolls} rolls to get {line} in a row.")
print(
    f"There are {rolls.count(1)} ones.\n"+
    f"There are {rolls.count(2)} twos.\n"+
    f"There are {rolls.count(3)} threes.\n"+
    f"There are {rolls.count(4)} fours.\n"+
    f"There are {rolls.count(5)} fives.\n"+
    f"There are {rolls.count(6)} sixes.\n"
    )
