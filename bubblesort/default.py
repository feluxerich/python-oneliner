import random

def bubblesort(lst: list[int]) -> list[int]:
    is_sorted: bool = False
    index: int = 0
    iterations: int = 0
    while not is_sorted:
        if index + 1 >= len(lst):
            index = 0
        if lst[index] <= lst[index + 1]:
            index += 1
            iterations += 1
            if iterations >= len(lst):
                is_sorted = True
            continue
        lst[index], lst[index + 1] = lst[index + 1], lst[index]
        iterations = 0
    return lst

print(bubblesort([random.randint(0, 20) for _ in range(10)]))
