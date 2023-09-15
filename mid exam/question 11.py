def fulfillment(c,d):
    new_list = []
    for i in range(len(c)):
        new_list.append(c[i])
    new_list.append(d)
    
    return new_list

def main():
    print(fulfillment([1,2,3], 4))

if __name__ == "__main__":
    main()
