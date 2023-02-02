from tkinter import *
from tkinter import messagebox
import os
from idlelib.tooltip import Hovertip
from Watcher import Watcher

EXAMPLE_DEST = {"monitored_directory":"C:\\Users\\[WINDOWS USER]\\Downloads", "images_directory":"C:\\Users\\[WINDOWS USER]\\Pictures", "videos_directory":"C:\\Users\\[WINDOWS USER]\\Videos", "screenshots_directory":"C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots",  "documents_directory":"C:\\Users\\[WINDOWS USER]\\Documents"}

def get_inputs():
    src, img, vid, ss, doc = False, False, False, False, False

    if str(MyEntryBox['state']) == "normal": 
        src=source.get() 
    if str(MyEntryBox1['state']) == "normal": 
        img=images_dest.get()
    if str(MyEntryBox2['state']) == "normal": 
        vid=videos_dest.get()
    if str(MyEntryBox3['state']) == "normal": 
        ss=screenshots_dest.get()
    if str(MyEntryBox4['state']) == "normal": 
        doc=documents_dest.get()

    return [src, img, vid, ss, doc]

def disable_entry(item):
    state = str(item['state'])
    if state != "disabled":       
        item.delete(0, END)
        item.config(state= "disabled")
    else:
        item.config(state= "normal")
        if item.winfo_name()[-1:].isnumeric():
            item.insert(0, list(EXAMPLE_DEST.values())[int(item.winfo_name()[-1:])-1])
        else:
            item.insert(0, "C:\\Users\\[WINDOWS USER]\\Downloads")

def check_paths():
    paths = get_inputs()
    path_validity = 1
    for path in paths:
        if path != False:
            if os.path.exists(path):
                path_validity *= 1  
            else:
                path_validity *=0
    return bool(path_validity)

def check_for_validity():
    validity = check_paths()
    paths = get_inputs()
    act_paths = [path for path in paths if path != False]

    if validity == True and len(set(paths)) != len(act_paths):
        w = Watcher(paths, window)
        w.run()
    elif validity == False:
        messagebox.showerror('Python Error', 'Error: Paths given were not correct! \nPlease run the application again with correct paths')
    elif len(set(paths)) != len(act_paths):
        messagebox.showerror('Python Error', 'Error: One of the paths given occured multiple times! \nPlease run the application again with correct paths')
    else:
        messagebox.showerror('Python Error', 'Error: Unexpected error occured. \nPlease run the application again') 

window =Tk()
window.geometry("420x480")
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
MyEntryBox = Entry(window,textvariable = source, width=50)
MyEntryBox.pack() 
Button(window,text="X", cursor="hand2", command=lambda: disable_entry(MyEntryBox)).pack()

Label(window, text="", font=("Arial 10 bold")).pack()
Label(window, text="Files destinatios" , font=("Arial 15 bold")).pack()
Label(window, text="Destination path for images").pack()
MyEntryBox1 = Entry(window, textvariable = images_dest,width=50)
MyEntryBox1.pack()
Button(window,text="X", command=lambda: disable_entry(MyEntryBox1)).pack()

Label(window, text="Destination path for videos").pack()
MyEntryBox2 = Entry(window, textvariable = videos_dest, width=50)
MyEntryBox2.pack()
Button(window,text="X", command=lambda: disable_entry(MyEntryBox2)).pack()


Label(window, text="Destination path for screenshots").pack()
MyEntryBox3 = Entry(window, textvariable = screenshots_dest, width=50)
MyEntryBox3.pack()
Button(window,text="X", command=lambda: disable_entry(MyEntryBox3)).pack()



Label(window, text="Destination path for text files").pack()
MyEntryBox4 = Entry(window, textvariable = documents_dest, width=50)
MyEntryBox4.pack()
Button(window,text="X", cursor="hand2", command=lambda: disable_entry(MyEntryBox4)).pack()

MyEntryBox.insert(0, "C:\\Users\\[WINDOWS USER]\\Downloads")
MyEntryBox1.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures")
MyEntryBox2.insert(0, "C:\\Users\\[WINDOWS USER]\\Videos")
MyEntryBox3.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots")
MyEntryBox4.insert(0, "C:\\Users\\[WINDOWS USER]\\Documents")


Label(window, text="", font=("Arial 7 bold")).pack()
MyTkButton = Button(window, image=dwnbtn, cursor="hand2", height=25, width=100, command=check_for_validity).pack(pady=3)

Hovertip(MyEntryBox,'FORMAT EXAMPLE:  C:\\Users\\user1\\Downloads', hover_delay=250)
Hovertip(MyEntryBox1,'FORMAT EXAMPLE:  C:\\Users\\user1\\Pictures', hover_delay=250)
Hovertip(MyEntryBox2,'FORMAT EXAMPLE:  C:\\Users\\user1\\Videos', hover_delay=250)
Hovertip(MyEntryBox3,'FORMAT EXAMPLE:  C:\\Users\\user1\\Pictures\\Screenshots', hover_delay=250)
Hovertip(MyEntryBox4,'FORMAT EXAMPLE:  C:\\Users\\user1\\Documents', hover_delay=250)

mainloop()