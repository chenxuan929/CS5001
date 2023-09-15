def get_max(list):
    
    if len(list) == 0:
        big = 0
    else:
        big = list[0]
        for i in range(len(list)):
            if list[i] >= big:
                big = list[i]
    return big

def main():
    print(get_max([1, 4, 9, -19]))
    print(get_max([]))
    print(get_max([-1, -18, -6, -250, -1]))

if __name__ == "__main__":
    main()
    
