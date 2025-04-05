from tkinter import*

from time import strftime #formatting the time in hours,minutes,second.

root=Tk()
root.title('DIGITAL CLOCK')

def time():
    monu=strftime("Year=""%Y\n"
                 "Date=""%D\n""Time=""%H:%M:%S %p")#the order of how time should be formatted
    label.config(text=monu)#config() combines the time to label.
    
   
label=Label(root,font=("ds-digital",80),background="pink",foreground="black")#passing root is compulsive.
label.pack(anchor="center")#pack()combines all elements passed to the label component and anchor is used to place contents in center.
time()

mainloop()
