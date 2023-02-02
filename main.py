from tkinter import *
from tkinter import messagebox
import os
from idlelib.tooltip import Hovertip
from Watcher import Watcher

EXAMPLE_DEST = {"monitored_directory":"C:\\Users\\[WINDOWS USER]\\Downloads", 
                "images_directory":"C:\\Users\\[WINDOWS USER]\\Pictures", 
                "videos_directory":"C:\\Users\\[WINDOWS USER]\\Videos",
                "screenshots_directory":"C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots",
                "documents_directory":"C:\\Users\\[WINDOWS USER]\\Documents"}

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

    if validity == True and len(set(act_paths)) == len(act_paths):
        w = Watcher(paths, window)
        w.run()
    elif validity == False:
        messagebox.showerror('Python Error', 'Error: One or more of the paths given were not correct! \nPlease run the application again with correct paths')
    elif len(set(act_paths)) != len(act_paths):
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


frame = Frame(window)
frame.pack(pady = 10, padx = 10)
Label(frame, text="Directory to monitor" , font=("Arial 15 bold")).grid(row = 0, column = 0, columnspan=2)

MyEntryBox = Entry(frame,textvariable = source, width=50)
MyEntryBox.grid(row = 1, column = 0, padx = 5, pady = 5)
Button(frame,text="X", cursor="hand2", command=lambda: disable_entry(MyEntryBox)).grid(row = 1, column = 1, padx = 5, pady = 5)


frame1 = Frame(window)
frame1.pack(pady = 10, padx = 10)

Label(frame1, text="Files destinations" , font=("Arial 15 bold")).grid(row = 0, column = 0, columnspan=2)

Label(frame1, text="Destination path for images").grid(row = 1, column = 0, columnspan=2)

MyEntryBox1 = Entry(frame1, textvariable = images_dest,width=50)
MyEntryBox1.grid(row = 2, column = 0, padx = 5, pady = 5)
Button(frame1,text="X", command=lambda: disable_entry(MyEntryBox1)).grid(row = 2, column = 1, padx = 5, pady = 5)


Label(frame1, text="Destination path for videos").grid(row = 3, column = 0, columnspan=2)

MyEntryBox2 = Entry(frame1, textvariable = videos_dest, width=50)
MyEntryBox2.grid(row = 4, column = 0, padx = 5, pady = 5)
Button(frame1,text="X", command=lambda: disable_entry(MyEntryBox2)).grid(row = 4, column = 1, padx = 5, pady = 5)

Label(frame1, text="Destination path for screenshots").grid(row = 5, column = 0, columnspan=2)

MyEntryBox3 = Entry(frame1, textvariable = screenshots_dest, width=50)
MyEntryBox3.grid(row = 6, column = 0, padx = 5, pady = 5)
Button(frame1,text="X", command=lambda: disable_entry(MyEntryBox3)).grid(row = 6, column = 1, padx = 5, pady = 5)

Label(frame1, text="Destination path for screenshots").grid(row = 7, column = 0, columnspan=2)

MyEntryBox4 = Entry(frame1, textvariable = documents_dest, width=50)
MyEntryBox4.grid(row = 8, column = 0, padx = 5, pady = 5)
Button(frame1,text="X", command=lambda: disable_entry(MyEntryBox4)).grid(row = 8, column = 1, padx = 5, pady = 5)


MyEntryBox.insert(0, EXAMPLE_DEST["monitored_directory"])
MyEntryBox1.insert(0, EXAMPLE_DEST["images_directory"])
MyEntryBox2.insert(0, EXAMPLE_DEST["videos_directory"])
MyEntryBox3.insert(0, EXAMPLE_DEST["screenshots_directory"])
MyEntryBox4.insert(0, EXAMPLE_DEST["documents_directory"])


Label(window, text="", font=("Arial 7 bold")).pack()
MyTkButton = Button(window, image=dwnbtn, cursor="hand2", height=25, width=100, command=check_for_validity).pack(pady=3)

Hovertip(MyEntryBox,'FORMAT EXAMPLE:  C:\\Users\\user1\\Downloads', hover_delay=250)
Hovertip(MyEntryBox1,'FORMAT EXAMPLE:  C:\\Users\\user1\\Pictures', hover_delay=250)
Hovertip(MyEntryBox2,'FORMAT EXAMPLE:  C:\\Users\\user1\\Videos', hover_delay=250)
Hovertip(MyEntryBox3,'FORMAT EXAMPLE:  C:\\Users\\user1\\Pictures\\Screenshots', hover_delay=250)
Hovertip(MyEntryBox4,'FORMAT EXAMPLE:  C:\\Users\\user1\\Documents', hover_delay=250)

mainloop()