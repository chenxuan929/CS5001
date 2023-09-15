"""
    Sorting
"""

def bubble_sort(lst):
    for passnum in range(len(lst)-1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                temp = lst[i]   # old school swap rather than python tuple xchange
                lst[i] = lst[i+1]
                lst[i+1] = temp

def insertion_sort(lst):
    for index in range(1, len(lst)):
        current_value = lst[index]
        position = index

        # if element at current pos > what we are inserting, shift right

        while position > 0 and lst[position-1] > current_value:
            lst[position] = lst[position-1]
            position = position - 1

        lst[position] = current_value

def main():
    print("Bubble Sort")
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Starting list = ", lst)
    bubble_sort(lst)
    print("Sorted list = ", lst)
    print("Insertion Sort")
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Starting list = ", lst)
    insertion_sort(lst)
    print("Sorted list = ", lst)
    

if __name__ == "__main__":
    main()

                
