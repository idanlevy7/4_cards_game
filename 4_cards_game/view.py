# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:20:20 2020

@author: Idan
"""
from tkinter import *
import controller

class GUI:
    def __init__(self,root,controller):
        self.root = root
        self.controller = controller
        self.root.title("4 CARDS GAME")
        self.root.geometry("600x600")
        
        self.btn_var=StringVar()
        M11_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("M11"))
        M12_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("M12"))
        M21_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("M21"))
        M22_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("M22"))
        L11_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("L11"))
        L12_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("L12"))
        L21_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("L21"))
        L22_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("L22"))
        R11_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("R11"))
        R12_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("R12"))
        R21_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("R21"))
        R22_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=lambda: self.btn_var.set("R22"))
        self.the_stack = Label(root,text="   ",relief=RAISED,width=5,height=4,)
        self.the_open_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,command=lambda: self.btn_var.set("open"))
        self.current_card = Button(root,text="   ",relief=GROOVE,width=5,height=4,state=DISABLED,command=self.controller.current_press)
        
        self.player_card_list = [[],[],[]] #first is player pos, second is card num
        self.player_card_list[0].append(M11_card)
        self.player_card_list[0].append(M12_card)
        self.player_card_list[0].append(M21_card)
        self.player_card_list[0].append(M22_card)
        self.player_card_list[1].append(L11_card)
        self.player_card_list[1].append(L12_card)
        self.player_card_list[1].append(L21_card)
        self.player_card_list[1].append(L22_card)
        self.player_card_list[2].append(R11_card)
        self.player_card_list[2].append(R12_card)
        self.player_card_list[2].append(R21_card)
        self.player_card_list[2].append(R22_card)
        
        
        M11_card.grid(row=3,column=2,pady=(0,15))
        M12_card.grid(row=3,column=3,pady=(0,15))
        M21_card.grid(row=4,column=2,pady=(0,15))
        M22_card.grid(row=4,column=3,pady=(0,15))
        L11_card.grid(row=0,column=1,pady=(0,15))
        L12_card.grid(row=1,column=1,pady=(0,15))
        L21_card.grid(row=0,column=0,pady=(0,15))
        L22_card.grid(row=1,column=0,pady=(0,15))
        R11_card.grid(row=1,column=4,pady=(0,15))
        R12_card.grid(row=0,column=4,pady=(0,15))
        R21_card.grid(row=1,column=5,pady=(0,15))
        R22_card.grid(row=0,column=5,pady=(0,15))
        self.the_stack.grid(row=2,column=2,pady=20)
        self.the_open_card.grid(row=2,column=3,pady=20)
        self.current_card.grid(row=3,column=0,rowspan=2,columnspan=2)
        
        self.draw_btn = Button(root,text="draw",command=self.controller.draw,state=DISABLED)
        self.look_self_btn = Button(root,text="look self",command=lambda: self.controller.look(0),state=DISABLED)
        self.look_other_btn = Button(root,text="look other",command=lambda: self.controller.look(1),state=DISABLED)
        self.replace_btn = Button(root,text="replace",command=self.controller.replace,state=DISABLED)
        self.next_btn = Button(root,text="next",command = self.controller.next_turn)
        self.win_btn = Button(root,text="NEXT TURN",state=DISABLED,command=self.controller.win_click)
        self.throw_btn = Button(root,text="throw",command=self.controller.throw_card)
        self.explain = Label(root,text="Its your turn",relief=RIDGE,width=50)
        
        self.draw_btn.grid(row=5,column=0,columnspan=2)
        self.look_self_btn.grid(row=5,column=2,columnspan=2)
        self.look_other_btn.grid(row=6,column=2,columnspan=2)
        self.replace_btn.grid(row=5,column=4,columnspan=2)
        self.next_btn.grid(row=3,column=4,columnspan=2,rowspan=2)
        self.win_btn.grid(row=7,column=0,columnspan=2)
        self.throw_btn.grid(row=6,column=0,columnspan=2)
        self.explain.grid(row=8,column=0,columnspan=6,pady=10)
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_columnconfigure(5, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        
    def draw_show(self,text):
        self.current_card["text"]=text
        self.current_card["state"]=NORMAL
        return
    
    def open_show(self,text):
        self.the_open_card["text"]=text
        return
        
    def enable_cards(self):
        for i in range(3):
            for j in range(4):
                self.player_card_list[i][j]["state"]=NORMAL
        return
        
    def disable_cards(self):
        for i in range(3):
            for j in range(4):
                self.player_card_list[i][j]["state"]=DISABLED
        return
        
    def enable_player_cards(self):
        for j in range(4):
            self.player_card_list[0][j]["state"]=NORMAL
        return
        
    def disable_player_cards(self):
        for j in range(4):
            self.player_card_list[0][j]["state"]=DISABLED
        return
    
    def enable_draw(self):
        self.draw_btn["state"]=NORMAL
    def disable_draw(self):
        self.draw_btn["state"]=DISABLED
    def enable_win(self):
        self.win_btn["state"]=NORMAL
    def disable_win(self):
        self.win_btn["state"]=DISABLED
    def enable_look_self(self):
        self.look_self_btn["state"]=NORMAL
    def disable_look_self(self):
        self.look_self_btn["state"]=DISABLED
    def enable_look_other(self):
        self.look_other_btn["state"]=NORMAL
    def disable_look_other(self):
        self.look_other_btn["state"]=DISABLED
    def enable_replace(self):
        self.replace_btn["state"]=NORMAL
    def disable_replace(self):
        self.replace_btn["state"]=DISABLED
    def disable_next(self):
        self.next_btn["state"]=DISABLED
    def enable_throw(self):
        self.throw_btn["state"]=NORMAL
    def disable_throw(self):
        self.throw_btn["state"]=DISABLED
        
        
    def disable_actions(self):
        self.disable_draw()
        self.disable_win()
        self.disable_look_self()
        self.disable_look_other()
        self.disable_replace()
        self.disable_throw()
        return
        

        
    
    def show_card(self,card_pos,text1,color): #gets touple of pos and text to write
        self.player_card_list[card_pos[0]][card_pos[1]]["text"]=text1
        self.player_card_list[card_pos[0]][card_pos[1]]["fg"]=color
        self.player_card_list[card_pos[0]][card_pos[1]]["disabledforeground"]=color
        return
    
    def wrong_card(self):
        messagebox.showerror("error","you picked an invalid card")
        return
    
    def change_explain(self,text):
        self.explain["text"]=text
        return
    
    def highlight_card_look(self,pos):
        self.player_card_list[pos[0]][pos[1]]["bg"]="#FFFA55"
        return
    
    def highlight_card_swap(self,pos):
        self.player_card_list[pos[0]][pos[1]]["bg"]="#D84D4D"
        return
        
    def un_highlight(self):
        for i in range(3):
            for j in range(4):
                self.player_card_list[i][j]["bg"]="SystemButtonFace"
        return
    
        