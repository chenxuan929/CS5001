from hw4data import *

def decode(data: list ) -> list:
    # creating a blank list to decoding
    decoded_list = []
    # getting the parameter needed to repeat
    for i in range(0, len(data), 2):
        # repeating the parameter for selected times
        for j in range(data[i + 1]):
            # adding in the blank list
            decoded_list.append(data[i])
    return decoded_list
