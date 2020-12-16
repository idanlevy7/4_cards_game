# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:13:38 2020

@author: Idan
"""
import random

class card:
    def __init__(self,val,suit=""):
        self.val = val
        self.suit = suit
        self.is_shown = False
        self.worth = 100
        if val in ["2","3","4","5","6","7","8","9","10"]:  self.worth = int(val)
        elif val == "A": self.worth = 1
        elif val == "J": self.worth = 11
        elif val == "Q": self.worth = 12
        elif val == "K" :
         #   if suit in ['H',"D"]: self.worth = 13
            if suit in ['♥','♦']: self.worth = 13
            else: self.worth = 0
        elif val == "Joker": self.worth = -1
        elif val == None: self.worth = 0
    def get_val(self):
        return self.val
    def get_suit(self):
        return self.suit
    def get_is_shown(self):
        return self.is_shown
    def set_is_shown(self,val):
        self.is_shown = val
        return
    def get_worth(self):
        return self.worth
        
    
        
class deck:
    def __init__(self):
       # suits=["H","D","C","S"]
        suits = ['♠', '♦', '♥', '♣']
        vals=["A","2","3","4","5","6","7","8","9","10","J","Q","K","Joker"]
        self.cards = []
        for i in range(13):
            for j in range(4):
                    temp = card(vals[i],suits[j])
                    self.cards.append(temp)
        self.cards.append(card("Joker"))
        self.cards.append(card("Joker"))
        random.shuffle(self.cards)
        self.open_card = None
    def get_cards(self):
        return self.cards
    def get_last_card(self):
        return self.cards[-1]
    def get_open_card(self):
        return self.open_card
    def set_open_card(self,new_card):
        self.open_card = new_card
    def pop(self):
        self.set_open_card(self.get_last_card())
        del self.cards[-1]
        return self.get_last_card()
    def size(self):
        return len(self.cards)

        
        
class player:
    def __init__(self,game_deck,num):
        self.cards = []
        for i in range(4):
            self.cards.append(game_deck.pop())
    #    self.card_in_hand = None
        self.num = num
        self.known =[(num,2),(num,3)]
    def switch_card(self,card_num,new_card,game_deck): #sets new card and puts old card in open card deck
        game_deck.set_open_card(self.cards[card_num])
        self.cards[card_num] = new_card
    def get_num(self):
        return self.num
    def get_cards(self):
        return self.cards
    def add_known(self,pos):
        self.known.append(pos)
    def get_known(self):
        return self.known
    def remove_known(self,pos):
        self.known.remove(pos)
            
        
       
        
                            
    