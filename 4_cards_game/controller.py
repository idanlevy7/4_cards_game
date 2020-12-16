# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:20:40 2020

@author: Idan
"""
import tkinter as tk
import model
import view
from numpy import random
import numpy


class controller():
    def __init__(self):
        self.root = tk.Tk()
        self.myGame = view.GUI(self.root,self)
        self.game_deck = model.deck()
        self.players = [model.player(self.game_deck,0),model.player(self.game_deck,1),model.player(self.game_deck,2)]
        self.current_card = None
        self.open_card = None
        self.turns = 0
        self.show_card1((0,2))
        self.show_card1((0,3))
        self.clicked_win = -1
        
    def run(self):
        self.turn(0)
        self.root.mainloop()
        

    def get_game(self):
        return self.myGame
    def get_game_deck(self):
        return self.game_deck
    def get_root(self):
        return self.root
    def get_players(self):
        return self.players
    def get_player_card(self,pos):
        return self.players[pos[0]].cards[pos[1]]
    def set_player_card(self,pos,new_card):
        self.players[pos[0]].cards[pos[1]] = new_card
    def set_open_card(self,card):
        self.open_card = card
    def get_open_card(self):
        return self.open_card
    def set_current_card(self,card):
        self.current_card = card
    def get_current_card(self):
        return self.current_card
    def get_turns(self):
       return self.turns
    def set_turns(self,n):
        self.turns = n
        return n
    def get_clicked_win(self):
        return self.clicked_win
    def set_clicked_win(self,a):
        self.clicked_win=a
    
        
        
        


    def show_card1(self,pos):
        card = self.get_player_card(pos)
        if card.get_is_shown():
            self.get_game().wrong_card()
            return 0
        else:
            if card.get_suit() in ['♥','♦']: c = "red"
            else: c= "black"
            self.get_game().show_card(pos,card.get_val()+card.get_suit(),c)
            card.set_is_shown(True)
            return 1
        
        
            
    def draw(self):
        self.get_game().disable_win()
        new_card = self.get_game_deck().pop()
        self.set_current_card(new_card)
        self.get_game().draw_show(new_card.get_val()+new_card.get_suit())
        self.get_game().disable_draw()
        return new_card
    
    def win_click(self):
        self.get_game().disable_draw()
        self.get_game().disable_win()
        self.set_clicked_win(0)
    
    def look(self,num):
        self.get_game().enable_cards()
        self.get_game().change_explain("choose card to look at")
        self.get_root().wait_variable(self.get_game().btn_var)
        pos = self.get_pos_from_btn_var()
        if pos in ["open","current"]: self.get_game().wrong_card()
        else:
            if num == 0 and pos[0] != 0: self.get_game().wrong_card()
            elif num == 1 and pos[0] == 0: self.get_game().wrong_card()
            else: self.show_card1(pos)
        self.get_game().disable_cards()
        if num == 0: self.get_game().disable_look_self()
        else: self.get_game().disable_look_other()
        return
        
    def throw_card(self):
        self.get_game().enable_player_cards()
        self.get_game().change_explain("choose card to throw")
        self.get_root().wait_variable(self.get_game().btn_var)
        pos = self.get_pos_from_btn_var()
        card = self.get_player_card(pos)
        if card.get_val() == self.get_open_card().get_val():
            self.set_open_card(card)
            self.get_game().open_show(card.get_val()+card.get_suit())
            empty = model.card(None)
            self.set_player_card(pos,empty)
            self.get_game().show_card(pos,"None","black")
        else:
            self.get_game().wrong_card()
        self.get_game().change_explain("its your turn")
        return
            
            
        
        
    def get_pos_from_btn_var(self):
        var = self.get_game().btn_var.get()
        if var == "": return None
        if var == "open":return "open"
        if var[0] == "M": i=0
        elif var[0] == "L": i=1
        else: i=2   
        if var[1] == "1":
            if var[2] == "1": j=0
            else: j=1
        else:
            if var[2] == "1": j=2
            else: j=3
        return (i,j)
        
                
    
    def replace(self):
        self.get_game().enable_cards()
        self.get_game().change_explain("choose a card of your own")
        self.get_root().wait_variable(self.get_game().btn_var)
        pos1 = self.get_pos_from_btn_var()
        self.get_game().change_explain("choose other player's card")
        self.get_root().wait_variable(self.get_game().btn_var)
        pos2 = self.get_pos_from_btn_var()
        if (pos1[0]==0 and pos2[0]!=0):
            temp = self.get_player_card(pos1)
            self.set_player_card(pos1,self.get_player_card(pos2))
            self.set_player_card(pos2,temp)
            for p in [pos1,pos2]:
                card = self.get_player_card(p)
                if card.get_suit() in ['♥','♦']: c = "red"
                else: c= "black"
                if card.get_is_shown(): self.get_game().show_card(p,card.get_val()+card.get_suit(),c)
                else: self.get_game().show_card(p,"   ","black")
            if pos1 in self.get_players()[pos1[0]].get_known() and pos2 not in self.get_players()[pos1[0]].get_known():
                self.get_players()[pos1[0]].add_known(pos2)
                self.get_players()[pos1[0]].remove_known(pos1)
            elif pos1 not in self.get_players()[pos1[0]].get_known() and pos2 in self.get_players()[pos1[0]].get_known():
                self.get_players()[pos1[0]].add_known(pos1)
                self.get_players()[pos1[0]].remove_known(pos2)
            self.get_game().highlight_card_swap(pos1)
            self.get_game().highlight_card_swap(pos2)
            self.get_game().change_explain("you swaped these cards")
        else: self.get_game().wrong_card()
        self.get_game().disable_cards()
        self.get_game().disable_replace()
        return
    
    
    def current_press(self):
        self.get_game().enable_player_cards()
        self.get_root().wait_variable(self.get_game().btn_var)
        pos = self.get_pos_from_btn_var()
        curr = self.get_current_card()
        if pos == "open":
            self.set_open_card(curr)
            self.set_current_card(None)
            self.get_game().draw_show("   ")
            self.get_game().open_show(curr.get_val()+curr.get_suit())
            if curr.get_val() in ("7","8"):
                self.get_game().change_explain("use look self")
                self.get_game().enable_look_self()
            elif curr.get_val() in ("9","10"):
                self.get_game().change_explain("use look other")
                self.get_game().enable_look_other()
            elif curr.get_val() in ("J","Q"): 
                self.get_game().change_explain("use replace")
                self.get_game().enable_replace()
            elif curr.get_val()=="K" and curr.get_suit in ('♥','♦'):
                self.get_game().change_explain("use all actions")
                self.get_game().enable_look_self()
                self.get_game().enable_look_other()
                self.get_game().enable_replace()
        else:
            self.set_open_card(self.get_player_card(pos))
            self.get_game().open_show(self.get_open_card().get_val()+self.get_open_card().get_suit())
            self.set_player_card(pos,curr)
            self.show_card1(pos)
            self.set_current_card(None)
            self.get_game().draw_show("   ")
        self.get_game().disable_player_cards()
        return
    
    
    def turn(self,num):
        self.get_game().un_highlight()
        if num == 0:
            self.get_game().enable_draw()
            self.get_game().enable_throw()
            self.get_game().enable_win()
        else:
            if self.check_pc_win(num): return
            self.get_game().disable_draw()
            self.get_game().disable_throw()
            self.get_game().disable_win()
            self.pc_try_throw(num)
            card_in_hand = self.get_game_deck().pop()
            if card_in_hand.get_val() in ("7","8"):
                self.set_open_card(card_in_hand)
                self.get_game().open_show(card_in_hand.get_val()+card_in_hand.get_suit())
                self.pc_look_self(num)
                
            elif card_in_hand.get_val() in ("9","10"):
                self.set_open_card(card_in_hand)
                self.get_game().open_show(card_in_hand.get_val()+card_in_hand.get_suit())
                self.pc_look_other(num)
                
            elif card_in_hand.get_val() in ("J","Q"):
                self.set_open_card(card_in_hand)
                self.get_game().open_show(card_in_hand.get_val()+card_in_hand.get_suit())
                self.pc_swap(num)
                
            elif card_in_hand.get_val()=="K" and card_in_hand.get_suit() in ['♥','♦']:
                self.set_open_card(card_in_hand)
                self.get_game().open_show(card_in_hand.get_val()+card_in_hand.get_suit())
                self.pc_red_king(num)
            
            elif card_in_hand.get_worth() < 7:
                self.pc_switch(num,card_in_hand)  
            self.pc_try_throw(num)
        return
    
    def next_turn(self):
        num=self.set_turns((self.get_turns()+0.5)%3)
        if num == self.get_clicked_win():
            self.finish_game()
        if num == int(num):
            self.turn(int(num))
        elif num==0.5:
            self.get_game().change_explain("Its pc player 1 turn")
            self.get_game().disable_actions()
        elif num==1.5: self.get_game().change_explain("Its pc player 2 turn")
        elif num==2.5: self.get_game().change_explain("Its your turn")
    
    
    def pc_look_self(self,num):
        for i in range(4):
            if (num,i) not in self.get_players()[num].get_known():
                self.get_players()[num].add_known((num,i))
                self.get_game().highlight_card_look((num,i))
                self.get_game().change_explain("pc player "+str(num)+" looked at this card")
                return
        rng = random.choice([0,1,2,3])
        self.get_game().highlight_card_look((num,rng))
        self.get_game().change_explain("pc player "+str(num)+" looked at this card")
        return
        
        
    def pc_look_other(self,num):
        for i in numpy.random.permutation([0,3-num]):
            for j in range(4):
                if (i,j) not in self.get_players()[num].get_known():
                    self.get_players()[num].add_known((i,j))
                    self.get_game().highlight_card_look((i,j))
                    self.get_game().change_explain("pc player "+str(num)+" looked at this card")
                    return
        rng1 = random.choice([0,1,2,3])
        rng2 = random.choice([0,3-num])
        self.get_game().highlight_card_look((rng2,rng1))
        self.get_game().change_explain("pc player "+str(num)+" looked at this card")
        return
    
    
    def pc_swap(self,num):
        own_cards = []
        other_cards = []
        for (i,j) in self.get_players()[num].get_known():
            if i==num: own_cards.append((i,j))
            else: other_cards.append((i,j))
        own_worths = [self.get_player_card((i,j)).get_worth() for (i,j) in own_cards if self.get_player_card((i,j)).get_val()!=None]
        other_worths = [self.get_player_card((i,j)).get_worth() for (i,j) in other_cards if self.get_player_card((i,j)).get_val()!=None]
        max_worth = max(own_worths+[-1000])
        min_worth = min(other_worths+[1000])
        if max_worth > min_worth:
            max_pos = own_cards[own_worths.index(max_worth)]
            min_pos = other_cards[other_worths.index(min_worth)]
            temp = self.get_player_card(max_pos)
            self.set_player_card(max_pos,self.get_player_card(min_pos))
            self.set_player_card(min_pos,temp)
            for p in [max_pos,min_pos]:
                card = self.get_player_card(p)
                if card.get_suit() in ['♥','♦']: c = "red"
                else: c= "black"
                if card.get_is_shown(): self.get_game().show_card(p,card.get_val()+card.get_suit(),c)
                else: self.get_game().show_card(p,"   ","black")
            self.get_game().highlight_card_swap(max_pos)
            self.get_game().highlight_card_swap(min_pos)
            self.get_game().change_explain("pc player "+str(num)+" switched those cards")
        else: self.get_game().change_explain("pc player "+str(num)+" didnt switch")
        return
                
        
    def pc_red_king(self,num):
        self.pc_look_self(num)
        self.pc_look_other(num)
        self.pc_swap(num)
        self.get_game().change_explain("pc player "+str(num)+" looked at yellow and swaped red")
        return
    
    
    def pc_switch(self,num,c):
        own_cards=[]
        for (i,j) in self.get_players()[num].get_known():
            if i==num: own_cards.append((i,j))
        own_worths = [self.get_player_card((i,j)).get_worth() for (i,j) in own_cards]
        max_worth = max(own_worths+[-1000])
        if max_worth >= c.get_worth():
            max_pos = own_cards[own_worths.index(max_worth)]
            throw = self.get_player_card(max_pos)
            self.set_open_card(throw)
            self.get_game().open_show(throw.get_val()+throw.get_suit())
            self.set_player_card(max_pos,c)
            self.get_game().highlight_card_swap(max_pos)
            self.get_game().show_card(max_pos,"","black")
            self.get_game().change_explain("pc player "+str(num)+" swaped this card with card from deck")
        else: self.get_game().change_explain("pc player "+str(num)+" threw away card from deck")
        return
    
    
    def pc_try_throw(self,num):
        for pos in self.get_players()[num].get_known():
            if pos[0]==num:
                card = self.get_player_card(pos)
                if card.get_val() == self.get_open_card().get_val():
                    self.set_open_card(card)
                    self.get_game().open_show(card.get_val()+card.get_suit())
                    empty = model.card(None)
                    self.set_player_card(pos,empty)
                    self.get_game().show_card(pos,"None","black")
        return
                    
    def check_pc_win(self,num):    
        for i in range(4):
            if (num,i) not in self.get_players()[num].get_known(): return False
        score = sum([self.get_player_card((num,i)).get_worth() for i in range(4)])
        if score < 3:
            self.set_clicked_win(num)
            self.get_game().change_explain("pc player "+str(num)+" said NEXT TURN")
            return True
        else: return False
            
            
        
    def finish_game(self):
        self.get_game().disable_next()
        for i in range(3):
            for j in range(4):
                card = self.get_player_card((i,j))
                if card.get_suit() in ['♥','♦']: c = "red"
                else: c= "black"
                if card.get_val() != None: self.get_game().show_card((i,j),card.get_val()+card.get_suit(),c)
        sum0 = sum([c.get_worth() for c in self.get_players()[0].get_cards()])
        sum1 = sum([c.get_worth() for c in self.get_players()[1].get_cards()])
        sum2 = sum([c.get_worth() for c in self.get_players()[2].get_cards()])
        new_list = [sum0,sum1,sum2]
        new_list.sort()
        if new_list[0] == sum1: self.get_game().change_explain("pc player 1 won")
        elif new_list[0] == sum2: self.get_game().change_explain("pc player 2 won")
        elif new_list[0] == sum0: self.get_game().change_explain("YOU WON")
        
                
            
                
 #make pc able to declare next turn     
 
    
if __name__ == "__main__" :
    c = controller()
    c.run()
        
    
    