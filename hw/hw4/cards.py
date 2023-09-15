import random

def create_deck():
    # listing poker value
    card_num = \
             ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # creating the original deck list of 52 poker cards
    cards = []
    index = 0
    while index < 13:
        # anrranging suit of the cards with values:
        # 's' for spades, 'h' for hearts, 'd' for diamonds, 'c' for clubs
        cards.append(card_num[index] + 's')
        cards.append(card_num[index] + 'h')
        cards.append(card_num[index] + 'd')
        cards.append(card_num[index] + 'c')
        index = index + 1
    # getting original cards
    return cards

def shuffle(cards):
    # creating a new cards list to shuffle
    # avoiding changing the original cards
    new_cards = []
    for card in cards:
        new_cards.append(card)

    # shufflling 100 times to get a totally new card list
    times = 0
    while times < 100:
        # choosing two random cards to change position
        c_1 = random.randint(0, len(new_cards) - 1)
        c_2 = random.randint(0, len(new_cards) - 1)
        new_cards[c_1], new_cards[c_2] = new_cards[c_2], new_cards[c_1]
        
        times = times + 1
        
    return new_cards

def deal(number_of_hands, number_of_cards, cards):
    # hands values allowed: 1..4
    # cards values allowed: 0..13
    
    # creating blank list for all of the hands' dealt cards
    dealt = []
    
    for i in range(number_of_hands):
        dealt.append([])
        
    index = 0
    # getting the cards for each hands and removing from deck
    for i in range(number_of_hands):
        for j in range(number_of_cards):
            dealt[i].append(cards.pop())

    return dealt
