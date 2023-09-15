def is_valid_upc(list_of_integers):
    # getting the length of the list of inregers
    digit = len(list_of_integers)
    # setting the original even and odd digit as zero
    even_digit = 0
    odd_digit = 0
    # getting the number backward in the list
    for i in range(-1, -len(list_of_integers) - 1, - 1):
        # calculate the sum of every even digit
        if i % 2 == 0:
            even_digit += int(list_of_integers[i])
        # calculate the sum of every odd digit
        elif i % 2 == 1:
            odd_digit += int(list_of_integers[i]) 
    # final result should be sume of odd digit and even digit * 3  
    result = odd_digit + even_digit * 3
    
    # If the input is less than 2 digits long
    # or if all the digits have value 0
    # upc code is not valid. 
    if digit < 2 or result == 0:
        return False
    # If it's valid UPC number, result is a multiple of 10
    else:   
        if result % 10 == 0:
            return True
        else:
            return False
