from Tkinter import *
from PIL import ImageTk,Image
root=Tk()
img1=ImageTk.PhotoImage(Image.open("bird1.png"))
img2=ImageTk.PhotoImage(Image.open("bird2.png"))
img3=ImageTk.PhotoImage(Image.open("bird3.png"))
img4=ImageTk.PhotoImage(Image.open("bird4.png"))
img5=ImageTk.PhotoImage(Image.open("bird5.png"))
images=[img1,img2,img3,img4,img5]

def forward(img_num):
  global mylabel
  global move_back
  global move_forward
  global move_tooback
  global move_tooforward
  mylabel.grid_forget()
  mylabel=Label(root,image=images[img_num-1])
  move_back=Button(root,text="<",command=lambda:back(img_num-1))
  move_forward=Button(root,text=">",command=lambda:forward(img_num+1))
  move_tooback=Button(root,text="<<",command=too_back)
  move_tooforward=Button(root,text=">>",command=too_forward)
  if(img_num==len(images)):
    move_forward=Button(root,text=">",state=DISABLED)
    move_tooforward=Button(root,text=">>",state=DISABLED)
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
  mylabel=Label(root,image=images[img_num-1])
  move_back=Button(root,text="<",command=lambda:back(img_num-1))
  move_forward=Button(root,text=">",command=lambda:forward(img_num+1))
  move_tooback=Button(root,text="<<",command=too_back)
  move_tooforward=Button(root,text=">>",command=too_forward)
  if(img_num==1):
    move_back=Button(root,text="<",state=DISABLED)
    move_tooback=Button(root,text="<<",state=DISABLED)
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
  mylabel=Label(root,image=images[-1])
  move_back=Button(root,text="<",command=lambda:back(len(images)-1))
  move_tooback=Button(root,text="<<",command=too_back)
  move_forward=Button(root,text=">",state=DISABLED)
  move_tooforward=Button(root,text=">>",state=DISABLED)
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
  mylabel=Label(root,image=images[0])
  move_forward=Button(root,text=">",command=lambda:forward(2))
  move_tooforward=Button(root,text=">>",command=too_forward)
  move_back=Button(root,text="<",state=DISABLED)
  move_tooback=Button(root,text="<<",state=DISABLED)
  mylabel.grid(row=0,column=0,columnspan=5)
  move_back.grid(row=1,column=1)
  move_forward.grid(row=1,column=3)
  move_tooback.grid(row=1,column=0)
  move_tooforward.grid(row=1,column=4)

mylabel=Label(root,image=img1)
move_exit=Button(root,text="exit",command=root.quit)
move_back=Button(root,text="<",state=DISABLED)
move_forward=Button(root,text=">",command=lambda:forward(2))
move_tooback=Button(root,text="<<",state=DISABLED)
move_tooforward=Button(root,text=">>",command=too_forward)
mylabel.grid(row=0,column=0,columnspan=5)
move_exit.grid(row=1,column=2)
move_back.grid(row=1,column=1)
move_forward.grid(row=1,column=3)
move_tooback.grid(row=1,column=0)
move_tooforward.grid(row=1,column=4)
root.mainloop()
