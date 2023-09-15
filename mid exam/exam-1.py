# question 9
def making_bacon(name):
    if len(name) == 0:
        Bacon_Number = 0
    elif len(name) == len('Kevin Bacon'):
        Bacon_Number = 11
    else:
        Bacon_Number = len(name) % len('Kevin Bacon')
    return Bacon_Number

# question 10
def defensive_fulfillment(a,b):
    if type(a) == type(b):
        answer = a + b
    else:
        answer = None
    return answer

# question 11
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

# question 12
def word_play(word_list, letter_1, letter_2):
    for i in range(len(word_list)):
        word_list[i] = list(word_list[i])
        for j in range(len(word_list[i])):
            if word_list[i][j] == letter_1:
                word_list[i][j] = letter_2
                break
            if word_list[i][j] == letter_2:
                word_list[i][j] = letter_1 
                break
            
    for i in range(len(word_list)):
        word_list[i] = ''.join(word_list[i])

# question 13
def fee_fi_file(file_name):
    search_text = 'Nike'
    replace_text = 'Prof Keith'
    try:
        with open(f"{file_name}.txt", "r") as file:
            data = file.read()
            new_data = data.replace(search_text, replace_text)     
        with open(f"new_{file_name}.txt", "w") as file:
            file.write(new_data)
    except IOError:
        with open('error.txt', 'a+') as file:
            file.write(f'{file_name}.txt does not exist')
