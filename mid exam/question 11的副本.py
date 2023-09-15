def fulfillment(c,d):
    new_list = []
    if type(c) != int:
        for i in range(len(c)):
            new_list.append(c[i])
            
        new_list.append(d)

    elif type(d) != int:
        for i in range(len(d)):
            new_list.append(d[i])
            
        new_list.append(c)

    return new_list

def main():
    print(fulfillment([1,2,3],44))
    print(fulfillment(4, [1,2,3]))

if __name__ == "__main__":
    main()
