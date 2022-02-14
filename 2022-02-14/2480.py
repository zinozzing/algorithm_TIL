#  주사위 세 개

dice = list(map(int, input().split()))
dice = sorted(dice)
set_dice = set(dice)

if len(set_dice) == 1:
    print(10000 + dice[0] * 1000)
elif len(set_dice) == 2:
    if dice.count(dice[0]) == 2:
        print(1000 + dice[0] * 100)
    elif dice.count(dice[1]) == 2:
        print(1000 + dice[1] * 100)
    elif dice.count(dice[2]) == 2:
        print(1000 + dice[2] * 100)    
elif len(set_dice) == 3:
    print(dice[2] * 100) 