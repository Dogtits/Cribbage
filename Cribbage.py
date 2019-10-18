"""Cribbage mk 1

kevin_mclaughlin

pthon 3.7.3"""

#libraries
from enum import Enum
from enum import IntEnum
from random import *
from collections import Counter
import collections
import operator
from itertools import combinations, chain, groupby



#lists for each pile of cards
full_deck = []
partial_deck = []
player1_cards = []
player2_cards = []
crib = []
turned_card = []


#value (input type IntEnum) of cards
class Card(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

#suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'


#class CribbageValue(IntEnum):
class CribbageValue(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10

#declare class and card information
class PlayingCard:
    def __init__(self, card_value, card_suit, card_cribValue):
        self.card = card_value  #pass the value into the card
        self.suit = card_suit   #pass the suit into the card
        self.cribValue = card_cribValue

#run 2 for loops to fill out the deck, and define it as a function.
#make sure to return 'full_deck' so it works outside the function
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit), CribbageValue[card.name]))
    return full_deck

create_deck()
"""
#test for full deck
for i in range(0, len(full_deck)):
    print("Card: ", full_deck[i].card)
    print("Suit: ", full_deck[i].suit)
    print("cribValue: ", full_deck[i].cribValue)"""


    



#a function that will apply when we check for 15
def powerset(iterable):
    result = []
    for size in range(len(iterable) + 1):
        result += combinations(iterable, size)
    return result

#use pop function to keep a partial deck that's been drawn from
#with the returnd card removed from the partial deck
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)



partial_deck = list(full_deck)
"""
#test by drawing a random card
test_card = draw_card(partial_deck)
print("you drew a: ", test_card.card, test_card.suit)

for i in range (0, len(partial_deck)):
    print(partial_deck[i].card, partial_deck[i].suit)"""



#deal 6 cards to each player:
def deal_cribbage():
    while(len(partial_deck) > 40):
            player1_cards.append(draw_card(partial_deck))
            player2_cards.append(draw_card(partial_deck))
    return player1_cards and player2_cards


#turn card
def turn_card():
    while(len(partial_deck) > 39):
        turned_card.append(draw_card(partial_deck))
    return turned_card

deal_cribbage()
turn_card()

#print testing for all altered lists
"""
print("player1's cards:-------------")
for i in range(0,len(player1_cards)):
    print( player1_cards[i].suit, player1_cards[i].card, "(", i, ")")
print("playeer2's cards:------------")
for i in range(0,len(player2_cards)):
    print(player2_cards[i].suit, player2_cards[i].card, "(", i, ")")

print("turn card:-------------------")
for i in range(0, len(turned_card)):
    print(turned_card[i].suit, turned_card[i].card)

print("remaining deck:--------------")
for i in range(0, len(partial_deck)):
    print(partial_deck[i].suit, partial_deck[i].card)
    """

"""
#keep track of turns and whose crib it is (DOES NOT WORK YET!)
def whose_crib():
    turn_count = 1
    if turn_count %2 == 0:
        player1_crib = True
        player2_crib = False
    else player1_crib = False and player2_crib = True
    turn_count = turn_count + 1
    return player1_crib, player2_crib"""

def print_turn_card():
    print("turn card:-------------------")
    for i in range(0, len(turned_card)):
        print(turned_card[i].suit, turned_card[i].card)

print_turn_card()


#get crib card 2 with input from user
def get_discard1():
    while (len(player1_cards) > 4):
        print("player1 cards------------")
        for i in range(0,len(player1_cards)):
            print( player1_cards[i].suit, player1_cards[i].card, "(", i, ")")
        crib_card1 = int(input(print("which card does player1 wish to put in the crib? ")))
        if crib_card1 > len(player1_cards) - 1:
            crib_card1 = int(input(print("please select a valid card")))
        crib.append(player1_cards[crib_card1])
        return player1_cards.pop(crib_card1)
    return player1_cards, crib


#get crib card 2 with input from user
def get_discard2():
    while (len(player1_cards) > 4):
        print("player1 cards------------")
        for i in range(0,len(player1_cards)):
            print( player1_cards[i].suit, player1_cards[i].card, "(", i, ")")
        crib_card2 = int(input(print("which card does player1 wish to put in the crib? ")))
        if crib_card2 > len(player1_cards) - 1:
            crib_card2 = int(input(print("please select a valid card")))
        crib.append(player1_cards[crib_card2])
        return player1_cards.pop(crib_card2)
    return player1_cards, crib



#get crib card 3 with input from user
def get_discard3():
    while (len(player2_cards) > 4):
        print("playeer2's cards:------------")
        for i in range(0,len(player2_cards)):
            print(player2_cards[i].suit, player2_cards[i].card, "(", i, ")")
        crib_card3 = int(input(print("which card does player2 wish to put in the crib? ")))
        crib.append(player2_cards[crib_card3])
        return player2_cards.pop(crib_card3)
    return player2_cards, crib


#get crib card 4 with input from user
def get_discard4():
    while (len(player2_cards) > 4):
        print("playeer2's cards:------------")
        for i in range(0,len(player2_cards)):
            print(player2_cards[i].suit, player2_cards[i].card, "(", i, ")")
        crib_card4 = int(input(print("which card does player1 wish to put in the crib? ")))
        crib.append(player2_cards[crib_card4])
        return player2_cards.pop(crib_card4)
    return player2_cards, crib


def get_discards():
    get_discard1()
    get_discard2()
    get_discard3()
    get_discard4()

get_discards()


#print test
print_turn_card()

def print_hands():
    print("player1 cards-------")
    for i in range(0,len(player1_cards)):
        print(player1_cards[i].suit, player1_cards[i].card, "(", i, ")")
    print("player2 cards-------")
    for i in range(0,len(player2_cards)):
        print(player2_cards[i].suit, player2_cards[i].card, "(", i, ")")

    print("crib:---------------")
    for i in range(0, len(crib)):
        print(crib[i].suit, crib[i].card, "(", i, ")")

print_hands()
##########################################################################################
####               DEALING PHASE COMPLETE!         #######################################
##########################################################################################

"""def counting_phase():
    Count = 0
    while Count < 31:
        if player1_count == True
        input(print("player1, please select a card to play:"))"""


##########################################################################################
####               COUNTING PHASE COMPLETE!         #######################################
##########################################################################################

def check_for_knobs_player1():
    player1_points = 0
    for i in range(0,len(player1_cards)):
        if player1_cards[i].card == Card.JACK:
            if player1_cards[i].suit == turned_card[0].suit:
                print("Knobs for one")
                player1_points += 1
    return player1_points
        
def check_for_knobs_player2():
    player2_points = 0
    for i in range(0,len(player2_cards)):
        if player2_cards[i].card == Card.JACK:
            if player2_cards[i].suit == turned_card[0].suit:
                print("Knobs for one")
                player2_points += 1
    return player2_points


def check_for_knobs_crib():
    crib_points = 0
    for i in range(0,len(crib)):
        if crib[i].card == Card.JACK:
            if crib[i].suit == turned_card[0].suit:
                print("Knobs for one")
                crib_points += 1
    return crib_points

def check_for_knobs(player1_points, player2_points, crib_points):
    player1_points = check_for_knobs_player1()
    player2_points = check_for_knobs_player2()
    crib_points = check_for_knobs_crib()
    return player1_points, player2_points, crib_points
    
################################################################################

def check_for_flush_player1():
    player1_points = 0
    if player1_cards[0].suit == player1_cards[1].suit:
        if player1_cards[1].suit == player1_cards[2].suit:
            if player1_cards[2].suit == player1_cards[3].suit:
                if player1_cards[3].suit == turned_card[0].suit:
                    print("flush for five points")
                    player1_points =+ 5
                elif player1_cards[3].suit != turned_card[0].suit:
                    print("flush for four points")
                    player1_points =+ 4
    return player1_points


def check_for_flush_player2():
    player2_points = 0
    if player2_cards[0].suit == player2_cards[1].suit:
        if player2_cards[1].suit == player2_cards[2].suit:
            if player2_cards[2].suit == player2_cards[3].suit:
                if player2_cards[3].suit == turned_card[0].suit:
                    print("flush for five points")
                    player2_points =+ 5
                elif player2_cards[3].suit != turned_card[0].suit:
                    print("flush for four points")
                    player2_points =+ 4
    return player2_points


def check_for_flush_crib():
    crib_points = 0
    if crib[0].suit == crib[1].suit:
        if crib[1].suit == crib[2].suit:
            if crib[2].suit == crib[3].suit:
                if crib[3].suit == turned_card[0].suit:
                    print("flush for five points")
                    crib_points =+ 5
                elif crib[3].suit != turned_card[0].suit:
                    print("flush for four points")
                    crib_points =+ 4
    return crib_points



def check_for_flush(player1_points, player2_points, crib_points):
    player1_points = check_for_flush_player1()
    player2_points = check_for_flush_player2()
    crib_points = check_for_flush_crib()
    return player1_points, player2_points, crib_points
    
################################################################################

################################################################################

def check_pairs_player1():
        player1_points = 0 
        pair_pool = [] #list for hand & turn card
        #combine hand and turn card for 5 card hand
        for i in range(0,len(player1_cards)):
            pair_pool.append(player1_cards[i].card)
        pair_pool.append(turned_card[0].card)
        #List [pair_pool] not has all 5 cards
        counter = Counter()
        #add up cards by numerical value, and identify multiples
        for card_value in pair_pool:
            counter[card_value] += 1

        #c = collections.Counter(pair_pool)
        print(counter)#this part and up works really well. if statements are still useless.
        #for key and value in the populated counter, check the value i.e, how many instances
        for k,v in counter.items():
            if v == 4:
                print("four of a kind")
                player1_points += 8
            elif v == 3:
                print("three of a kind")
                player1_points += 6
            elif v == 2:
                print("pair")
                player1_points += 2
            elif v == 1:
                print("no pair")
        return player1_points



def check_pairs_player2():
        player2_points = 0
        pair_pool = []
        for i in range(0,len(player2_cards)):
            pair_pool.append(player2_cards[i].card)
        pair_pool.append(turned_card[0].card)
        counter = Counter()
        for card_value in pair_pool:
            counter[card_value] += 1

        print(counter)

        for k,v in counter.items():
            if v == 4:
                print("four of a kind")
                player2_points += 8
            elif v == 3:
                print("three of a kind")
                player2_points += 6
            elif v == 2:
                print("pair")
                player2_points += 2
            elif v == 1:
                print("no pair")
        return player2_points



def check_pairs_crib():
        crib_points = 0
        pair_pool = []
        for i in range(0,len(crib)):
            pair_pool.append(crib[i].card)
        pair_pool.append(turned_card[0].card)
        counter = Counter()
        for card_value in pair_pool:
            counter[card_value] += 1

        print(counter)

        for k,v in counter.items():
            if v == 4:
                print("four of a kind")
                crib_points += 8
            elif v == 3:
                print("three of a kind")
                crib_points += 6
            elif v == 2:
                print("pair")
                crib_points += 2
            elif v == 1:
                print("no pair")
        return crib_points

                
            

def check_pairs(player1_points, player2_points, crib_points):
    player1_points = check_pairs_player1()
    player2_points = check_pairs_player2()
    crib_points = check_pairs_crib()
    return player1_points, player2_points, crib_points

################################################################################    
def check_straight_player1():
        player1_points = 0
        straight_pool = []
        for i in range(0,len(player1_cards)):
            straight_pool.append(player1_cards[i].card)
        straight_pool.append(turned_card[0].card)
        #counter = Counter()#this is mostly scrap I think, but leaving it in there so I can remember I already tried it
        #for card_value in straight_pool:
            #counter[card_value] += 1
        print(straight_pool)
        #straight_pool.sort(key=lambda x: x.card)
        #for i in range(0,len(straight_pool)):
        if (min(straight_pool) + 1) in straight_pool:
                if ((min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool and (min(straight_pool)) + 4) in straight_pool:
                    print("5 straight")
                    player1_points += 5
                    return
                elif (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    player1_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player1_points += 3
                    return

###this part abouve is weird, the and statements don't seem to be exclusionary, i.e. if low card, lowcard+1, lowcard+2,
###and lowcard+4 without lowcard+3, it will register as a 5 straight.

        else:
            straight_pool.remove(min(straight_pool))
        
        if (min(straight_pool) + 1) in straight_pool:
                if (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    player1_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player1_points += 3
                    return
        else:
            straight_pool.remove(min(straight_pool))

        if (min(straight_pool) + 1) in straight_pool:
            if (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player1_points += 3
        else:
            print("no straight")
        return player1_points



def check_straight_player2():
        player2_points = 0
        straight_pool = []
        for i in range(0,len(player2_cards)):
            straight_pool.append(player2_cards[i].card)
        straight_pool.append(turned_card[0].card)

        print(straight_pool)

        if (min(straight_pool) + 1) in straight_pool:
                if ((min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool and (min(straight_pool)) + 4) in straight_pool:
                    print("5 straight")
                    player2_points += 5
                    return
                elif (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    player2_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player2_points += 3
                    return

        else:
            straight_pool.remove(min(straight_pool))
        
        if (min(straight_pool) + 1) in straight_pool:
                if (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    player2_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player2_points += 3
                    return
        else:
            straight_pool.remove(min(straight_pool))

        if (min(straight_pool) + 1) in straight_pool:
            if (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    player2_points += 3
        else:
            print("no straight")
        return player2_points


def check_straight_crib():
        crib_points = 0
        straight_pool = []
        for i in range(0,len(crib)):
            straight_pool.append(crib[i].card)
        straight_pool.append(turned_card[0].card)

        print(straight_pool)

        if (min(straight_pool) + 1) in straight_pool:
                if ((min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool and (min(straight_pool)) + 4) in straight_pool:
                    print("5 straight")
                    crib_points += 5
                    return
                elif (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    crib_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    crib_points += 3
                    return

        else:
            straight_pool.remove(min(straight_pool))
        
        if (min(straight_pool) + 1) in straight_pool:
                if (min(straight_pool)) + 2 in straight_pool and (min(straight_pool)) + 3 in straight_pool:
                    print("4 straight")
                    crib_points += 4
                    return
                elif (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    crib_points += 3
                    return
        else:
            straight_pool.remove(min(straight_pool))

        if (min(straight_pool) + 1) in straight_pool:
            if (min(straight_pool)) + 2 in straight_pool:
                    print("3 straight")
                    crib_points += 3
        else:
            print("no straight")
        return crib_points


def check_straight(player1_points, player2_points, crib_points):
    player1_points = check_straight_player1()
    player2_points = check_straight_player2()
    crib_points = check_straight_crib()
    return player1_points, player2_points, crib_points


################################################################################    
"""
def equal_sum_partition(seq):
    subsets = chain.from_iterable(combinations(seq, r) for r in range(len(seq)+1)
    for k, g in groupby(sorted(subsets, key=sum), key=sum):
        group = [set(u) for u in g]
        if len(group) > 1:
            for u, v in combinations(group, 2):
                if not u & v:
                    print(k, (u,v))"""
                               
def check_for_fifteen_player1(): #changed the wholehand & wholehand_sums to fifteens and fifteens_sums and removed the empty list 'fifteens'
        player1_points = 0
        fifteen_pool = []
        for i in range(0,len(player1_cards)):
            fifteen_pool.append(player1_cards[i].cribValue)
        fifteen_pool.append(turned_card[0].cribValue)
        fifteens = powerset(fifteen_pool)
        print(list(map(sum, fifteens)))
        fifteens_sums = list(map(sum, fifteens))
        print(fifteens_sums.count(15))
        player1_points += (fifteens_sums.count(15) *2)
        return player1_points
   

       
def check_for_fifteen_player2():
        player2_points = 0
        fifteen_pool = []
        for i in range(0,len(player2_cards)):
            fifteen_pool.append(player2_cards[i].cribValue)
        fifteen_pool.append(turned_card[0].cribValue)
        fifteens = powerset(fifteen_pool)
        fifteens_sums = list(map(sum, fifteens))
        print(fifteens_sums.count(15))
        player2_points += (fifteens_sums.count(15) *2)
        return player2_points

    
def check_for_fifteen_crib():
        crib_points = 0
        fifteen_pool = []
        for i in range(0,len(crib)):
            fifteen_pool.append(crib[i].cribValue)
        fifteen_pool.append(turned_card[0].cribValue)
        fifteens = powerset(fifteen_pool)
        fifteens_sums = list(map(sum, fifteens))
        print(fifteens_sums.count(15))
        crib_points += (fifteens_sums.count(15) *2)
        return crib_points

    
def check_for_fifteen(player1_points, player2_points, crib_points):
    player1_points = check_for_fifteen_player1()
    player2_points = check_for_fifteen_player2()
    crib_points = check_for_fifteen_crib()
    return player1_points, player2_points, crib_points



################################################################################    


def main():
    player1_points = 0
    player2_points = 0
    crib_points = 0
    


    player1_knob_points, player2_knob_points, crib_knobs_points = check_for_knobs(player1_points, player2_points, crib_points)

    player1_flush_points, player2_flush_points, crib_flush_points = check_for_flush(player1_points, player2_points, crib_points)

    player1_pair_points, player2_pair_points, crib_pair_points = check_pairs(player1_points, player2_points, crib_points)

    player1_straight_points, player2_straight_points, crib_straight_points = check_straight(player1_points, player2_points, crib_points)

    player1_fifteen_points, player2_fifteen_points, crib_fifteen_points = check_for_fifteen(player1_points, player2_points, crib_points)



    player1_points = player1_knob_points +  player1_flush_points + player1_pair_points + player1_fifteen_points + player1_straight_points
    player2_points = player2_knob_points +  player2_flush_points + player2_pair_points + player2_fifteen_points + player2_straight_points
    crib_points = crib_knobs_points + crib_flush_points + crib_pair_points + crib_fifteen_points + crib_straight_points

    print("player 1's points:", player1_points)
    print("player 2's points:", player2_points)
    print("crib points:", crib_points)
    
    return player1_points, player2_points, crib_points


main()


