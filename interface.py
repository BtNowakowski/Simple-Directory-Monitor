from tkinter import*
from tkinter import messagebox
import os
import sys

def Get_MyInputValue():
    source =zero.get()
    img_dest = one.get()
    vid_dest = two.get()
    
    if os.path.exists(source) and os.path.exists(img_dest) and os.path.exists(vid_dest) and source != img_dest and source != vid_dest and img_dest != vid_dest:
        return [source,img_dest,vid_dest]
    elif not os.path.exists(source) or not os.path.exists(img_dest) or not os.path.exists(vid_dest):
        messagebox.showerror('Python Error', 'Error: Paths given were not correct!\nPlease run the application again with correct paths')
        sys.exit()
    else:
        messagebox.showerror('Python Error', 'Error: One of the paths given occured multiple times! \nPlease run the application again with correct paths')
        sys.exit()

def close_window():
    window.destroy()
    messagebox.showinfo('Info', 'The app will continue to run in background. \nTo completely kill the app use your task manager.')

window =Tk()
window.geometry("400x350")
window.title("Simple Directory Monitor")
window.resizable(False, False)


zero = StringVar()
one = StringVar()
two = StringVar()

Label(window, text="Please enter full paths of the directories", font=("Arial 10 bold")).pack()
Label(window, text="", font=("Arial 10 bold")).pack()
Label(window, text="Directory to monitor").pack()
MyEntryBox = Entry(window, textvariable = zero, width=20)
MyEntryBox.pack()
Label(window, text="Destination path for images").pack()
MyEntryBox1 = Entry(window, textvariable = one,width=20)
MyEntryBox1.pack()
Label(window, text="Destination path for videos").pack()
MyEntryBox2 = Entry(window, textvariable = two, width=20)
MyEntryBox2.pack()

MyEntryBox.insert(0, "C:\\Users\\[USERNAME]\\Downloads")
MyEntryBox1.insert(0, "C:\\Users\\[USERNAME]\\Pictures")
MyEntryBox2.insert(0, "C:\\Users\\[USERNAME]\\Videos")
#command will call the defined function
MyTkButton = Button(window, height=1, width=10, text="Submit", command= Get_MyInputValue)
MyTkButton.pack()
Label(window, text="", font=("Arial 7 bold")).pack()
Label(window, text="Input format example: ", font=("Arial 7 bold")).pack()
Label(window, text="C:\\Users\\user1\\Downloads", font=("Arial 7 bold")).pack()

Label(window, text="", font=("Arial 7 bold")).pack()
Label(window, text="After passing the values, please close the window", font=("Arial 10 bold")).pack()

# Label(window, text="The app will continue to run in background", font=("Arial 7 bold")).pack()
button = Button(window, text = 'Close the window', command = close_window).pack()

# Label(window, text="To completely kill the app use your task manager", font=("Arial 7 bold")).pack()

mainloop()