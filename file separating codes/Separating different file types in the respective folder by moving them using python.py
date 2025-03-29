import tkinter as tk    # For creating Graphical User Interface
import os               # For interaction of code with operating system
import shutil           # For high level file operations
import time             # For time measurement

# Tuples named as file types with extensions of respective file types included in it 

music = ("AUDIOS","MP3","AMR","M4A","FLAC","WAV","WMA","AAC")
videos = ("VIDEOS","MP4","MKV","FLV","3GP","OGG","OGV","DRC","AVI","MPEG","MTS","M2TS","TS","MOV","WMV","ASF","DIVX","M4P","M4V","M2V","M4V","SVI","VOB","WEBM")
Documents = ("DOCUMENTS","DOC","DOCX","HTML","HTM","PDF","ODT","XLS","XLSX","ODS","PPT","PPTX","TXT","XML")
Images = ("IMAGES","JPG","JPEG","GIF","PNG","WEBP","HEIF","TIFF","BMP","PAM")
Programming_codes = ("PROGRAMMING CODES","PY","C","CPP","JAVA","KTX","JS","RDA","RDS","RDS")
executables = ("EXECUTABLES","EXE")
number = 0

# Create a new window
window = tk.Tk()

# Set the dimensions of the created window
window.geometry("800x400")

# Set the background color of the window
window.config(bg="violet")

# Set Window Title
window.title('FILE HANDLING USING PYTHON')

window.resizable(width=False,height=False)

# Functions for updation of current status, time and number of files handeled  

def update_result(text):
    result.configure(text=text)

def update_time(text):
    times.configure(text=text)

def update_number(text):
    numbers.configure(text=text)

# Main function for sorting the files

def main_code():
    global start_time
    start_time = time.time()
    global files, number
    path = entry.get()
    if os.path.exists(path):
        files = os.listdir(path)
        number = len(files)
        for file in files:
            filename,extension = os.path.splitext(file)
            extension = (extension[1:]).upper()
            for r in (music,videos,Documents,Images,Programming_codes,executables):
                if extension in r:
                    extension = r[0]
                    break
            if os.path.exists(path+'/'+extension):
                shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
            else:
                os.makedirs(path+'/'+extension)
                shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
        update_result(text="Sorting completed...")
    else:
        update_result(text="Enter valid path...")
    global end_time
    end_time = time.time()
    timee = end_time - start_time
    update_time(text= "Execution time = " + str(timee) + " sec")
    update_number(text= "Total files handeled = " + str(number))

   #REMOVING EMPTY FLODERS

def delete() :
    path = entry.get()
    de = os.listdir(path)
    for v in de:
        filename,extension = os.path.splitext(v)
        extension = (extension[1:]).upper()
        if extension == "" :
            delet = os.listdir(path+'/'+v)
            m = len(delet)
            if m == 0 :
                shutil.rmtree(path+'/'+v)
       
    

# Unsorting function

def reverse():
    global start_time
    start_time = time.time()
    global number
    number=0
    path = entry.get()
    if os.path.exists(path):
        for s in (music,videos,Documents,Images,Programming_codes,executables):
            for r in s :
                if os.path.exists(path+'/'+r):
                    fil = os.listdir(path+'/'+r+'/')
                    b = len(fil)
                    number = number+b
                    for file in fil:
                        if file in files :
                            shutil.move(path+'/'+r+'/'+file,path+'/'+file)
                        else :
                            continue

        delete()
        
        update_result(text="Unsorting completed...")
    else:
        update_result(text="Enter valid path...")
    update_number(text= "Total files handeled = " + str(number))
    global end_time
    end_time = time.time()
    timee = end_time - start_time
    update_time(text= "Execution time = " + str(timee) + " sec")
    


# Heading of our project
title = tk.Label(window,text="SORTING DIFFERENT FILE TYPES IN THE RESPECTIVE FOLDER BY MOVING THEM USING PYTHON",font=("Arial",13),fg="#fffcbd",bg="#065569")

# Heading for path entry
title2 = tk.Label(window,text="Enter path of the directory containing files:",font=("Arial",20),fg="black",bg="white")

# Buttons
button = tk.Button(text="SORT",width=25,height=2,bg="blue",fg="yellow", command = main_code)
button2 = tk.Button(text="UNSORT",width=25,height=2,bg="blue",fg="yellow", command = reverse)
# Exit Button
exit_button = tk.Button(window,text="Exit",font=("Arial",14), fg="White", bg="#b82741", command=exit)


entry = tk.Entry(fg="black", bg="pink", width=100)
result = tk.Label(window, text="** Enter path and click **", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
times = tk.Label(window, text="Time", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
numbers = tk.Label(window, text="Total files handeled", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)


title.place(x=12, y=10)
title2.place(x=10, y=60)
entry.place(x=100, y=130)
button.place(x=140, y=170)
button2.place(x=480, y=170)
exit_button.place(x=50,y=300)
result.place(x=320, y=280)
times.place(x=320, y=320)
numbers.place(x=320, y=350)

window.mainloop()


    

