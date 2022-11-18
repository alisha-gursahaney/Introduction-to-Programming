# Name: Alisha Gursahaney
# Net Id: amg9zd
# Partner: Sean Pettit scp5jt breakout room 20

# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)

marbles = 0
pick = 0


def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while (ans*2) <= n:
        ans = ans * 2
    return ans


print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))
turn_choice = input("Who will start? (p or c): ")
turn = False
if turn_choice == 'p':
    turn = True

while marbles != 0:
    print("The pile has", marbles, "marbles in it.")
    if turn == False:
        take = 1
        target = pow2(marbles)
        take = marbles - target
        if take < 1:
            take = 1
        marbles = marbles - take
        print("The computer takes", take, "marbles.")
    else:
        can_take = marbles // 2
        take = 0
        if take <= can_take:
            take = int(input("How many marbles do you want to take (1-" + str(can_take) + "): "))
        marbles = marbles - take
    turn = not turn


if turn:
    print("The player wins!")
else:
    print("The computer wins!")
