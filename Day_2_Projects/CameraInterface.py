# Camera Interface
# by Mark Thornber

#This reqires an extra library installed. From a terminal window type
#in "sudo apt-get install python3-pil.imagetk" (no quotes) then press enter
#You also need two pictures called default.jpg and testpic.jpg in the 
#same place as the program

import tkinter as tk
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep
import explorerhat as eh


#These functions are run by pressing the buttons
def ehfwd(event):
    eh.motor.one.forward(100)

def ehbwd(event):
    eh.motor.one.backwards(100)

def ehstop(event):
    eh.motor.one.stop()

def showprev():
    global x,y
    x=mywindow.winfo_rootx()
    y=mywindow.winfo_rooty()
	#The preview is drawn directly on the screen 
	#on top of everything else
	#The given coordinates draw it in the right place on top of the window
    camera.start_preview(fullscreen=False,window=(x+97,y-59,640,480))

def noprev():
    camera.stop_preview()

def update():
    pic2 = './testpic.jpg'
    img2 = importpic(pic2)
    camera.stop_preview()
    mypic.configure(image=img2)
    mypic.image=img2

def takepic():
    camera.capture('./testpic.jpg')

#This function opens and resizes pictures to display in the panel
def importpic(picture):
    origpic=Image.open(picture)
    resizedpic=origpic.resize((640,360),Image.ANTIALIAS)
    return ImageTk.PhotoImage(resizedpic)

#Define the default picture
pic = './default.jpg'
#Set up the camera
camera = PiCamera()

#This part sets up the window
mywindow = tk.Tk()
mywindow.title('Camera')
mywindow.grid()
#Initialise variables
x=0
y=0
img = importpic(pic)
#Define and set up the widgets (buttons etc.)
mypic = tk.Label(mywindow,image=img,height=360,width=640)
mypic.grid(row=0,column=1,rowspan=6)
fwdButton = tk.Button(mywindow,text='Forward',bg='grey')
fwdButton.bind('<Button-1>',ehfwd)
fwdButton.bind('<ButtonRelease-1>',ehstop)
fwdButton.grid(row=0,column=0)
bwdButton = tk.Button(mywindow,text='Backwards',bg='grey')
bwdButton.bind('<Button-1>',ehbwd)
bwdButton.bind('<ButtonRelease-1>',ehstop)
bwdButton.grid(row=1,column=0)
picButton = tk.Button(mywindow,text='Take Pic',bg='grey',command=takepic)
picButton.grid(row=2,column=0)
updateButton = tk.Button(mywindow,text='Update Pic',bg='grey',command=update)
updateButton.grid(row=3,column=0)
prevButton = tk.Button(mywindow,text='Preview',bg='grey',command=showprev)
prevButton.grid(row=4,column=0)
stprevButton = tk.Button(mywindow,text='No Preview',bg='grey',command=noprev)
stprevButton.grid(row=5,column=0)

#The next section centres the window on the screen:
#Temporarily hide the window to avoid drawing in the wrong position
mywindow.withdraw()
#Update the current size of the window
mywindow.update_idletasks()  
#Calculate the correct position
x = (mywindow.winfo_screenwidth() - mywindow.winfo_reqwidth()) / 2
y = (mywindow.winfo_screenheight() - mywindow.winfo_reqheight()) / 2
#Centre the window
mywindow.geometry("+%d+%d" % (x, y))
#Finally, draw the window
mywindow.deiconify()

#Clear the settings and start the loop
mywindow.mainloop()
