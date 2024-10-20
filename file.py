#Mini Project 2.

#Rendum Number game

""" create a mini projet for gues any number """

import tkinter as tk
import random
root=tk.Tk()
root.title("random number game")
root.config(bg="dark orange")
def rand(n,num,label):
    if num<n:
        label.config(font='arial 30 ',text='gess is low')
    elif num>n:
        label.config(font='arial 30 ',text='gess is height')
    else:
        label.config(font='arial 30 ',text='you gessed number')
def rules():
    label.config(font='arial 30 ',text="""this programm is generate a
                 random number """)
label=tk.Label(root,fg="indigo",bg="dark orange")
label.grid(row=0,column=0,pady=20,columnspan=4)
n=random.randint(1,9)
#print(n)
num3=4
num4=1
for num1 in range(1,4):
    for num2 in range(1,4):
        tk.Button(root,text=str(num1),font="arial 15",width=10,height=2,
                  command=lambda:rand(n,num4,label)).grid(row=num3,column=num2)
        num4+=1
    num3+=1
    

tk.Button(root,text='1',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,1,label)).grid(row=4,column=1)

tk.Button(root,text='2',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,2,label)).grid(row=4,column=2)    
    
tk.Button(root,text='3',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,3,label)).grid(row=4,column=3)        

tk.Button(root,text='4',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,4,label)).grid(row=5,column=1)

tk.Button(root,text='5',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,5,label)).grid(row=5,column=2)


tk.Button(root,text='6',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,6,label)).grid(row=5,column=3)


tk.Button(root,text='7',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,7,label)).grid(row=6,column=1)

tk.Button(root,text='8',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,8,label)).grid(row=6,column=2)

tk.Button(root,text='9',font='arial 25 bold',bg="maroon",fg="white",
          width=6,height=1,border=8,command=lambda: rand (n,9,label)).grid(row=6,column=3)


tk.Button(root,text="Exit",font='arial 25 bold',bg="red",fg="black",width=6,height=1,border=8,
          command=root.destroy).grid(row=7,column=0,columnspan=3)


tk.Button(root,text="Rules",font='arial 25 bold',bg="green",fg="black",width=6,height=1,border=8,
          command=lambda:rules()).grid(row=7,column=2,columnspan=3)



        
