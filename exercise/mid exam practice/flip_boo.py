def flip(list):
    for i in range(len(list)):
        if list[i] == True:
            list[i] = False
        elif list[i] == False:
            list[i] = True
    print(list)

def main():
    
    flip([True, False, True])
    flip([True])
    flip([])
    
    # check if I returned 'nothing' to meet question's asking
    print('\n')
    print(type(flip([True, False, True])))

if __name__ == "__main__":
    main()
