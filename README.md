# Cribbage
python cribbage project


This is a barebones program to compile a deck of cards, draw from it, and maintain a record of which cards are in which place,
then apply scoring rules from the hand value phase of a cribbage game.

Main goal at present is to add a functional turn counter so as to add the value of the crib to either player's hand depending on 
whose turn it is, and have it alternate from an initial state until the end of the game.


Secondary to that is a global points counter, which will run the game until either one of the players' scores exceeds 121 points,
then delcare a winner.

Beyond that, adding a framework for the counting phase of the game, i.e. after the hand is dealt, but before the value is calculated,
alternating on a subroutine with different parameters, until the players cards are both exhausted.

Pipe dream; have the game hide the other player's cards, and possibly some kind of graphic interface to select cards and display
a board with pegs, so we can get on a common server and play in the terminal.

Current issuses: problem with the straight counting module, in which a straight will be dectected even if one of the intermediary cards
is out of place. ie a 4,5,7,8,K hand will register sometimes as a 5 straight. Still trying to puzzle that one out.
