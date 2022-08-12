import os
import random
import time

os.system('cls')

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
#--------------------------------------------------------------------
#RANDOM CARD GENERATOR

card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card_signs = [chr(9829), chr(9830), chr(9824), chr(9827)]

#making list of strings which lookS lika a of deck of cards
deck = []
for i in card_numbers:
    for n in card_signs:
        deck.append(i+n)
#how many decks is used
deck = deck * 1

#function for getting random cards
def get_random(cards):
    random_card = random.choice(cards)
    cards.pop(cards.index(random_card))
    # random_card = 'A#'
    # print(len(deck))
    return random_card

#defining class which gets value and looks of a random card
class RandomCard:
    def __init__(self):
        self.card = get_random(deck)
        if self.card[0] == 'J' or self.card[0] == 'Q' or self.card[0] == 'K' or (self.card[0] == '1' and self.card[1] == '0'):
            self.value = 10
        elif self.card[0] == 'A':
            self.value = 11
        else:
            self.value = int(self.card[0])
    def get_value(self):
        self = self.value
        return self
    def get_looks(self):
        self = self.card
        return self
    def get_first_letter(self):
        self = self.card[0]
        return self

#changes value of aces
def change_value(changes_list, cards_value):
    for i in changes_list:
        if i == 'A' and cards_value > 21:
            cards_value -= 10
    return cards_value

def change_value_check(changes_list, cards_value):
    for i in changes_list:
        if i == 'A' and cards_value > 21:
            return True
    return False

def pop_ace(changes_list):
    for i in changes_list:
        if i == 'A':
            changes_list.pop(changes_list.index(i))
    return changes_list

#---------------------------------------------------------------------
#GAME

money_played_with = int(input("How much money do you have? "))

def hand_value(cards):
    value_of_cards = []
    for n in cards:
        value_of_cards.append(n.get_value())
    hand_pc = sum(value_of_cards)
    return hand_pc

print(LINE_UP, end = LINE_CLEAR)
print(f"Money: {money_played_with}")

while money_played_with > 0:
    #betting
    error = True

    while error:
        bet = input(f"How much do you bet? (1-{money_played_with}, or QUIT) \n>")
        try:
            bet = int(bet)
        except:
            if bet == 'QUIT':
                break
            else:
                print("Input error!")

        if isinstance(bet, int):
            if bet <= money_played_with:
                error = False
            else:
                print("You dont have that much money!")
   
    if bet == 'QUIT':
        print("Sorry to see you leave :(")
        break
    
    print(LINE_UP * 2, end = LINE_CLEAR)
    print(f"Bet: {bet}")
    print(LINE_CLEAR)

    #computer plays first

    changes_list = [] #helps changing the value of ace

    a = RandomCard()
    b = RandomCard()

    hand_pc = []
    hand_pc.append(a) 
    hand_pc.append(b)
    cards_value = hand_value(hand_pc)
    hand_pc_looks = [a.get_looks(), b.get_looks()]

    # print(a.get_looks())
    print("DEALER : ???")
    print('##', b.get_looks())

    #algorithm for changing the value of ace
    changes_list.append(a.get_first_letter())
    changes_list.append(b.get_first_letter())
    check = change_value_check(changes_list, cards_value)
    if check:
        cards_value = change_value(changes_list, cards_value)
        changes_list = pop_ace(changes_list)
    #---

    while cards_value < 17:
        c = 0
        c = RandomCard()
        hand_pc_looks.append(c.get_looks())
        hand_pc.append(c)
        cards_value += c.get_value()
        #algorithm for changing the value of ace
        changes_list.append(c.get_first_letter())
        check = change_value_check(changes_list, cards_value)
        if check:
            cards_value = change_value(changes_list, cards_value)
            changes_list = pop_ace(changes_list)
        #---

    hand_pc_looks = (' '.join(hand_pc_looks))

    #Player

    def update_console(hand_player_looks, cards_value_player):
        hand_player_looks = ' '.join(hand_player_looks)
        print(LINE_UP*4, end = LINE_CLEAR)
        print(f"PLAYER : {cards_value_player}")
        print(hand_player_looks, end = ('\n' * 2))
        print(LINE_CLEAR, end = LINE_UP)
        hand_player_looks = hand_player_looks.split(' ')

    changes_list = [] #helps changing the value of ace

    player_first_card = RandomCard()
    player_second_card = RandomCard()

    hand_player = []
    hand_player.append(player_first_card) 
    hand_player.append(player_second_card)
    cards_value_player = hand_value(hand_player)
    hand_player_looks = [player_first_card.get_looks(), player_second_card.get_looks()]

    #algorithm for changing the value of ace
    changes_list.append(player_first_card.get_first_letter())
    changes_list.append(player_second_card.get_first_letter())
    check = change_value_check(changes_list, cards_value_player)
    if check:
        cards_value_player = change_value(changes_list, cards_value_player)
        changes_list = pop_ace(changes_list)
    #---

    print(f"PLAYER : {cards_value_player}")
    print(player_first_card.get_looks(), player_second_card.get_looks())

    while cards_value_player < 21:
        next_move = input("(H)it, (S)tands, (D)ouble down\n")
        if next_move == "H" or next_move == "D":
            c = 0
            c = RandomCard()
            hand_player.append(c)
            # print(c.get_looks())
            hand_player_looks.append(c.get_looks())
            cards_value_player += c.get_value()
            #algorithm for changing the value of ace
            changes_list.append(c.get_first_letter())
            check = change_value_check(changes_list, cards_value_player)
            if check:
                cards_value_player = change_value(changes_list, cards_value_player)
                changes_list = pop_ace(changes_list)
            #---
            # print(f"value of hand_player is : {cards_value_player}")
            if next_move == "D":
                update_console(hand_player_looks, cards_value_player)
                break
        
        update_console(hand_player_looks, cards_value_player)

        if next_move == "S":
            break
        

    print("------------------------------")

    print(LINE_UP*5, end = LINE_CLEAR)
    print("DEALER :", end = " ")
    time.sleep(1)
    print(cards_value)
    time.sleep(1)
    print(hand_pc_looks, end = ('\n' * 4))

    if cards_value_player > 21:
        money_played_with -= bet
        print(f"You lost {bet}!")
    elif cards_value > 21:
        money_played_with += bet
        print(f"You won {bet}!")
    elif cards_value_player > cards_value:
        if next_move == "D":
            money_played_with += (bet * 2)
            print(f"You won {bet*2}!")
        else:
            money_played_with += bet
            print(f"You won {bet}!")
    elif cards_value > cards_value_player:
        money_played_with -= bet
        print(f"You lost {bet}!")
    else:
        print("It's a tie!")

    if money_played_with == 0:
        print("Thank you for playing with us. You lost all your money loser!")

