from tkinter import*
from tkinter import messagebox
import os
from idlelib.tooltip import Hovertip
from Watcher import Watcher

def get_inputs():
    return [source.get(), images_dest.get(),videos_dest.get(), screenshots_dest.get(), documents_dest.get()]

def check_paths():
    paths = get_inputs()
    path_validity = 1
    for path in paths:
        if os.path.exists(path):
            path_validity *= 1  
        else:
            path_validity *=0
    return bool(path_validity)

def check_for_validity():
    validity = check_paths()
    paths = get_inputs()
    if validity == True and len(set(paths)) ==5:
        w = Watcher(paths, window)
        w.run()
    elif validity == False:
        messagebox.showerror('Python Error', 'Error: Paths given were not correct!\nPlease run the application again with correct paths')
    elif len(set(paths)) !=5:
        messagebox.showerror('Python Error', 'Error: One of the paths given occured multiple times! \nPlease run the application again with correct paths')
    else:
        messagebox.showerror('Python Error', 'Error: Unexpected error occured. \nPlease run the application again') 

window =Tk()
window.geometry("420x350")
window.title("Simple Directory Monitor")
window.resizable(False, False)
dwnbtn = PhotoImage(file='submitbtn.png')

source = StringVar()
images_dest = StringVar()
videos_dest = StringVar()
screenshots_dest = StringVar()
documents_dest = StringVar()

Label(window, text="", font=("Arial 7 bold")).pack()
Label(window, text="Directory to monitor" , font=("Arial 15 bold")).pack()
MyEntryBox = Entry(window, textvariable = source, width=50)
MyEntryBox.pack() 

Label(window, text="", font=("Arial 10 bold")).pack()
Label(window, text="Files destinatios" , font=("Arial 15 bold")).pack()
Label(window, text="Destination path for images").pack()
MyEntryBox1 = Entry(window, textvariable = images_dest,width=50)
MyEntryBox1.pack()

Label(window, text="Destination path for videos").pack()
MyEntryBox2 = Entry(window, textvariable = videos_dest, width=50)
MyEntryBox2.pack()

Label(window, text="Destination path for screenshots").pack()
MyEntryBox3 = Entry(window, textvariable = screenshots_dest, width=50)
MyEntryBox3.pack()

Label(window, text="Destination path for text files").pack()
MyEntryBox4 = Entry(window, textvariable = documents_dest, width=50)
MyEntryBox4.pack()

MyEntryBox.insert(0, "C:\\Users\\[WINDOWS USER]\\Downloads")
MyEntryBox1.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures")
MyEntryBox2.insert(0, "C:\\Users\\[WINDOWS USER]\\Videos")
MyEntryBox3.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots")
MyEntryBox4.insert(0, "C:\\Users\\[WINDOWS USER]\\Documents")

Label(window, text="", font=("Arial 7 bold")).pack()
MyTkButton = Button(window, image=dwnbtn, cursor="hand2", height=25, width=100, command=check_for_validity).pack(pady=3)

myTip = Hovertip(MyEntryBox,'Input format example: \nC:\\Users\\user1\\Downloads')
myTip1 = Hovertip(MyEntryBox1,'Input format example: \nC:\\Users\\user1\\Pictures')
myTip2 = Hovertip(MyEntryBox2,'Input format example: \nC:\\Users\\user1\\Videos')
myTip3 = Hovertip(MyEntryBox3,'Input format example: \nC:\\Users\\user1\\Pictures\\Screenshots')
myTip4 = Hovertip(MyEntryBox4,'Input format example: \nC:\\Users\\user1\\Documents')

mainloop()