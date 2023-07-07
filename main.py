# Coded By Shikto
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import moviepy.editor as me

filename=''
# Convert Function
def convert():
        global filename
        filetypes=(("Audio files","*.mp3 , *.wav , *.ogg"),("All files","*.*"))
        video=me.VideoFileClip(filename)
        audio=video.audio
        file=asksaveasfilename(filetypes=filetypes)
        audio.write_audiofile(f'{file}{format.get()}')
        label5=Label(root,text="Done",font=("Arial",18),fg="green")
        label5.pack()
        label5.place(x=450,y=300)

# Select Function
def select():
    global filename
    filetypes = (
        ('video files', '*.WEBM , *.MPG, *.MP2 , *.MPEG , *.MPE , *.MPV , *.MP4 , *.M4P , *.M4V , *.AVI , *.WMV , *.MOV , *.QT , *.FLV , *.SWF , *.AVCHD'),
        ('All files', '*.*')
    )
    filename=askopenfilename(filetypes=filetypes)
    label3.config(text="File Selected",fg="green")
    label4=Label(root,text="Audio Format :-",font=("Arial",18))
    label4.pack()
    label4.place(x=125,y=250)
    options=[".mp3",".ogg",".wav"]
    format.set(".mp3")
    menu=OptionMenu(root,format,*options)
    menu.pack()
    menu.place(x=375,y=250)
    button3=Button(root,text="Export",font=("Harlow Solid",12),command=convert,width=10,height=1)
    button3.pack()
    button3.place(x=250,y=300)

# GUI 
root=Tk()
# Window dimension
root.geometry("600x350")
root.minsize(600,350)
root.maxsize(600,350)
root.title("SoundGrab Pro v0.0.1-alpha")
icon=PhotoImage(file="icon.png")
root.iconphoto(True,icon)

# Title
label1=Label(root,text="SoundGrab Pro",font=("GEEKSFORGEEKS",32,"bold","italic"))
label1.pack()
label1.place(x=140,y=5)
# Heading
label2=Label(root,text="Select Video",font=("Arial",18))
label2.pack()
label2.place(x=230,y=100)
# Select video file button
button1=Button(root,text="Select",font=("Harlow Solid",12),command=select,width=10,height=1)
button1.pack()
button1.place(x=250,y=200)
label3=Label(root,font=("Footlight MT",18,"bold"))
label3.pack()
label3.place(x=225,y=150)
format=StringVar()
root.mainloop()