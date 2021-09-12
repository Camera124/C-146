from tkinter import *
from tkmacosx import *
root=Tk()
root.title("ASCII VALUE")
root.geometry("300x400")

root.configure(background = 'aqua')

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor=CENTER)

def asciicov():
    value = enter_word.get()
    for letter in value:
        label["text"] += str(ord(letter)) + "  "
        
     
        
button = Button(root, text = 'Display Ascii and Encrypted Value', bg = "red", fg = 'black', command=asciicov)
        
label = Label(root, text = 'Name In Ascii: ', bg = 'orange', fg = 'black')

label2 = Label(root, text = 'Encrypted Name: ', bg = 'yellow', fg = 'black')

button.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label.place(relx = 0.5, rely = 0.6  , anchor=CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor=CENTER)

root.mainloop()