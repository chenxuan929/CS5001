"""
    Mergesort
    Recursive, Divide & Conquer
"""

def merge_sort(lst):
    print("Splitting ", lst)
    if len(lst) <= 1:
        print("Base case hit!")
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half) # recursive call with half of list
        merge_sort(right_half)

        i = 0 # index for elements in the left half
        j = 0 # index for elements in the right half
        k = 0 # index for elements in original list

        while i < len(left_half) and j < len(right_half): # merge sublists
            if left_half[i] <= right_half[j]: # if left < right reinsert it
                lst[k] = left_half[i]
                i = i + 1
            else:
                lst[k] = right_half[j]
                j = j + 1
                
            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j  < len(right_half):
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1
            
        print("Merging...", lst)

def main():
    print("Merge sort")
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print("Starting sort here --->")
    merge_sort(lst)
    print("Sorted list = ", lst)

if __name__ == "__main__":
    main()
            
