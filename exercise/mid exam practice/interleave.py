def interleave(list_1, list_2):
    answer = []
    
    for i in range(len(list_1)):
        # solution is easier and shorter:
        # answer.append(list_1[i] + list_2[i])
        
        list_1[i] = list_1[i] + list_2[i]
        answer.append(list_1[i])

    return answer

def print_list(answer):
    for each in answer:
        print(each, end = " ")
    return

def main():
    # teset 1
    # want to get ['every', 'good', 'boy', 'does', 'fine']
    list_1 = ['e', 'g', 'b', 'd', 'f']
    list_2 = ['very', 'ood', 'oy', 'oes', 'ine']
    answer = interleave(list_1, list_2)
    print(answer)
    # want to get every good boy does fine
    print_list(answer)

    print('\n')

    
    # test 2
    # want to get []
    list_3 = []
    list_4 = []
    print(interleave(list_3, list_4))
    
if __name__ == "__main__":
    main()
    
