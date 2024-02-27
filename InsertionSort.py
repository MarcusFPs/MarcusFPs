import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

antaltal = int(input("Hvor mange tal skal sorteres? "))

my_list = [random.randrange(1, 100) for _ in range(antaltal)]
insertion_sort(my_list)
print("Sorteret liste:", my_list)