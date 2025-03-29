import os
import shutil

path = input("Enter Path: ")


music = ("AUDIOS","MP3","AMR","M4A","FLAC","WAV","WMA","AAC")
videos = ("VIDEOS","DIVX","WEBM","MKV","FLV","VOB","OGG","OGV","DRC","AVI","MPEG","MTS","M2TS","TS","MOV","WMV","ASF","MP4","M4P","M4V","M2V","M4V","SVI","3GP")
Documents = ("DOCUMENTS","DOC","DOCX","HTML","HTM","PDF","ODT","XLS","XLSX","ODS","PPT","PPTX","TXT")                      
Images = ("IMAGES","JPG","JPEG","GIF","PNG","WEBP","HEIF","TIFF","BMP","PAM")

for s in (music,videos,Documents,Images):
    for r in s :
        if os.path.exists(path+'/'+r):
            files = os.listdir(path+'/'+r+'/')
            for file in files:
                shutil.move(path+'/'+r+'/'+file,path+'/'+file)
for t in ("EXECUTABLES","PYTHON","exe","py","PROGRAMMING CODES","EXE","PY"):
    if os.path.exists(path+'/'+t):
        r = t
        files = os.listdir(path+'/'+r+'/')
        for file in files:
            shutil.move(path+'/'+r+'/'+file,path+'/'+file)


de = os.listdir(path)
for v in de:
    filename,extension = os.path.splitext(v)
    extension = (extension[1:]).upper()
    if extension == "" :
        delet = os.listdir(path+'/'+v)
        m = len(delet)
        if m == 0 :
            shutil.rmtree(path+'/'+v)
       


