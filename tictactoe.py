from ast import lambda
from tkinter import*
from tkinter import messagebox

root= Tk()
root.title('connect 4- camilla')



# x starts so true
clicked=True
count=0



# checck to see i someone won
def checkifwon():
    global winner
    winner=False
  
def disable_all_buttons():
    b1.config(state=DISABLED)  
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)
    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
       
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
# check o
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
       
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Connect-4", "congrats")
        disable_all_buttons()

# button click function
def b_click(b):
    global clicked, count
   
    if b["text"]==" " and clicked == True:
        b["text"]= "X"
        clicked= False
        count+=1
        checkifwon()
    elif  b["text"]==" " and clicked == False:
        b["text"]= "O"
        clicked= True
        count+=1
        checkifwon()
    else:
        messagebox.showerror("Connect Four", "Another player already claimed that spot /n Choose another spot")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count
    clicked= True
    count= 0

#build buttons
b1=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda:b_click(b1) )
b2=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b2) )
b3=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b3) )
b4=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b4) )
b5=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b5) )
b6=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b6) )
b7=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b7) )
b8=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b8) ) 
b9=Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b9) ) 
b10=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b10) )
b11=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b11) )
b12=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b12) )
b13=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b13) )
b14=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b14) )
b15=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b15) )
b16=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b16) )
b17=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b17) )
b18=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b18) )
b19=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b19) )
b20=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b20) )
b21=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b21) )
b22=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b22) )
b23=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b23) )
b24=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b24) )
b25=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b25) )
b26=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b26) )
b27=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b27) )
b28=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b28) )
b29=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b29) )
b30=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b30) )
b31=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b31) )
b32=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b32) )
b33=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b33) )
b34=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b34) )
b35=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b35) )
b36=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b36) )
b37=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b37) )
b38=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b38) )
b39=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b39) )
b40=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b40) )
b41=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b41) )
b42=Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b42) )

# grid button
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)
b6.grid(row=0, column=5)
b7.grid(row=0, column=6)

b8.grid(row=1, column=0)
b9.grid(row=1, column=1)
b10.grid(row=1, column=2)
b11.grid(row=1, column=3)
b12.grid(row=1, column=4)
b13.grid(row=1, column=5)
b14.grid(row=1, column=6)

b15.grid(row=2, column=0)
b16.grid(row=2, column=1)
b17.grid(row=2, column=2)
b18.grid(row=2, column=3)
b19.grid(row=2, column=4)
b20.grid(row=2, column=5)
b21.grid(row=2, column=6)

b22.grid(row=3, column=0)
b23.grid(row=3, column=1)
b24.grid(row=3, column=2)
b25.grid(row=3, column=3)
b26.grid(row=3, column=4)
b27.grid(row=3, column=5)
b28.grid(row=3, column=6)

b29.grid(row=4, column=0)
b30.grid(row=4, column=1)
b31.grid(row=4, column=2)
b32.grid(row=4, column=3)
b33.grid(row=4, column=4)
b34.grid(row=4, column=5)
b35.grid(row=4, column=6)

b36.grid(row=5, column=0)
b37.grid(row=5, column=1)
b38.grid(row=5, column=2)
b39.grid(row=5, column=3)
b40.grid(row=5, column=4)
b41.grid(row=5, column=5)
b42.grid(row=5, column=6)


# creat menu
my_menu=Menu(root)
root.config(menu=my_menu)

# creats options menu
options_menu= Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="options",menu=options_menu)
options_menu.add_command(label="RestGame", command=reset)

reset()

root.mainloop()

