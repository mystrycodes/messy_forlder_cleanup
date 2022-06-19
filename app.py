import os
import shutil

extensions={
'videos':('.mp4','.mov','.mwv','.wmv','.avi','.avchd','.flv', '.f4v', '.swf','.mkv','.webm','.mkv','.mpeg'),
'audios':('.mp3','.m4a','.wav','.flac','.wma','.aac'),
'text':('.doc','.txt','.pdf','.rtf','.wpd','.odt','.tex'),
'images':('.jfif','.jpeg','.png','.jpg','.gif','.svg','.pjp','.pjpeg')
}

path=r'D:\PYTHON\PROJECTS\CleanMyStuff\dummy';
BASE_DIR=os.path.dirname(path)


def file_finder(path,extension):        
    return [file for file in os.listdir(path) if os.path.splitext(file)[-1] in extension]

for extension_type,extension_values in extensions.items():
    destination_dir=os.path.join(BASE_DIR,extension_type)
    for folder_path,_,item in os.walk(path):
        for file in file_finder(folder_path,extension_values):
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
            old_path=os.path.join(folder_path,file)
            new_path=os.path.join(destination_dir,file)
            shutil.move(old_path,new_path)


for items,_,_ in os.walk(path):
    if os.listdir(items)==0:
        os.rmdir(items)

os.rename(path,os.path.join(BASE_DIR,'MISC'))

    
