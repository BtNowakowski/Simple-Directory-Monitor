from importlib.resources import path
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
dst_ss = paths[3]
dst_doc = paths[4]
list_of_images = []
list_of_videos = []
list_of_screenshots = []
list_of_documents =[]
already_added= []
for root, dirs, files in os.walk(src):
	for file in files:
            fname, ext = os.path.splitext(file)
            if(fname.__contains__('Zrzut ekranu') or fname.__contains__('screenshot') or fname.__contains__('Adnotacja')or fname.__contains__('Annotation')):
                list_of_screenshots.append(os.path.join(root,file))
            elif(ext =='.pdf'or ext =='.txt'or ext =='text'or ext =='.rtf' or ext =='.html' or ext =='.asc'):
                list_of_documents.append(os.path.join(root,file))
            elif(ext =='.png' or ext =='.jpg' or ext =='.gif' or ext =='.webp' or ext =='.tiff' or ext =='.psd' or ext =='.raw'or ext =='.jpeg'or ext =='.svg' or ext =='.ai'or ext =='.eps'):
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
            for name in list_of_screenshots:
                if (not os.path.exists(f'{name}')):
                    print('The file doesnt exist') 
                    list_of_screenshots.remove(name)
                elif(not os.path.exists(f'{dst_ss}\\{os.path.basename(name)}')):
                    shutil.copy2(name,dst_ss)
                    os.remove(name)
                    print(f'{name} was moved')
                    list_of_screenshots.remove(name)
                    already_added.append(name)
                else:
                    print('The image is already in the desired path')
                    list_of_screenshots.remove(name)
            for name in list_of_documents:
                if (not os.path.exists(f'{name}')):
                    print('The file doesnt exist') 
                    list_of_documents.remove(name)
                elif(not os.path.exists(f'{dst_doc}\\{os.path.basename(name)}')):
                    shutil.copy2(name,dst_doc)
                    os.remove(name)
                    print(f'{name} was moved')
                    list_of_documents.remove(name)
                    already_added.append(name)
                else:
                    print('The image is already in the desired path')
                    list_of_documents.remove(name)
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
                _,ext = os.path.splitext(event.src_path)
                fn = os.path.basename(event.src_path)
                filename,ext = os.path.splitext(fn)
                if(filename.__contains__('Zrzut') or filename.__contains__('screenshot') and ext =='.png' or ext =='.jpg'):
                    list_of_screenshots.append(os.path.join(event.src_path))
                elif(ext =='.pdf'or ext =='.txt'or ext =='text'or ext =='.rtf' or ext =='.html' or ext =='.asc'):
                    list_of_documents.append(os.path.join(event.src_path))
                elif(ext =='.png' or ext =='.jpg' or ext =='.gif' or ext =='.webp' or ext =='.tiff' or ext =='.psd' or ext =='.raw'or ext =='.jpeg'or ext =='.svg' or ext =='.ai'or ext =='.eps'):
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
                        already_added.append(name1)
                    else:
                        print('The video is already in the desired path')
                        list_of_images.remove(name1)
                for name1 in list_of_screenshots:
                    if (not os.path.exists(f'{name1}')):
                        print('The file doesnt exist') 
                        list_of_screenshots.remove(name1)
                    elif(not os.path.exists(f'{dst_ss}\\{os.path.basename(name1)}')):
                        shutil.copy2(name1,dst_ss)
                        os.remove(name1)
                        print(f'{name1} was moved')
                        list_of_screenshots.remove(name1)
                        already_added.append(name1)
                    else:
                        print('The screenshot is already in the desired path')
                        list_of_screenshots.remove(name1)
                for name in list_of_documents:
                    if (not os.path.exists(f'{name}')):
                        print('The file doesnt exist') 
                        list_of_documents.remove(name)
                    elif(not os.path.exists(f'{dst_doc}\\{os.path.basename(name)}')):
                        shutil.copy2(name,dst_doc)
                        os.remove(name)
                        print(f'{name} was moved')
                        list_of_documents.remove(name)
                        already_added.append(name)
                    else:
                        print('The document is already in the desired path')
                        list_of_documents.remove(name)                
                time.sleep(2)

            elif event.event_type == 'modified':
                pass
if __name__ == '__main__':
    w = Watcher()
    w.run()