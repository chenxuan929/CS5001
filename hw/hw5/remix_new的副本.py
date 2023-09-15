from music import *

def substitute(song, old_word, new_word):
    # creating check_song to checking if old word exist in song and not change song at the same time
    check_song = (' '.join(song)).split()
    # creating a blank list to store the index position of finded old word
    check = []
    for i in range(len(check_song)):
        if check_song[i].lower() == str(old_word).lower():
            check.append(i)
    # if the length of check list is 0 means no old word exists
    if len(check) == 0:
        print(f"Sorry, I didn't find {old_word} in existing song")
        return False
    else:
        # old word exists, replacing every single old word to new old then formatting
        for i in check:
            song = check_song
            song[i] = str(new_word)
            #song = ' '.join(song)
            #song = '\n'.join(song) # print! not change the song
        print(song) ##### how to let song go back to original format? some sentence dont have'.'
        return True, song
    
    
def reverse_it(song):
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
    #print(song) #check
    return song

def load_song(song):
    # creating songs list with title number
    title_num = 0
    for each in PLAYLIST:
        print(title_num + 1, PLAYLIST[title_num])
        title_num = title_num + 1
    # asking user to choose the song
    num = int(input("Choose the number for song you want to load:"))
    # if the song don't exist, return blank list
    if num > len(PLAYLIST):
        create_list = []
        #print(create_list) #check
    # if the song exist, put songs in index 0, put title in index 1
    else:
        num = num - 1
        create_list = [SONGS[num]]
        create_list.append(PLAYLIST[num])
        #print(create_list) #check

    return create_list, num
    
def main():
    while True:
       
        choice = input('\nReMix_Master:\nL: Load a different song\n\
T:Title of curremt song\nS: Substitute a word\nP: Playback your song\n\
R:Reverse it!\nX: Reset to original song\nQ: Quit?\nYoung choice:')
        
        if choice.upper() == 'Q':
            print('Bravo! Your Grammy Award is being shipped to you now!')
            break
        
        if choice.upper() == 'L':
            song = 0 # setting a 0 to start
            create_list,num = load_song(song)
            song = SONGS[num]
            #print(num) # this is the 'selected number - 1'
            #print(create_list) #this is the selected song
           
        if choice.upper() == 'T':
            print(create_list[1])

        if choice.upper() == 'S':
            old_word = input("What word do you want to replace in the existing song?")
            new_word = input("What new word do you want to use for the song?")
            result, song = substitute(song, old_word, new_word)
            
        if choice.upper() == 'P':
            print(song)
            #song = ''.join(song)
            ##### have to format to a string to putput

        if choice.upper() == 'R':
            song = reverse_it(song)

        if choice.upper() == 'X':
            song = SONGS[num]
            

if __name__ == "__main__":
    main()

                

               
