def batch_translate(emoji_file_name: str, directives_file_name: str ):
    try:
        # openning original emoji file
        # creating an empty list to store emojis
        with open(emoji_file_name, 'r') as file:
            emoji = []
            for line in file:
                new_line = line.strip().split()
                emoji.append(new_line)
                # formatting stored emojis line by line
                for i in range(len(emoji)):
                    for j in range(len(emoji[i])):
                        # finding the index position of 'ENGLISH'
                        # changing english words to lower case
                        if emoji[i][j].upper() == 'ENGLISH':
                            j_position = j - 1
                    emoji[i][j_position] = emoji[i][j_position].lower()
                    # changing back the first word 'ENGLISH' 
                    emoji[0][j_position] = emoji[0][j_position].upper()
                    
        # openning directive file to satrt translating different emojis
        with open(directives_file_name, 'r') as file:
            # creating an empty list to format and store file content
            instruction = []
            for line in file:
                new_line = line.strip().split()
                instruction.append(new_line)
        # openning writting the new file as the directive file asked
        for i in range(len(instruction)):
            outfile = open(instruction[i][3], 'w')
            # openning the file as the dirctive file asked
            with open(instruction[i][2], 'r') as file:
                # getting the right position the word need to be replaced
                search = instruction[i][0].upper()
                search_index = emoji[0].index(search) - 1
                target = instruction[i][1].upper()
                target_index = emoji[0].index(target) - 1
                # replacing the word accorfing to the index finded line by line
                for line in file:
                    for word in line.split():
                        for j in range(len(emoji)):
                            search_word = emoji[j][search_index]
                            target_word = emoji[j][target_index]
                            if search_word == word:
                                line = line.replace(search_word, target_word)
                    # writting the line in the file openning at the first step
                    outfile.write(line)
    # dealing with the file not found error           
    except IOError:
        print('File Fot Found or Exist')

def main():
    batch_translate('emojis.txt', 'emoji_directives.txt' )

if __name__ == "__main__":
    main()
