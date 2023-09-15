"""
    Searching algorithms
"""

def linear_search(lst, item): # could use .index(), but writing our own
    times = 0
    for index, value in enumerate(lst):
        times += 1
        if value == item:
            print(f"Times = {times}")
            return index

    print(f"Times = {times}")
    return -1

def binary_search(lst, item):
    low = 0 # Keep track of part of the list (low) searched
    high = len(lst) - 1 # looking at full list at first
    times = 0
    
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        times += 1
        if guess == item:
            print(f"Times = {times}")
            return mid
        if guess > item: # guessed too high
            high = mid - 1
        else:           # guessed too low
            low = mid + 1
    print(f"Times = {times}")
    return -1
"""
    Bring your own search
"""
def choose_your_search(search_function, lst, item):
    return search_function(lst, item)

def main():
    lst = [1, 3, 5, 7, 9, 11, 15, 23]
    print("Index found: ", linear_search(lst, 7))
    print("Index found: ", linear_search(lst, 23))
    print("Index found: ", linear_search(lst, 33))
    print("Index found: ", linear_search(lst, 1))
    print("Starting Binary Search")

    print("Index found: ", binary_search(lst, 7))
    print("Index found: ", binary_search(lst, 23))
    print("Index found: ", binary_search(lst, 33))
    print("Index found: ", binary_search(lst, 1))

    print("Dynamically choose linear search")
    print(choose_your_search(linear_search, lst, 7 ))
    print(choose_your_search(linear_search, lst, 23 ))
    print("Dynamically choose binary search")
    print(choose_your_search(binary_search, lst, 7 ))
    print(choose_your_search(binary_search, lst, 23 ))


if __name__ == "__main__":
    main()

