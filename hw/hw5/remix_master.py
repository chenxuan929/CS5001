'''
     CS5001
     Fall 2022
     HW5
 
     Chenxuan Xu
'''

from music import *

def substitute(song: list, old_word: str, new_word: str) -> bool:
    # setting flag equal False to start
    # if old word not exist return False
    flag = False
    # removing punctuations using function remove_punc
    for i in range(len(song)):
        song[i] = remove_punc(song[i]).split()
        # checking every elements to search if old words exists
        for j in range(len(song[i])):
            if song[i][j] == old_word:
                # setting flag equal True
                # if old word exist, return True
                flag = True
                # replacing every old word to new word
                song[i][j] = new_word
        # formatting song
        song[i] = ' '.join(song[i])
    return flag
    
def reverse_it(song: list) -> list:
    # creating a new list to store reverse song
    reverse_song = []
    # reversing each elements in original song and put in blank list
    for each in song:
        each_sentence = each.split()
        each_sentence = each_sentence[::-1]
        each_sentence = ' '.join(each_sentence)
        reverse_song.append(each_sentence)
    song = reverse_song
    # removing funtuations in song by using remove_punc function
    for i in range(len(song)):
        song[i] = remove_punc(song[i]).split()
        song[i] = ' '.join(song[i])
    return song

def load_song(selection: int) -> list:
    # if the song don't exist, return blank list
    if selection > len(PLAYLIST) or selection <= 0:
        create_list = []
    # if the song exist, put songs in index 0, put title in index 1
    else:
        select_i = selection - 1
        # using selection - 1 to get the index position
        create_list = [SONGS[select_i]]
        # setting a new list contains song and title
        create_list.append(PLAYLIST[select_i])
        
    return create_list


def remove_punc(words):
    '''
        removing punctuations in songs
    '''
    # setting puctuations list to check
    punctuations = '.?!;:,,'
    for each in words:
        # for each elements in list replace punctuations to ''
        if each in punctuations:
            words = words.replace(each, '')
    return words
            
            
def main():
    while True:
        # asking user to input the choice
        choice = input('\nReMix_Master:\nL: Load a different song\n\
T: Title of curremt song\nS: Substitute a word\nP: Playback your song\n\
R: Reverse it!\nX: Reset to original song\nQ: Quit?\nYoung choice:')
        
        if choice.upper() == 'Q':
            print('Bravo! Your Grammy Award is being shipped to you now!')
            break
        
        if choice.upper() == 'L':
            selection = 0 # setting a 0 for now to start calling function
            # creating songs list with title number
            title_num = 0
            for each in PLAYLIST:
                print(title_num + 1, PLAYLIST[title_num])
                title_num = title_num + 1
            # asking user to choose the song
            selection = int(input("Choose the\
number for song you want to load:"))
            create_list = load_song(selection)
            song = SONGS[selection - 1]
           
        if choice.upper() == 'T':
            # outputing the song title to user
            print("You are mixing the song:", create_list[1])
            print('♬-♬-♬-♬-♬-♬-♬-♬-♬-♬ \
♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬')

        if choice.upper() == 'S':
            # getting the old word that want to replace from user
            old_word = input("What word\
do you want to replace in the existing song?")
            # getting the new word from user
            new_word = input("What new word do you want to use for the song?")
            substitute(song, old_word, new_word)
            
        if choice.upper() == 'P':
            print("Turn up the 808's and drop the beat! Here's yourremix: ")
            format_song = song.copy()
            # removing the puctuations by using function remove_punc
            for i in range(len(format_song)):
                format_song[i] = remove_punc(format_song[i]).split()
                format_song[i] = ' '.join(format_song[i])
            format_song = ' '.join(format_song)        
            print(format_song)
            print('♬-♬-♬-♬-♬-♬-♬-♬-♬-♬ \
♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬')
        
        if choice.upper() == 'R':
            song = reverse_it(song)

        if choice.upper() == 'X':
            song = SONGS[selection - 1]
            

if __name__ == "__main__":
    main()

                

               
