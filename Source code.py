import tkinter as tk
root = tk.Tk()
#Display
root.title("Calculator")
root.geometry("300x400")
root.configure(bg = "black")
entry = tk.Entry(root,width=20,font=("Helvetica", 20, "bold"),bg = "black", fg = "white")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=20)

#function for press
def press(num):
    entry.insert(tk.END,num)

#function for equal
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
    except ZeroDivisionError:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Can't Divide By 0!")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END,"error")

#function for clear
def clear():
    entry.delete(0,tk.END)



#Number Buttons
b1 = tk.Button(root,text="1", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("1"))
b2 = tk.Button(root,text="2", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("2"))
b3 = tk.Button(root,text="3", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("3"))
b4 = tk.Button(root,text="4", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("4"))
b5 = tk.Button(root,text="5", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("5"))
b6 = tk.Button(root,text="6", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("6"))
b7 = tk.Button(root,text="7", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("7"))
b8 = tk.Button(root,text="8", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("8"))
b9 = tk.Button(root,text="9", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("9"))
b0 = tk.Button(root,text="0", width = 5, height= 2,bg="yellow",fg="black",command=lambda:press("0"))
b_add = tk.Button(root, text = "+",width=5,height=2,bg="teal",fg="black",command=lambda:press("+"))
b_sub = tk.Button(root, text = "-",width=5,height=2,bg="teal",fg="black",command=lambda:press("-"))
b_mul = tk.Button(root, text = "*",width=5,height=2,bg="teal",fg="black",command=lambda:press("*"))
b_div = tk.Button(root, text = "/",width=5,height=2,bg="teal",fg="black",command=lambda:press("/"))

#Button for =
b_equal = tk.Button(root, text="=",width=5,height=2, bg="teal",fg="black",command=equal)

#Button for Clear all
b_clear = tk.Button(root, text="C",width=5,height=2, bg= "skyblue",fg = "black",command=clear)

#Row 1
b7.grid(row=1,column=0,padx=5,pady=5)
b8.grid(row=1,column=1,padx=5,pady=5)
b9.grid(row=1,column=2,padx=5,pady=5)
b_div.grid(row=1,column=3,padx=5,pady=5)

#Row 2
b4.grid(row=2,column=0,padx=5,pady=5)
b5.grid(row=2,column=1,padx=5,pady=5)
b6.grid(row=2,column=2,padx=5,pady=5)
b_mul.grid(row=2,column=3,padx=5,pady=5)

#Row 3
b1.grid(row=3,column=0,padx=5,pady=5)
b2.grid(row=3,column=1,padx=5,pady=5)
b3.grid(row=3,column=2,padx=5,pady=5)
b_sub.grid(row=3,column=3,padx=5,pady=5)

#Row 4
b_clear.grid(row=4,column=0,padx=5,pady=5)
b0.grid(row=4,column=1,padx=5,pady=5)
b_equal.grid(row=4,column=2,padx=5,pady=5)
b_add.grid(row=4,column=3,padx=5,pady=5)

#Run 
root.mainloop()
