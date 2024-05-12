import numpy as np
import cv2
import  random
from tkinter import *
from tkinter import  messagebox


class picture:
    def __init__(self,wind,path):
        self.path=path
        self.window=wind
        cv2.namedWindow("win2")
        self.img=cv2.imread(path)
        self.img2=cv2.imread(path)
        self.height, self.width, self.channels = self.img.shape
        cv2.imshow("win2",self.img)
        self.wx=100
        self.wy=300
        cv2.moveWindow("win2",self.wx,self.wy)
        self.Cx=0
        self.Cy = 0
        self.xpos=50
        self.ypos=50
        self.counter=0
        self.bordersize=0
        cv2.setMouseCallback("win2",self.chRand)

    def addTxt(self,event):
        txt=self.window.txt.get()
        pos=(self.xpos,self.ypos)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        thickness = 2
        cv2.putText(self.img,txt,pos,font,fontScale,color,thickness)
        cv2.putText(self.img2,txt,pos,font,fontScale,color,thickness)
        cv2.imshow("win2",self.img)
        self.xpos=(self.xpos+60)%self.wx
        self.ypos=(self.ypos+60)%self.wy
        self.window.txt.delete(0,END)

    def chSize(self,event):
        s=self.window.Lsize.get(self.window.Lsize.curselection()[0])
        self.width=int(float(self.width)*float(s))
        self.height=int(float(self.height)*float(s))
        dim = (self.width, self.height)
        self.img = cv2.resize(self.img, dim)
        self.img2 = cv2.resize(self.img2, dim)
        cv2.imshow("win2", self.img)


    def draw(self,event):
        selection=self.window.shape.curselection()[0]
        if(selection==0):
            cv2.setMouseCallback("win2", self.__drawCircle)
            return
        if(selection==1):
            cv2.setMouseCallback("win2", self.__drawSquare)
            return
        cv2.setMouseCallback("win2", self.__drawX)

    def __drawCircle(self,event,x,y,flags,param):
        if(event==cv2.EVENT_LBUTTONDOWN):
            self.Cx=x
            self.Cy=y
            return
        if(event==cv2.EVENT_LBUTTONUP):
            center=(int((self.Cx+x)/2),int((self.Cy+y)/2))
            color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            cv2.circle(self.img,center,int(abs(x-self.Cx)/2),color,thickness=3)
            cv2.circle(self.img2,center,int(abs(x-self.Cx)/2),color,thickness=3)
            cv2.imshow("win2",self.img)
            cv2.setMouseCallback("win2", self.finish)

    def __drawSquare(self,event,x,y,flags,param):
        if (event == cv2.EVENT_LBUTTONDOWN):
            self.Cx = x
            self.Cy = y
            return
        if (event == cv2.EVENT_LBUTTONUP):
            p1 = (int(self.Cx ) ,int(self.Cy ))
            p2 = (int(x) ,int(y))
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv2.rectangle(self.img, p1,p2,color, thickness=3)
            cv2.rectangle(self.img2, p1,p2,color, thickness=3)
            cv2.imshow("win2", self.img)
            cv2.setMouseCallback("win2", self.finish)

    def __drawX(self,event,x,y,flags,param):
        if (event == cv2.EVENT_LBUTTONDOWN):
            self.Cx = x
            self.Cy = y
            return
        if (event == cv2.EVENT_LBUTTONUP):
            self.counter+=1
            p1 = (int(self.Cx ) ,int(self.Cy ))
            p2 = (int(x) ,int(y))
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv2.line(self.img, p1,p2,color, thickness=3)
            cv2.line(self.img2, p1,p2,color, thickness=3)
            cv2.imshow("win2", self.img)
            if(self.counter==2):
                self.counter=0
                cv2.setMouseCallback("win2", self.finish)

    def chColor(self):
        v=self.window.v.get()
        if(v=="var1"):
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2HLS)
            cv2.imshow("win2", self.img)
            return
        if(v=="var2"):
            rows = self.img.shape[0]
            cols = self.img.shape[1]
            for i in range(0, rows):
                for j in range(0, cols):
                    if self.img.item(i, j, 2) > 155 and self.img.item(i, j, 0) < 200 and self.img.item(i, j,1) < 200:
                        self.img.itemset((i, j, 0), 0)
                        self.img.itemset((i, j, 1),0)
                        self.img.itemset((i, j, 2), 255)
            cv2.imshow("win2", self.img)
            return
        if(v=="var3"):
            rows = self.img.shape[0]
            cols = self.img.shape[1]
            for i in range(0, rows):
                for j in range(0, cols):
                    if self.img.item(i, j, 0) > 155 and self.img.item(i, j, 1) <155and self.img.item(i, j, 2)< 155:
                        self.img.itemset((i, j, 0), 255)
                        self.img.itemset((i, j, 1), 0)
                        self.img.itemset((i, j, 2), 0)
            cv2.imshow("win2",self.img)
            return
        if (v == "gray"):
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
            cv2.imshow("win2", self.img)
            return

    def cutPic(self,event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            self.Cx=x
            self.Cy=y
        elif event==cv2.EVENT_LBUTTONUP:
            self.img=self.img[min(self.Cy,y):max(self.Cy,y),min(self.Cx,x):max(self.Cx,x)]
            self.img2=self.img2[min(self.Cy,y):max(self.Cy,y),min(self.Cx,x):max(self.Cx,x)]
            cv2.imshow("win2",self.img)
            self.width=int(abs(x-self.Cx))
            self.height=int(abs(y-self.Cy))
            cv2.setMouseCallback("win2",self.finish)

    def options(self,event):
        my_option=self.window.options.curselection()[0]
        if(my_option==0):
            self.img=cv2.blur(self.img,(10, 10))
            self.img2=cv2.blur(self.img,(10, 10))
            cv2.imshow("win2",self.img)
            return
        if(my_option==1):
            dim = (int(self.width*1.3), self.height)
            self.img=cv2.resize(self.img,dim)
            self.img2=cv2.resize(self.img2,dim)
            self.img=self.img[0:self.height,int(self.width*1.3*0.12):int(self.width*1.3*0.12)+self.width]
            self.img2=self.img2[0:self.height,int(self.width*1.3*0.12):int(self.width*1.3*0.12)+self.width]
            cv2.imshow("win2",self.img)
            return
        if(my_option==2):
            self.img=self.img[self.bordersize:(self.height-self.bordersize),self.bordersize:(self.width-self.bordersize)]
            self.img2=self.img2[self.bordersize:(self.height-self.bordersize),self.bordersize:(self.width-self.bordersize)]
            self.width -= (2 * self.bordersize)
            self.height-= (2 * self.bordersize)
            cv2.imshow("win2",self.img)
            self.bordersize =random.randint(0,20)
            self.img = cv2.copyMakeBorder(
                self.img,
                top=self.bordersize,
                bottom=self.bordersize,
                left=self.bordersize,
                right=self.bordersize,
                borderType=cv2.BORDER_CONSTANT,
                value=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            )
            self.img2 = cv2.copyMakeBorder(
                self.img,
                top=self.bordersize,
                bottom=self.bordersize,
                left=self.bordersize,
                right=self.bordersize,
                borderType=cv2.BORDER_CONSTANT,
                value=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
            )
            self.width+=(2*self.bordersize)
            self.height+=(2*self.bordersize)
            cv2.imshow("win2",self.img)
            return

    def original(self,event):
        self.img = cv2.imread(self.path)
        self.img2 = cv2.imread(self.path)
        cv2.imshow("win2", self.img)
        self.height, self.width, self.channels = self.img.shape
        return

    def chRand(self,event,x,y,flags,param):
        if(event==cv2.EVENT_RBUTTONDOWN):
            p=random.randint(0,3)
            print(p)
            if(p!=3):
                rows = self.img.shape[0]
                cols = self.img.shape[1]
                for i in range(0, rows):
                    for j in range(0, cols):
                        self.img.itemset((i, j, p), self.img2.item(i, j, p)+10)
                        self.img.itemset((i, j, (p-1)%3),0)
                        self.img.itemset((i, j, (p-2)%3),0)
            else:
                self.img=self.img2.copy()
            cv2.imshow("win2",self.img)

    def finish(self,event,x,y,flags,param):
        cv2.setMouseCallback("win2",self.chRand)
        pass

    def imNameIn(self,event):
        self.window.imName.delete(0,END)
        self.window.imName["fg"]='black'
        self.window.imName["font"]=('Arial 10')

    def imNameOut(self,event):
        self.window.imName["fg"]='gray'
        self.window.imName["font"]=('Arial 10 italic')
        self.window.imName.insert(0,"name the image")

    def save(self,event):
        name=self.window.imName.get()
        if(name=="" or self.window.imName["fg"]=="gray"):
            messagebox.showerror(title="save",message="name the new image")
            self.window.imName.focus()
        else:
            cv2.imwrite(name+".jpg",self.img)
            exit(1)

