from pydoc import doc
from tkinter import*
from tkinter import messagebox
import os
import sys
from idlelib.tooltip import Hovertip
def close_window():
    window.destroy()
    messagebox.showinfo('Info', 'The app currently runs in the background!\nTo completely kill the app use your task manager.')
  
def Get_MyInputValue():
    source =zero.get()
    img_dest = one.get()
    vid_dest = two.get()
    ss_dest = three.get()
    doc_dest = four.get()
    a = [source, img_dest,vid_dest, ss_dest, doc_dest]
    if os.path.exists(source) and os.path.exists(img_dest) and os.path.exists(vid_dest) and os.path.exists(ss_dest) and os.path.exists(doc_dest) and len(set(a)) ==5:
        return[source,img_dest,vid_dest, ss_dest,doc_dest]
    elif not os.path.exists(source) or not os.path.exists(img_dest) or not os.path.exists(vid_dest) or not os.path.exists(ss_dest) or not os.path.exists(doc_dest):
        messagebox.showerror('Python Error', 'Error: Paths given were not correct!\nPlease run the application again with correct paths')
        sys.exit()
    else:
        messagebox.showerror('Python Error', 'Error: One of the paths given occured multiple times! \nPlease run the application again with correct paths')
        sys.exit()

window =Tk()
window.geometry("420x350")
window.title("Simple Directory Monitor")
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', close_window)
dwnbtn = PhotoImage(file='submitbtn.png')

messagebox.showinfo('Info', 'After entering desired paths and submiting them, please close the application')
zero = StringVar()
one = StringVar()
two = StringVar()
three = StringVar()
four = StringVar()

# checkvar1= IntVar()
# checkvar2 =IntVar()
# checkvar3 = IntVar()
# checkvar4 = IntVar()

# source_dict = {"Source": checkvar1, "Img_dest": checkvar2, "Vid_dest": checkvar3}

Label(window, text="", font=("Arial 7 bold")).pack()
Label(window, text="Directory to monitor" , font=("Arial 15 bold")).pack()
MyEntryBox = Entry(window, textvariable = zero, width=50)
MyEntryBox.pack() 

# c1 = Checkbutton(window, text ="disable", variable = checkvar1, onvalue=1, offvalue=0,  command=choice).pack()
Label(window, text="", font=("Arial 10 bold")).pack()
Label(window, text="Files destinatios" , font=("Arial 15 bold")).pack()
Label(window, text="Destination path for images").pack()
MyEntryBox1 = Entry(window, textvariable = one,width=50)
MyEntryBox1.pack()
# c2 = Checkbutton(window, text ="disable", variable = checkvar2, onvalue=1, offvalue=0, command=choice).pack()

Label(window, text="Destination path for videos").pack()
MyEntryBox2 = Entry(window, textvariable = two, width=50)
MyEntryBox2.pack()
# c3 = Checkbutton(window, text ="disable", variable = checkvar3, onvalue=1, offvalue=0,  command=choice).pack()
Label(window, text="Destination path for screenshots").pack()
MyEntryBox3 = Entry(window, textvariable = three, width=50)
MyEntryBox3.pack()
# c4 = Checkbutton(window, text ="disable", variable = checkvar4, onvalue=1, offvalue=0, command=choice).pack()
Label(window, text="Destination path for text files").pack()
MyEntryBox4 = Entry(window, textvariable = four, width=50)
MyEntryBox4.pack()
# c4 = Checkbutton(window, text ="disable", variable = checkvar4, onvalue=1, offvalue=0, command=choice).pack()


MyEntryBox.insert(0, "C:\\Users\\[WINDOWS USER]\\Downloads")
MyEntryBox1.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures")
MyEntryBox2.insert(0, "C:\\Users\\[WINDOWS USER]\\Videos")
MyEntryBox3.insert(0, "C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots")
MyEntryBox4.insert(0, "C:\\Users\\[WINDOWS USER]\\Documents")

Label(window, text="", font=("Arial 7 bold")).pack()
MyTkButton = Button(window, image=dwnbtn, cursor="hand2", height=25, width=100, command= Get_MyInputValue).pack(pady=3)
myBtn = Button(window,text='?')

myTip = Hovertip(MyEntryBox,'Input format example: \nC:\\Users\\user1\\Downloads')
myTip1 = Hovertip(MyEntryBox1,'Input format example: \nC:\\Users\\user1\\Pictures')
myTip2 = Hovertip(MyEntryBox2,'Input format example: \nC:\\Users\\user1\\Videos')
myTip3 = Hovertip(MyEntryBox3,'Input format example: \nC:\\Users\\user1\\Pictures\\Screenshots')
myTip4 = Hovertip(MyEntryBox4,'Input format example: \nC:\\Users\\user1\\Documents')
mainloop()


