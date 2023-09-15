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
        
    print(word_list)#
    
def main():
    word_play(["Hello", "World"], "H", "J")
    word_play(["The"], "T", "j")


if __name__ == "__main__":
    main()
