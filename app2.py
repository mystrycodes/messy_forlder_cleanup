import os
import shutil


extensions={
'videos':('.mp4','.mov','.mwv','.wmv','.avi','.avchd','.flv', '.f4v', '.swf','.mkv','.webm','.mkv','.mpeg'),
'audios':('.mp3','.m4a','.wav','.flac','.wma','.aac'),
'text':('.doc','.txt','.pdf','.rtf','.wpd','.odt','.tex'),
'images':('.jfif','.jpeg','.png','.jpg','.gif','.svg','.pjp','.pjpeg')
}

path=input("Enter the path of folder");
BASE_DIR=os.path.dirname(path)


for folder_path,_,files in os.walk(path):
    for file in files:
        extension=os.path.splitext(file)[-1]
        if extension in extensions['audios']:
            destination_dir=os.path.join(BASE_DIR,'AUDIOS')
        elif extension in extensions['videos']:
            destination_dir=os.path.join(BASE_DIR,'VIDEOS')
        elif extension in extensions['images']:
            destination_dir=os.path.join(BASE_DIR,'IMAGES')
        elif extension in extensions['text']:
            destination_dir=os.path.join(BASE_DIR,'DOCS')
        else:
            destination_dir=os.path.join(BASE_DIR,'MISC')
        if not os.path.exists(destination_dir):
            os.mkdir(destination_dir)
        old_path=os.path.join(folder_path,file)
        new_path=os.path.join(destination_dir,file)
        shutil.move(old_path,new_path)

folders_still_present=list(os.walk(path))
for i in range(len(folders_still_present)-1,-1,-1):
    if len(os.listdir(folders_still_present[i][0]))==0:
        os.rmdir(folders_still_present[i][0])
