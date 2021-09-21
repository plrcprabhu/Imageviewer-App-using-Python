from Tkinter import *
from PIL import ImageTk,Image
import tkFileDialog
import tkMessageBox
import os

root=Tk()
root.title("IMAGE VIEWER APP")

images=[]

def forward(img_num):
  global mylabel
  global move_back
  global move_forward
  global move_tooback
  global move_tooforward
  mylabel.grid_forget()
  mylabel=Label(root2,image=images[img_num-1])
  move_back=Button(root2,text="<",command=lambda:back(img_num-1))
  move_forward=Button(root2,text=">",command=lambda:forward(img_num+1))
  move_tooback=Button(root2,text="<<",command=too_back)
  move_tooforward=Button(root2,text=">>",command=too_forward)
  if(img_num==len(images)):
    move_forward=Button(root2,text=">",state=DISABLED)
    move_tooforward=Button(root2,text=">>",state=DISABLED)
  mylabel.grid(row=0,column=0,columnspan=5)
  move_back.grid(row=1,column=1)
  move_forward.grid(row=1,column=3)
  move_tooback.grid(row=1,column=0)
  move_tooforward.grid(row=1,column=4)
  
def back(img_num):
  global mylabel
  global move_back
  global move_forward
  global move_tooback
  global move_tooforward
  mylabel.grid_forget()
  mylabel=Label(root2,image=images[img_num-1])
  move_back=Button(root2,text="<",command=lambda:back(img_num-1))
  move_forward=Button(root2,text=">",command=lambda:forward(img_num+1))
  move_tooback=Button(root2,text="<<",command=too_back)
  move_tooforward=Button(root2,text=">>",command=too_forward)
  if(img_num==1):
    move_back=Button(root2,text="<",state=DISABLED)
    move_tooback=Button(root2,text="<<",state=DISABLED)
  mylabel.grid(row=0,column=0,columnspan=5)
  move_back.grid(row=1,column=1)
  move_forward.grid(row=1,column=3)
  move_tooback.grid(row=1,column=0)
  move_tooforward.grid(row=1,column=4) 
  
def too_forward():
  global mylabel
  global move_back
  global move_forward
  global move_tooback
  global move_tooforward
  mylabel.grid_forget()
  mylabel=Label(root2,image=images[-1])
  move_back=Button(root2,text="<",command=lambda:back(len(images)-1))
  move_tooback=Button(root2,text="<<",command=too_back)
  move_forward=Button(root2,text=">",state=DISABLED)
  move_tooforward=Button(root2,text=">>",state=DISABLED)
  mylabel.grid(row=0,column=0,columnspan=5)
  move_back.grid(row=1,column=1)
  move_forward.grid(row=1,column=3)
  move_tooback.grid(row=1,column=0)
  move_tooforward.grid(row=1,column=4)

def too_back():
  global mylabel
  global move_back
  global move_forward
  global move_tooback
  global move_tooforward
  mylabel.grid_forget()
  mylabel=Label(root2,image=images[0])
  move_forward=Button(root2,text=">",command=lambda:forward(2))
  move_tooforward=Button(root2,text=">>",command=too_forward)
  move_back=Button(root2,text="<",state=DISABLED)
  move_tooback=Button(root2,text="<<",state=DISABLED)
  mylabel.grid(row=0,column=0,columnspan=5)
  move_back.grid(row=1,column=1)
  move_forward.grid(row=1,column=3)
  move_tooback.grid(row=1,column=0)
  move_tooforward.grid(row=1,column=4)



def popup():
	tkMessageBox.showerror("Error Message!","Album is empty!")

def showimg():
	if(len(images)==0):
		popup()
	else:
		global mylabel
		global move_back
		global move_forward
		global move_tooback
		global move_tooforward
		global root2
		root2=Toplevel()
		mylabel=Label(root2,image=images[0])
		move_exit=Button(root2,text="exit",command=root.quit)
		move_back=Button(root2,text="<",state=DISABLED)
		move_forward=Button(root2,text=">",command=lambda:forward(2))
		move_tooback=Button(root2,text="<<",state=DISABLED)
		move_tooforward=Button(root2,text=">>",command=too_forward)
		mylabel.grid(row=0,column=0,columnspan=5)
		move_exit.grid(row=1,column=2)
		move_back.grid(row=1,column=1)
		move_forward.grid(row=1,column=3)
		move_tooback.grid(row=1,column=0)
		move_tooforward.grid(row=1,column=4)

def takeImages():
	fil=tkFileDialog.askopenfilename()
	img=ImageTk.PhotoImage(Image.open(fil))
	images.append(img)
	global suc_lab
	suc_lab.config(text=str(len(images))+("image" if len(images)==1 else "images")+" Uploaded!!")
	suc_lab.pack()

lab=Label(root,text="Upload an image").pack()
btn=Button(root,text="Upload",command=takeImages).pack()
view_btn=Button(root,text="See the Album",command=showimg).pack()
suc_lab=Label(root,text="")
root.attributes("-zoomed",True)

root.mainloop()

