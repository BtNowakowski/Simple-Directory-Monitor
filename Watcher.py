import time
import shutil
import os
import time
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


list_of_images = []
list_of_videos = []
list_of_screenshots = []
list_of_documents = []
already_added= []

class Watcher:
    def __init__(self, paths, window):
        self.paths = paths
        self.window = window
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = paths[0]

    def run(self):
        event_handler = Handler(self.paths)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        self.window.destroy()
        messagebox.showinfo('Info', 'The app currently runs in the background!\nTo completely kill the app use your task manager.')
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, paths: list[str]):
        self.dst_img = paths[1]
        self.dst_vid = paths[2]
        self.dst_ss = paths[3]
        self.dst_doc = paths[4]          

    def move_files(self, items_list):
        if len(items_list) > 0:
            for item in items_list:
                if (not os.path.exists(f'{item}')):
                    print('The file doesnt exist') 
                    items_list.remove(item)
                elif(not os.path.exists(f'{self.dst_img}\\{os.path.basename(item)}')):
                    try:
                        shutil.copy2(item,self.dst_img)
                        os.remove(item)
                        print(f'{item} was moved')
                    except PermissionError:
                        print("No permission!")
                    items_list.remove(item)
                    already_added.append(item)
                else:
                    print('The file is already in desired path')
                    items_list.remove(item)
                time.sleep(2)
    
    def on_any_event(self, event):

        if(event.src_path not in already_added):
            if event.is_directory:
                return None
            elif event.event_type == 'created':
                _,ext = os.path.splitext(event.src_path)
                fn = os.path.basename(event.src_path)
                filename,ext = os.path.splitext(fn)
                if(filename.__contains__('Zrzut') or filename.__contains__('screenshot') and ext =='.png' or ext =='.jpg'):
                    list_of_screenshots.append(os.path.join(event.src_path))
                elif(ext =='.pdf'or ext =='.txt'or ext =='.text'or ext =='.rtf' or ext =='.html' or ext =='.asc'):
                    list_of_documents.append(os.path.join(event.src_path))
                elif(ext =='.png' or ext =='.jpg' or ext =='.gif' or ext =='.webp' or ext =='.tiff' or ext =='.psd' or ext =='.raw'or ext =='.jpeg'or ext =='.svg' or ext =='.ai'or ext =='.eps'):
                    list_of_images.append(os.path.join(event.src_path))
                elif(ext =='.mp4'):
                    list_of_videos.append(os.path.join(event.src_path))
                else:
                    print(f'skip - {event.src_path}')

            self.move_files(list_of_images)
            self.move_files(list_of_screenshots)
            self.move_files(list_of_videos)
            self.move_files(list_of_documents)