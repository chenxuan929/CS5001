'''
    Coin flip with functions
'''

def flip_coin(number):
    '''flip_coin answers 0 or 1 representing heads or tails'''
    return number % 2

def main():
    print("Enter any integer and I'll convert it to either 0 for heads or 1 for tails")
    number = int(input("Enter your number:"))
    # heads_or_tails = flip_coin(number)
    print("Your coin flip is", flip_coin(number))

if __name__ == "__main__":
    main()




def calculate_gpa(current_gpa, num_classes, new_grade):
    '''
        calculate_gpa
        input: current gpa(float), num_classes(int), new grade(float)
        returns: updated GPA with one class added
    '''
    old_total = current_gpa * num_classes
    new_total = old_total + new_grade
    new_gpa = new_total / (num_classes + 1)
    return new_gpa
def main():
    print(calculate_gpa(0,0,3.5)) #no classes yet, add one
    print(calculate_gpa(3.6,1,4.0)) #1 class, add another A

if __name__ == "__main__":
    main()




    
    
