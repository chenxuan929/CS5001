def initialize_FB():
    ''' Function: initialize_FB
        Input: None
        Returns: a list filled with the dwarves and their frined, read from a file.
        First name in the list is the "account holder".
        The rest of the list are their "friends"
    '''

    try:
        with open('facebook.txt', 'r') as infile:
            dwarves = []
            for lines in infile:
                lines = lines.split()
                dwarves.append(lines)
            return dwarves
    except FileNotFoundError:
        print("Error: Could not locate the facebook data")
    except:
        print("An unknown error occurred")
    finally:
        print("----------")

def menu(message, options='PUFQ'):
    ''' Function: menu
        Input: message - user prompt message, options - valid options.
        Returns: 2 tuple - user selection and boolean indicating if the choice was in the valid option list
    '''
    answer = input(message)
    answer = answer.upper()
    if(answer[0] in options.upper()):
        return answer, True
    return answer, False

def get_known_dwarves(dwarves):
    known_dwarves = []
    try:
        for each in dwarves:
            known_dwarves.append(each[0].lower())
    except:
        print("A little bit of an index error occurred. Data is unusable")
    finally:
        return known_dwarves
def find_me(me, dwarves):
    for each in dwarves:
        if each[0].lower() == me.lower():
            return each
        
def print_friends(me, dwarves):
    target = find_me(me,dwarves)
    if target is None:
        print("Warning: Data file is damaged. Cannot process request")
        return
    if len(target) == 1:
        print('You have no friends. Boo hoo.')
        return
    friends = target[1:]
    print(f"{target[0]}'s friends ->", end = " ")
    for each in friends:
        print(each.capitalize(), end= " ")
    print("\n- - - - - - - - \n")

def unfriend(me, dwarves):
    target = find_me(me, dwarves)
    if target is None:
        print("Warning: Data file is damaged. Cannot process request")
        return
    if len(target) == 1:
        print('No one to unfriend')
        return
    print('Here is your current friend list')
    print_friends(me, dwarves)

    undwarf = input('Who do you want to unfriend?')
    undwarf = undwarf.lower().capitalize()
    if (undwarf == target[0]) or (undwarf not in target):
        print('That person isn\'t your friend. No changes made')
        return
    target.remove(undwarf)
    print('Here is your updated friend list')
    print_friends(me, dwarves)

def add_friend(me, dwarves):
    known_dwarves = get_known_dwarves(dwarves)
    target = find_me(me, dwarves)
    if target is None:
        print("Warning: Data file is damaged.  Cannot process request")
        return
    print('*** Here is the current friend list ***')
    print_friends(me, dwarves)
    dwarf = input('Who do you want to add your friend list?')
    dwarf = dwarf.lower()
    if dwarf not in known_dwarves:
        print('That person is not a 7_dwarf! No change made')
        return
    target.append(dwarf)
    print('*** Here is the updated friend list ***')
    print_friends(me, dwarves)

def quitting(dwarves):
    with open('facebook.txt', 'w') as outfile:
        for dwarf in dwarves:
            for each in dwarf:
                outfile.write(each.capitalize() + ' ')
            outfile.write('\n')
            
def main():
    dwarves = initialize_FB()
    known_dwarves = get_known_dwarves(dwarves)
    
    me = input('Which of the 7 is logging in?')
    if me.lower() not in known_dwarves:
        print('Unkown user. Goodbye')
    else:
        while True:
            answer, status = menu(
                'Choose from one of the options below: \n'+
                'P: print friends List\n' +
                'U: Unfriend someone\n' +
                'F: Add a new friend\n' +
                'Q: Quit\n Enter your choice now:')
            if answer == 'P':
                print_friends(me, dwarves)
            elif answer == 'U':
                unfriend(me, dwarves)
            elif answer == 'F':
                add_friend(me, dwarves)
            elif answer == 'Q':
                quitting(dwarves)
                break
        print("Thanks for using Facebooking!")
              
                

    
    

if __name__ == "__main__":
    main()
