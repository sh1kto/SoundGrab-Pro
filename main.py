from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import moviepy.editor as me

select = None

# GUI 
root=Tk()
# Window dimension
root.geometry("600x350")
root.minsize(600,350)
root.maxsize(600,350)
root.title('SoundGrab Pro v0.0.1-alpha')

# Title
label1=Label(root,text="SoundGrab Pro",font=("GEEKSFORGEEKS",32,"bold","italic"))
label1.pack()
label1.place(x=140,y=5)
# Heading
label2=Label(root,text="Select Video",font=("Arial",18))
label2.pack()
label2.place(x=220,y=180)

# Select video file button
button1=Button(root,text="Select",font=("Harlow Solid",12),command=select,width=10,height=1)
button1.pack()
button1.place(x=240,y=240)


root.mainloop()