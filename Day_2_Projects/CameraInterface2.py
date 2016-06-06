# Camera Interface v2
# by Mark Thornber

#This reqires an extra library installed. From a terminal window type
#in "sudo apt-get install python3-pil.imagetk" (no quotes) then press enter
#You also need two pictures called default.jpg and testpic.jpg in the 
#same place as the program


import tkinter as tk
import io
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep



#These functions are run by pressing the buttons
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

def latest():
    newpic = pics[len(pics)-1]
    showpic(newpic)

def showpic(picture):
    camera.stop_preview()
    img = importpic(picture)
    mypic.configure(image=img)
    mypic.image=img

def takepic():
    global fn
    newpic = './picture' + str(next(counter)).zfill(3) + '.jpg'
    camera.capture(newpic)
    pics.append(newpic)

def picplus():
    global currentpic
    if currentpic < len(pics)-1:
        currentpic += 1
        newpic = pics[currentpic]
        showpic(newpic)

def picminus():
    global currentpic
    if currentpic > 0:
        currentpic -= 1
        newpic = pics[currentpic]
        showpic(newpic) 

#This generates numbers to use in the file names
 def counter():
    n = 1
    while True:
        yield n
        n += 1 

#This function opens and resizes pictures to display in the panel
def importpic(picture):
    origpic=Image.open(picture)
    resizedpic=origpic.resize((640,360),Image.ANTIALIAS)
    return ImageTk.PhotoImage(resizedpic)
        
#Initialise variables
pic1 = './default.jpg'
pic2 = './testpic.jpg'
currentpic = 0
filenum = counter()
pics = [pic1,pic2]
#Set up the camera
camera = PiCamera()
camera.resolution = (1280,720)
#This part sets up the window
mywindow = tk.Tk()
mywindow.title('Camera')
mywindow.grid()
#More initialising
x=0
y=0
picname = tk.StringVar()
picname.set(pic1)
img = importpic(pics[0])
#Define and set up the widgets (buttons etc.)
mypic = tk.Label(mywindow,image=img,height=360,width=640)
mypic.grid(row=0,column=1,rowspan=6)
picnameLabel = tk.Label(mywindow,textvariable=picname)
picnameLabel.grid(row=6,column=1)
picplusButton = tk.Button(mywindow,text='Pic +',bg='grey',command=picplus)
picplusButton.grid(row=0,column=0)
picminusButton = tk.Button(mywindow,text='Pic -',bg='grey',command=picminus)
picminusButton.grid(row=1,column=0)
picButton = tk.Button(mywindow,text='Take Pic',bg='grey',command=takepic)
picButton.grid(row=3,column=0)
latestButton = tk.Button(mywindow,text='Latest Pic',bg='grey',command=latest)
latestButton.grid(row=2,column=0)
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
