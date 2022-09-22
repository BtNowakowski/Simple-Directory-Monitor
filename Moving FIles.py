import time
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from interface import Get_MyInputValue

paths = Get_MyInputValue()
src = paths[0]
dst_img = paths[1]
dst_vid = paths[2]
list_of_images = []
list_of_videos = []
already_added= []
for root, dirs, files in os.walk(src):
	for file in files:
            split1 = os.path.splitext(file)
            ext = split1[1]
            if(ext =='.png' or ext =='.jpg'):
                list_of_images.append(os.path.join(root,file))
            elif(ext =='.mp4'):
                list_of_videos.append(os.path.join(root,file))
            for name in list_of_images:
                if (not os.path.exists(f'{name}')):
                    print('The file doesnt exist') 
                    list_of_images.remove(name)
                elif(not os.path.exists(f'{dst_img}\\{os.path.basename(name)}')):
                    shutil.copy2(name,dst_img)
                    os.remove(name)
                    print(f'{name} was moved')
                    list_of_images.remove(name)
                    already_added.append(name)
                else:
                    print('The image is already in the desired path')
                    list_of_images.remove(name)
                for name1 in list_of_videos:
                    if (not os.path.exists(f'{name1}')):
                        print('The file doesnt exist') 
                        list_of_videos.remove(name1)
                    elif(not os.path.exists(f'{dst_vid}\\{os.path.basename(name1)}')):
                        shutil.copy2(name1,dst_vid)
                        os.remove(name1)
                        print(f'{name1} was moved')
                        list_of_videos.remove(name1)
                    else:
                        print('The video is already in the desired path')
                        list_of_videos.remove(name1)


class Watcher:
    DIRECTORY_TO_WATCH = src
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if(event.src_path not in already_added):
            if event.is_directory:
                return None

            elif event.event_type == 'created':
                time.sleep(3)
                # Take any action here when a file is first created.
                # print(f"Received created event - {event.src_path}." )
                _,ext = os.path.splitext(event.src_path)
                # fn,ext = os.path.splitext(filename)
                if(ext =='.png' or ext =='.jpg'):
                    list_of_images.append(os.path.join(event.src_path))
                elif(ext =='.mp4'):
                    list_of_videos.append(os.path.join(event.src_path))
                else:
                    print(f'skip - {event.src_path}')
                for name in list_of_images:
                    if (not os.path.exists(f'{name}')):
                        print('The file doesnt exist') 
                        list_of_images.remove(name)
                    elif(not os.path.exists(f'{dst_img}\\{os.path.basename(name)}')):
                        shutil.copy2(name,dst_img)
                        os.remove(name)
                        print(f'{name} was moved')
                        list_of_images.remove(name)
                        already_added.append(name)
                    else:
                        print('The image is already in the desired path')
                        list_of_images.remove(name)
                for name1 in list_of_videos:
                    if (not os.path.exists(f'{name1}')):
                        print('The file doesnt exist') 
                        list_of_images.remove(name1)
                    elif(not os.path.exists(f'{dst_vid}\\{os.path.basename(name1)}')):
                        shutil.copy2(name1,dst_vid)
                        os.remove(name1)
                        print(f'{name1} was moved')
                        list_of_videos.remove(name1)
                    else:
                        print('The video is already in the desired path')
                        list_of_images.remove(name1)
                time.sleep(5)

            elif event.event_type == 'modified':
                pass

if __name__ == '__main__':
    w = Watcher()
    w.run()

