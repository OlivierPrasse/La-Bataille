import sys
import math
from collections import deque

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def get_value(card_str):
    return CARD_VALUES[card_str[:-1]]

p1_deck = deque()
p2_deck = deque()

n = int(input())  
for i in range(n):
    cardp1 = input() 
    p1_deck.append(get_value(cardp1))

m = int(input()) 
for i in range(m):
    cardp2 = input()  
    p2_deck.append(get_value(cardp2))

rounds = 0
is_pat = False

while len(p1_deck) > 0 and len(p2_deck) > 0:
    rounds += 1
    
    card1 = p1_deck.popleft()
    card2 = p2_deck.popleft()

    p1_stake = [card1]
    p2_stake = [card2]
    
    winner = None
    
    while card1 == card2:
        if len(p1_deck) < 4 or len(p2_deck) < 4:
            is_pat = True
            break
 
        for _ in range(3):
            p1_stake.append(p1_deck.popleft())
            p2_stake.append(p2_deck.popleft())
 
        card1 = p1_deck.popleft()
        card2 = p2_deck.popleft()
        
        p1_stake.append(card1)
        p2_stake.append(card2)
    
    if is_pat:
        break
  
    if card1 > card2:
        p1_deck.extend(p1_stake + p2_stake)
    else:
        p2_deck.extend(p1_stake + p2_stake)

if is_pat:
    print("PAT")
elif len(p1_deck) > 0:
    print(f"1 {rounds}")
else:
    print(f"2 {rounds}")
