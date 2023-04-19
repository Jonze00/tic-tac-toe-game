import tkinter as tk
from tkinter import messagebox

def display_Label_Frame():
    global head_Label_Frame,body_Label_Frame,footer_Label_Frame
    head_Label_Frame = tk.LabelFrame(main_container, text="score board")
    body_Label_Frame = tk.LabelFrame(main_container, text="board")
    footer_Label_Frame = tk.LabelFrame(main_container, text="restart")

    head_Label_Frame.grid(row=0, column=0, padx=15, pady=10)
    body_Label_Frame.grid(row=1, column=0, padx=15, pady=10)
    footer_Label_Frame.grid(row=2, column=1, padx=15,pady=10)


def display_body_widget():      
        global button1,button2,button3,button4,button5,button6,button7,button8,button9   
        button1 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button1.grid(column=0, row=0)
        button2 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button2.grid(column=1, row=0)
        button3 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button3.grid(column=2, row=0)
        button4 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button4.grid(column=0, row=1)
        button5 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button5.grid(column=1, row=1)
        button6 = tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button6.grid(column=2, row=1)
        button7 =tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button7.grid(column=0, row=2)
        button8 =tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3)
        button8.grid(column=1,row=2)
        button9= tk.Button(body_Label_Frame, text="",font=("arial", 12, "bold"),width=7, height=3) 
        button9.grid(column=2, row=2)


        
#Checking if there is a winner
def winner_check():
    global winner, player1_score, player2_score, player, player2
    #checking if x has won 
    winner = False 
    if button1['text'] =='x' and button2['text']=='x' and button3['text']=='x':
        button1.config(bg='red')
        button2.config(bg='red')
        button3.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score: {player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons()
    elif button4['text'] =='x' and button5['text']=='x' and button6['text']=='x':
            
        button4.config(bg='red')   
        button5.config(bg='red')
        button6.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score:{player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons() 
    elif button7['text'] =='x' and button8['text']=='x' and button9['text']=='x':
        button7.config(bg='red')   
        button8.config(bg='red')
        button9.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score:{player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='x' and button5['text'] == 'x' and button9['text']=='x':
        button1.config(bg='red')   
        button5.config(bg='red')
        button9.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score:{player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons()
    elif button3['text'] =='x' and button5['text']=='x' and button7['text']=='x':
        button3.config(bg='red')   
        button5.config(bg='red')
        button7.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score:{player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons()
    elif button1['text'] =='x' and button ['text']=='x' and button ['text']=='x':    
        button1.config(bg='red')   
        button.config(bg='red')
        button.config(bg='red')
        winner = True
        player1_score += 1
        player.config(text=f'player1 score:{player1_score}')
        messagebox.showinfo('jay Tic Tac Toe Design', 'x won! CONGRATULATION')
        disable_all_buttons()
        
        
        # checking if o has won


def checkingwon():
    pass




def button_click(button):
    global click, count 
    head_Label_Frame.config(text="adasdas")
    if button["text"] == "X":
        click = False 
        count += 1
    elif button["text"] == "" and click == False:
        button["text"] = "0"
        click = False
        count += 1 
    else:
        messagebox.showerinfo("jay Tic Tac Toe", "hey! that box has already been :")



        #check to see if someone won
        checkingwon()
        global winner 
        winner = False     

        






if __name__=="__main__":
    main_container=tk.Tk()

    display_Label_Frame()
    display_body_widget()
    

    main_container.mainloop()