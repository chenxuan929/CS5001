'''
     CS5001
     Spring 2022
     HW1
 
     Chenxuan Xu
'''
def main():
    # get the legth and width of the office from the user
    length = float(input("Enter the length of the office (in feet)"))
    width = float(input("Enter the width of the office (in feet)"))

    # compute the area
    area = length * width
    area_2 = area * 0.092903
    cost = 21.10 * area_2

    # output the area and cost
    print(f"The area of the office is {area:.2f} square feet \n...\
which is {area_2:.2f} square meters \n......\
and you will pay €{cost:.2f} per month")


if __name__ == "__main__":
    main()
