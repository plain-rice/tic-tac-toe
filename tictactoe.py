#tic tac toe game

import os
import random
import time

board=["$"," ", " ", " ", " ", " ", " ", " ", " ", " "]
slottaken=[" "," ", " ", " ", " ", " ", " ", " ", " ", " "]


print("""
████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗  ██╗
╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝  ██║
░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░  ██║
░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░  ╚═╝
░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗  ██╗
░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝  ╚═╝""")
      





#for printing the board
def print_board():
    print(board[1] +  " | "  + board[2] + "| " + board[3])
    print("--|--|--")
    print(board[4] +  " | "  + board[5] + "| " + board[6])
    print("--|--|--")
    print(board[7] +  " | "  + board[8] + "| " + board[9])

print_board()
chance=True
count =0
#for AI's turn
def compmove():
    compchoice=3
    if board[5]==" ":
        compchoice=5

    else:
        for i in (1,2,3):
            
            if board[i]=="X" and board[i+3]=="X" and board[i+6]==" ":
                compchoice=i+6
            
            elif board[i]==" " and board[i+3]=="X" and board[i+6]=="X":
                compchoice=i
                
            elif board[i]=="X" and board[i+3]==" " and board[i+6]=="X":
                compchoice=i+3

            else:
                for i in (1,4,7):
                    if board[i]=="X" and board[i+1]=="X" and board[i+2]==" ":
                        compchoice=i+2
                    elif board[i]==" " and board[i+1]=="X" and board[i+2]=="X":
                        compchoice=i
                
                    elif board[i]==" " and board[i+1]==" " and board[i+2]=="X":
                        compchoice=i+1
                    else:
                       if board[1]=="X" and board[5]=="X" and board[9]==" ":
                           compchoice==9
                       elif board[1]==" " and board[5]=="X" and board[9]=="X":
                           compchoice==1
                       elif board[1]=="X" and board[5]==" " and board[9]=="X":
                           compchoice==5

                       else:
                           if board[3]=="X" and board[5]=="X" and board[7]==" ":
                               compchoice==7
                           elif board[3]==" " and board[5]=="X" and board[7]=="X":
                               compchoice==3
                           elif board[3]=="X" and board[5]==" " and board[7]=="X":
                               compchoice==5
                           else: 

                                        while compchoice in slottaken:
                                                compchoice=random.randint(1,9)
                                        compchoice=int(compchoice)

    board[compchoice]= "0"
    slottaken[compchoice]=compchoice
    print(" Hmmmmm.... Let me think ...")
    time.sleep(2)
    print_board()
    global chance
    chance=True                                               
                                          

  
#for my turn    
def mymove():
    while True:
        choice=input("Where do you want to place your X ?")
        choice=int(choice)
    
        if board[choice]==" " :
            board[choice]= "X"
            break
        else:
            print("Please select an empty space")
        
            continue
    print_board()    
    slottaken[choice]=choice
    global chance
    chance= False

#check if tie
def isFull():
     if " " in board:
        isFull==False
     else:
            isFull==True
            print("The game is a tie!")
            
    
while True:
    
    if chance==True:
       mymove()   
    else:
       compmove()
    

    #check if I won
    if(board[1]=="X" and board[2]=="X" and board[3]=="X") or \
        (board[4]=="X" and board[5]=="X" and board[6]=="X") or \
        (board[1]=="X" and board[4]=="X" and board[7]=="X") or \
        (board[2]=="X" and board[5]=="X" and board[8]=="X") or \
        (board[3]=="X" and board[6]=="X" and board[9]=="X") or \
        (board[7]=="X" and board[8]=="X" and board[9]=="X" )or \
        (board[1]=="X" and board[5]=="X" and board[9]=="X" )or \
        (board[3]=="X" and board[5]=="X" and board[7]=="X"):
         
         print(" X wins !")
         break
         
    #check if computer won
    if (board[1]=="0" and board[2]=="0" and board[3]=="0") or \
        (board[4]=="0" and board[5]=="0" and board[6]=="0") or \
        (board[1]=="0" and board[4]=="0" and board[7]=="0") or \
        (board[2]=="0" and board[5]=="0" and board[8]=="0" )or \
        (board[3]=="0" and board[6]=="0" and board[9]=="0") or \
        (board[7]=="0" and board[8]=="0" and board[9]=="0") or \
        (board[1]=="0" and board[5]=="0" and board[9]=="0") or \
        (board[3]=="0" and board[5]=="0" and board[7]=="0"):
         print_board()
         print(" 0 wins !")
         break
                 
   
        
    isFull()        
    continue
