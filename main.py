from tkinter import *
from tkinter import messagebox
import os
from tkinter import font
from tkinter.filedialog import askdirectory
from idlelib.tooltip import Hovertip
from Watcher import Watcher


# EXAMPLE_DEST = {"monitored_directory": "C:\\Users\\[WINDOWS USER]\\Downloads",
#                 "images_directory": "C:\\Users\\[WINDOWS USER]\\Pictures",
#                 "videos_directory": "C:\\Users\\[WINDOWS USER]\\Videos",
#                 "screenshots_directory": "C:\\Users\\[WINDOWS USER]\\Pictures\\Screenshots",
#                 "documents_directory": "C:\\Users\\[WINDOWS USER]\\Documents"}


def select_directory(widget):
    widget.delete(0, END)
    widget.insert(0, str(askdirectory(title='Select Folder')))


def get_inputs():
    src, img, vid, ss, doc = False, False, False, False, False

    if str(source_directory['state']) == "normal":
        src = source.get()
    if str(images_destination['state']) == "normal":
        img = images_dest.get()
    if str(videos_destination['state']) == "normal":
        vid = videos_dest.get()
    if str(screenshots_destination['state']) == "normal":
        ss = screenshots_dest.get()
    if str(documents_destination['state']) == "normal":
        doc = documents_dest.get()

    return [src, img, vid, ss, doc]


def disable_entry(item):
    state = str(item['state'])
    if state != "disabled":
        item.delete(0, END)
        item.config(state="disabled")
    else:
        item.config(state="normal")
        item.insert(0, "C:\\Users\\[WINDOWS USER]\\Directory")


def check_paths():
    paths = get_inputs()
    path_validity = 1
    for path in paths:
        if path != False:
            if os.path.exists(path):
                path_validity *= 1
            else:
                path_validity *= 0
    return bool(path_validity)


def check_for_validity():
    validity = check_paths()
    paths = get_inputs()
    act_paths = [path for path in paths if path != False]

    if len(act_paths) <= 1:
        messagebox.showerror(
            'Python Error', 'Error: Not enough paths selected \nPlease select valid number of paths')
    elif validity == True and len(set(act_paths)) == len(act_paths):
        w = Watcher(paths, window)
        w.run()
    elif validity == False:
        messagebox.showerror(
            'Python Error', 'Error: One or more of the paths given were not correct! \nPlease run the application again with correct paths')
    elif len(set(act_paths)) != len(act_paths):
        messagebox.showerror(
            'Python Error', 'Error: One of the paths given occured multiple times! \nPlease run the application again with correct paths')
    else:
        messagebox.showerror(
            'Python Error', 'Error: Unexpected error occured. \nPlease run the application again')


window = Tk()
window.geometry("620x480")
window.title("Simple Directory Monitor")
window.resizable(False, False)
defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Calibri", size=14)

source = StringVar()
images_dest = StringVar()
videos_dest = StringVar()
screenshots_dest = StringVar()
documents_dest = StringVar()


frame = Frame(window, highlightcolor="white")
frame.pack(pady=10, padx=15)
Label(frame, text="Directory to monitor", font=(
    "Calibri 17")).grid(row=0, column=0, pady=5, columnspan=4, sticky=W+E+N+S)

source_directory = Entry(frame, textvariable=source, width=50, font=("Calibri", 12))
source_directory.grid(row=1, column=1, padx=5, pady=5, ipady=3)
Button(frame, text="...", height=1, width=2, cursor="hand2", command=lambda: select_directory(
    source_directory)).grid(row=1, column=3, padx=5, pady=5)

frame1 = Frame(window)
frame1.pack(pady=10, padx=10)

Label(frame1, text="Files destinations", font=(
    "Calibri 17")).grid(row=1, column=0, pady=5, columnspan=4, sticky=W+E+N+S)

Label(frame1, text="Images: ").grid(
    row=2, pady=5, column=0, columnspan=1, sticky=W)

images_destination = Entry(frame1, textvariable=images_dest,
                    width=50, font=("Calibri", 12))
images_destination.grid(row=2, column=1, padx=5, pady=5, ipady=3)
Button(frame1, text="X", height=1, width=2, cursor="hand2", command=lambda: disable_entry(
    images_destination)).grid(row=2, column=2, padx=5, pady=5)
Button(frame1, text="...", height=1, width=2, cursor="hand2", command=lambda: select_directory(
    images_destination)).grid(row=2, column=3, padx=5, pady=5)


Label(frame1, text="Videos: ").grid(
    row=4, pady=5, column=0, columnspan=1, sticky=W)

videos_destination = Entry(frame1, textvariable=videos_dest,
                    width=50, font=("Calibri", 12))
videos_destination.grid(row=4, column=1, padx=5, pady=5, ipady=3)
Button(frame1, text="X", height=1, width=2, cursor="hand2",  command=lambda: disable_entry(
    videos_destination)).grid(row=4, column=2, padx=5, pady=5)
Button(frame1, text="...", height=1, width=2, cursor="hand2",  command=lambda: select_directory(
    videos_destination)).grid(row=4, column=3, padx=5, pady=5)

Label(frame1, text="Screenshots: ").grid(
    row=6, column=0, pady=5, columnspan=1, sticky=W)

screenshots_destination = Entry(frame1, textvariable=screenshots_dest,
                    width=50, font=("Calibri", 12))
screenshots_destination.grid(row=6, column=1, padx=5, pady=5, ipady=3)
Button(frame1, text="X", height=1, width=2, cursor="hand2",  command=lambda: disable_entry(
    screenshots_destination)).grid(row=6, pady=5, column=2, padx=5)
Button(frame1, text="...", height=1, width=2, cursor="hand2",  command=lambda: select_directory(
    screenshots_destination)).grid(row=6, pady=5, column=3, padx=5)

Label(frame1, text="Documents: ").grid(
    row=8, column=0, columnspan=1, sticky=W)

documents_destination = Entry(frame1, textvariable=documents_dest,
                    width=50, font=("Calibri", 12))
documents_destination.grid(row=8, column=1, padx=5, pady=5, ipady=3)
Button(frame1, text="X", height=1, width=2, cursor="hand2",  command=lambda: disable_entry(
    documents_destination)).grid(row=8, column=2, padx=5, pady=5, sticky=W+E+N+S)
Button(frame1, text="...", height=1, width=2, cursor="hand2",  command=lambda: select_directory(
    documents_destination)).grid(row=8, column=3, padx=5, pady=5, sticky=W+E+N+S)


# source_directory.insert(0, EXAMPLE_DEST["monitored_directory"])
# images_destination.insert(0, EXAMPLE_DEST["images_directory"])
# videos_destination.insert(0, EXAMPLE_DEST["videos_directory"])
# screenshots_destination.insert(0, EXAMPLE_DEST["screenshots_directory"])
# documents_destination.insert(0, EXAMPLE_DEST["documents_directory"])


Label(window, text="", font=("Arial 7 bold")).pack()
submit_button = Button(window, cursor="hand2",
                    height=1, width=10, text="Submit", command=check_for_validity).pack(pady=3)

mainloop()
