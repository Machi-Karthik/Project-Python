import random

def coinToss():
    number = int(input("Number of times to flip coin: "))
    recordList = []
    heads = 0
    tails = 0

    for count in range(number):  # loop from 0 to number-1
        flip = random.randint(0, 1)
        if flip == 0:
            print("Heads")
            recordList.append("Heads")
            heads += 1
        else:
            print("Tails")
            recordList.append("Tails")
            tails += 1

    print("\n All flips:", recordList)
    print("Heads count:", heads)
    print("Tails count:", tails)



coinToss()
