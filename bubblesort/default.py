import random
import time

def bubblesort(lst: list[int]) -> list[int]:
    is_sorted = False
    index = 0
    iterations: int = 0
    temp: int
    while not is_sorted:
        if index + 1 >= len(lst):
            index = 0
        if lst[index] <= lst[index + 1]:
            index += 1
            iterations += 1
            if iterations >= len(lst):
                is_sorted = True
            continue
        temp = lst[index]
        lst[index] = lst[index + 1]
        lst[index + 1] = temp
        iterations = 0
    return lst

print(bubblesort([random.randint(0, 20) for _ in range(10)]))
