from PIL import Image
from PIL import ImageTk
import Tkinter
import imutils
import time
import datetime
import tkMessageBox
from os import listdir
import cv2

l=list()
root = Tkinter.Tk()
date=time.strftime("%d-%m-%Y")
current=0

def Video():
        for i in xrange(len(l)):
                img = cv2.imread(".\\MotionImgDay_"+date+"\\"+str(l[i])+".jpg")
                print ".\\MotionImgDay_"+date+"\\"+str(l[i])+".jpg"
                cv2.putText(img, "Press Q to Exit", (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                cv2.imshow('video',img)        
                if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
                        break
                time.sleep(1)
        cv2.destroyAllWindows()
        tkMessageBox.showinfo('No More', 'Done')

def get_latest():
        global date
        date=time.strftime("%d-%m-%Y")
        text_list = list()
        l=list()
        current=0
        update()
        move(0)
def update():
        global l,date
        root.title("Entry Logs of "+date)
        l=list()
        try:
                image_list = listdir(".\\MotionImgDay_"+date)
        except:
                tkMessageBox.showinfo('Wrong Date', 'Enter again')
                get_latest()
                return
        for i in image_list:
                g=[i[x] for x in xrange(0,len(i)-4)]
                g=''.join(g)
                g=int(g)
                l.append(g)
        l.sort()
        #print l
update()

def move(delta):
        global current, image_list
        current += delta
        if current <0:
                current =0
                tkMessageBox.showinfo('End', 'No more image.')
                return
        try:
                image = Image.open(".\\MotionImgDay_"+date+"\\"+str(l[current])+".jpg")
                new_width  = 600
                new_height = 600
                image = image.resize((new_width, new_height), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                label['image'] = photo
                label.photo = photo
                root.after(1000, update())
        except:
                current -= delta
                tkMessageBox.showinfo('End', 'No more image.')
                return

        
root.minsize(700, 600)
root.title("Entry Logs of "+date)
label = Tkinter.Label(root, compound=Tkinter.TOP)
label.grid(row=0,column=0, padx=5, pady=5)

frame = Tkinter.Frame(root)
frame.grid(row=0,column=1, padx=5, pady=5)
Tkinter.Button(frame, text='Previous', command=lambda: move(-1)).grid(row=1,column=1, padx=5, pady=5)
Tkinter.Button(frame, text='Next', command=lambda: move(+1)).grid(row=1,column=2, padx=5, pady=5)
Tkinter.Button(frame, text='Today', command=lambda: get_latest()).grid(row=1,column=3, padx=5, pady=5)

Tkinter.Label(frame, text="For a Specific date Enter |").grid(row=3,column=1, padx=5, pady=5)
Tkinter.Label(frame, text="Date in dd-mm-yyyy     |").grid(row=4,column=1, padx=5, pady=5)
Tkinter.Label(frame, text="|  To See all").grid(row=3,column=2, padx=5, pady=5)
Tkinter.Label(frame, text="   |  Click Show ").grid(row=4,column=2, padx=5, pady=5)

e1 = Tkinter.Entry(frame)
e1.grid(row=5,column=1, padx=5, pady=5)

def specificDate():
        global date
        inpu= e1.get()
        date=inpu
        print date
        l=list()
        current=0
        update()
        move(0)

b = Tkinter.Button(frame, text="get", width=10, command=specificDate)
b.grid(row=6,column=1, padx=5, pady=5)
b = Tkinter.Button(frame, text="Show", width=10, command=Video)
b.grid(row=6,column=2, padx=5, pady=5)
move(0)

root.mainloop()
