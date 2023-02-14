import random

inpt: int
rand = random.randint(1, 100)

while inpt != rand:
    inpt = int(input())

    if inpt < rand:
        print('to low')
    elif inpt > rand:
        print('to high')
    else:
        print('right')