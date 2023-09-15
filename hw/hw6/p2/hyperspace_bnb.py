'''
     CS5001
     Fall 2022
     HW6
 
     Chenxuan Xu
'''
def load_travelers(travelers_file_name: str):
    # assigning the variable to an empty set to create a dictionary
    travelers = {}
    try:
        # opening given travelers information file
        with open( travelers_file_name, 'r') as file:
            # copying and formatting the information to dictionary
            for line in file:
                new_line = line.strip('\n').split('@')
                travelers[new_line[1]] =\
                    {'name': new_line[0], 'credits': new_line[2]}
    # using file exception to handle error when file can't be found
    except FileNotFoundError:
        print(f'{travelers_file_name} not found. Sorry.')
    # returning the dictionary we create for travelers' information
    return travelers

def process_requests(travelers: dict, request_file_name: str):
    # creating empty list to store booked week number
    week_booked = []
    # creating empty list to store booking information in specified format
    booking = []
    try:
        # openning request file to start arrange reservation
        with open( request_file_name, 'r') as file:
            # creating a empty list
            # storing success reservation information in format
            lines = []
            for line in file:
                lines.append(line.strip('\n').split())
            # For each reservation information
            # calculate whether the week available and credit is sufficient
            for each in lines:
                week_num = int(each[1])
                id_num = each[0]
                # getting information from traveler dictionary
                name = travelers[each[0]]['name']
                credit_s = travelers[each[0]]['credits']
                # current credits should over 500
                # since one week will cost 500 credits
                if week_num not in week_booked and int(credit_s) >= 500:
                    # updating the unavailable week list and newest credits
                    week_booked.append(week_num)
                    travelers[each[0]]['credits'] =\
                        int(travelers[each[0]]['credits']) - 500
                    # updating the success reservation information
                    booking.append(f'{week_num}-{id_num}-{name}')
    # using file exception to handle error when file can't be found
    except FileNotFoundError:
        print(f'{request_file_name} not found.')
    # writting all succuss reservation information to a new file
    # and finish the work
    with open('bookings.txt', 'w') as file:
        for i in range(len(booking)):
            file.write(booking[i] + '\n')
        print('Finished processing reservations. Beam us up Scottie!')
    
    
def main():
    process_requests(load_travelers('travelers.txt'), 'requests.txt')

if __name__ == "__main__":
    main()   
