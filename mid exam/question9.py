def making_bacon(name):
    if len(name) == 0:
        Bacon_Number = 0
    elif len(name) == len('Kevin Bacon'):
        Bacon_Number = 11
    else:
        Bacon_Number = len(name) % len('Kevin Bacon')
    return Bacon_Number

def main():
    print(making_bacon("Kevin Bacon"))
    print(making_bacon("Keith Bagley"))
    print(making_bacon("K"))
    print(making_bacon(""))

    print(type(making_bacon("")))
    
if __name__ == "__main__":
    main()
