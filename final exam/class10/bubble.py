"""
    Bubble Sort
"""

def bubble_sort(my_list):
    for passnum in range(len(my_list) - 1, 0, -1):
        for i in range(passnum):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i] # could have done tuple swap here
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp



"""
    Insertion Sort
"""

def insertion_sort(lst):
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index

        # if element at current position > what we want to insert, shift right
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position = position - 1

        # fill the open slot with the value we're inserting
        lst[position] = current_value
        
def main():
    print("Bubble sort")
    lst = [54, 26, 93, 17, 31, 44, 55, 20]
    print("starting list = ", lst)
    bubble_sort(lst)
    print("sorted list = ", lst)

    print("Insertion sort")
    lst = [54, 26, 93, 17, 31, 44, 55, 20]
    print("starting list = ", lst)
    insertion_sort(lst)
    print("sorted list = ", lst)

if __name__ == "__main__":
    main()
