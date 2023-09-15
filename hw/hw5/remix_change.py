'''
     CS5001
     Fall 2022
     HW5
 
     Chenxuan Xu
'''

from music import *

def substitute(song: list, old_word: str, new_word: str) -> bool:
    song = (' '.join(song)).split()
    # creating a blank list to store the index position of finded old word
    check = []
    for i in range(len(song)):
        if song[i].lower() == str(old_word).lower():
            check.append(i)
    # if the length of check list is 0 means no old word exists
    if len(check) == 0:
        print(f"Sorry, I didn't find {old_word} in existing song")
        return False
    else:
        # exists, replacing every item to new then formatting
        for i in check:
            song[i] = str(new_word)
            #print(song) # check ###need to format the song to ['sentence','sentence',...]
        print(song)
        return True, song
    
    
def reverse_it(song: list) -> list:
    # creating a new list to store reverse song
    reverse_song = []
    # reversing each elements in original song and put in blank list
    for each in song:
        each_sentence = each.split()
        each_sentence = each_sentence[::-1]
        each_sentence = ' '.join(each_sentence)
        reverse_song.append(each_sentence)
    # formatting the reverse song
    reverse_song = '\n'.join(reverse_song)
    reverse_song = reverse_song.split('.')
    reverse_song = ''.join(reverse_song)
    # changing the song now by setting song equals the reverse song
    song = reverse_song
    # changing song from string to list
    song = song.split('\n')
    print(song) #check
    return song

def load_song(selection: int) -> list:
    # creating songs list with title number
    title_num = 0
    for each in PLAYLIST:
        print(title_num + 1, PLAYLIST[title_num])
        title_num = title_num + 1
    # asking user to choose the song
    selection = int(input("Choose the number for song you want to load:"))
    # if the song don't exist, return blank list
    if selection > len(PLAYLIST):
        create_list = []
    # if the song exist, put songs in index 0, put title in index 1
    else:
        selection = selection - 1
        create_list = [SONGS[selection]]
        create_list.append(PLAYLIST[selection])
        #print(create_list) #check

    return create_list, selection
    
def main():
    while True:
        choice = input('\nReMix_Master:\nL: Load a different song\n\
T: Title of curremt song\nS: Substitute a word\nP: Playback your song\n\
R: Reverse it!\nX: Reset to original song\nQ: Quit?\nYoung choice:')
        
        if choice.upper() == 'Q':
            print('Bravo! Your Grammy Award is being shipped to you now!')
            break
        
        if choice.upper() == 'L':
            selection = 0 # setting a 0 for now to start calling function
            create_list, selection = load_song(selection)
            song = SONGS[selection]
           
        if choice.upper() == 'T':
            # outputing the song name to user
            print("You are mixing the song:", create_list[1])
            print('♬-♬-♬-♬-♬-♬-♬-♬-♬-♬ \
♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬')

        if choice.upper() == 'S':
            # getting the old word that want to replace from user
            old_word =\
            input("What word do you want to replace in the existing song?")
            # getting the new word from user
            new_word = input("What new word do you want to use for the song?")
            result = substitute(song, old_word, new_word)
            
        if choice.upper() == 'P':
            print("Turn up the 808's and drop the beat! Here's yourremix: ")
            song_format = ' '.join(song)
            # deleting the puctuations in the song to putput
            punctuations = '''!()[]{}:;'""/.,<>?@#$\%^&*_~`'''
            no_punc_song = ""
            for each in song_format:
                if each not in punctuations:
                    no_punc_song = no_punc_song + each
            print(no_punc_song) # ##need format
            print('♬-♬-♬-♬-♬-♬-♬-♬-♬-♬ \
♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬-♬')
        
        if choice.upper() == 'R':
            song = reverse_it(song)

        if choice.upper() == 'X':
            song = SONGS[selection]
            

if __name__ == "__main__":
    main()

                

               
