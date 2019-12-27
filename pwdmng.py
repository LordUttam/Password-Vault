from string import ascii_letters as chars
from tkinter import *
from tkinter.ttk import *
import random, pyperclip

chars+='1234567890!@#$%^&*()_-=+*//,< >.?;:"[]{}\\|`~'

def generate():
    minChars=int(entry.get())
    numChars=random.randrange(minChars,minChars+6)
    password=''
    entry2.delete(0,password)
    for i in range(numChars-3):
        password+=random.choice(chars)
    password+=random.choice('1234567890')#ensuring there is at least a number buy adding a number.
    password+=random.choice('!@#$%^&*()_-=+*/,<>.?;:"[]{}\\|`~')#adding a sp character
    password+=random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')#adding an upper case
    password=list(password)
    random.shuffle(password)
    password=''.join(password)
    entry2.insert(0,password)

def copypwd():
    pwd=entry2.get()
    pyperclip.copy(pwd)

#GUI
#Window
root = Tk()
root.title("Uttam's Password Generator")

#Inside Window

#label for length of pwd
minlength=Label(root, text="Min. length")
minlength.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

#password label and space where generated pwd will be displayed
pwd = Label(root, text="Password: ")
pwd.grid(row=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

#Copy Button
copyButton = Button(root, text = "Copy", command = copypwd)
copyButton.grid(row=1,column=3)
#Generate Button
generateButton = Button(root, text="Generate", command=generate) 
generateButton.grid(row=0, column=3)

#running the GUI
root.mainloop()
