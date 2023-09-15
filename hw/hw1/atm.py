'''
     CS5001
     Spring 2022
     HW1
 
     Chenxuan Xu

Test case #1:
Input: $41
Output: 0 fifties, 2 twenties, 0 tens, 0 fives, 1 ones

Test case #2:
Input: $19
Output: 0 fifties, 0 twenties, 1 tens, 1 fives, 4 ones

Test case #3:
Input: $5
Output: 0 fifties, 0 twenties, 0 tens, 1 fives, 0 ones

'''

def main():
    cost = int(input( "Welcome to PDQ Bank! Amount to withdraw?"))
    print(f"Cha-ching! You asked for ${cost:}")

    # compute the break down for user
    fifties = cost // 50
    remainder = cost % 50
    twenties = remainder // 20
    remainder_2 = remainder % 20
    tens = remainder_2 // 10
    remainder_3 = remainder_2 % 10
    fives = remainder_3 // 5
    remainder_4 = remainder_3 % 5
    ones = remainder_4 // 1

    # output the break down for user
    print(f"That breaks down to:\
    \n {fifties} fifties \n {twenties} twenties\
    \n {tens} tens \n {fives} fives \n {ones} ones")
    

if __name__ == "__main__":
    main()
