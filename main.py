from tkinter import *
import cv2
from numba.cuda import selp
from pandas.io.stata import _maybe_convert_to_int_keys
from tkinter.filedialog import askopenfilename
import pic


class my_window():
    def __init__(self,wind):
        self.window=wind
        self.cvwindow=pic.picture(self,"a.jpg")
        self.chPictue = Button(self.window, text="choose a picture", fg='blue',bg='white')
        self.note=Label(self.window,text="note! to change the picture color by random, click the right button on the picture",fg='red',bg='white')
        self.lb = Label(self.window, text="choose picture size",bg='white',font="Arial 9 bold")
        self.Lsize = Listbox(self.window, height=3,bg='white')
        self.lb2=Label(self.window,text="choose picture color",bg='white',font="Arial 9 bold")
        self.v=StringVar()
        self.r1 = Radiobutton(self.window, text="special", variable=self.v, valu="var1",bg='white')
        self.r2 = Radiobutton(self.window, text="paint red", variable=self.v, valu="var2",bg='white')
        self.r3 = Radiobutton(self.window, text="paint blue", variable=self.v, valu="var3",bg='white')
        self.r4 = Radiobutton(self.window, text="gray", variable=self.v, valu="gray",bg='white')
        self.cutPictue=Button(self.window,text="cut your picture",fg='blue',bg='white')
        self.lb3=Label(self.window,text="insert a text",bg='white',font="Arial 9 bold")
        self.txt=Entry(self.window,bg='white')
        self.txt.focus()
        self.txtAdd=Button(self.window,text="Add",fg='blue',bg='white')
        self.lb4=Label(self.window,text="choose a shape to draw",bg='white',font="Arial 9 bold")
        self.shape=Listbox(self.window,height=3,bg='white')
        self.lb5=Label(self.window,text="other options",bg='white',font="Arial 9 bold")
        self.options=Listbox(self.window,height=4,bg='white')
        self.saveBtn=Button(self.window,text="save changes", fg='red',bg='white',width=15)
        self.imName=Entry(self.window,font=('Arial 10 italic'),fg='gray',bg='white',width=15)
        self.resetBtm=Button(self.window,text="original pictue", fg='red',bg='white')
        self.__fullDetails()
        self.__position()
        self.__events()

    def __events(self):
        self.resetBtm.bind('<Button-1>',self.cvwindow.original)
        self.saveBtn.bind('<Button-1>',self.cvwindow.save)
        self.txtAdd.bind('<Button-1>',self.cvwindow.addTxt)
        self.r1["command"]=self.cvwindow.chColor
        self.r2["command"]=self.cvwindow.chColor
        self.r3["command"]=self.cvwindow.chColor
        self.r4["command"]=self.cvwindow.chColor
        self.chPictue.bind('<Button-1>',self.__choosePic)
        self.Lsize.bind('<<ListboxSelect>>', self.cvwindow.chSize)
        self.shape.bind('<<ListboxSelect>>',self.cvwindow.draw)
        self.cutPictue.bind('<Button-1>',self.__cut)
        self.options.bind('<<ListboxSelect>>',self.cvwindow.options)
        self.imName.bind('<FocusIn>',self.cvwindow.imNameIn)
        self.imName.bind('<FocusOut>',self.cvwindow.imNameOut)

    def __cut(self,event):
        cv2.setMouseCallback("win2",self.cvwindow.cutPic)

    def __choosePic(self,event):
        r=Tk()
        r.withdraw()
        file_name = askopenfilename()
        if(file_name!=""):
            cv2.destroyWindow("win2")
            self.cvwindow=pic.picture(self,file_name)
            self.__events()
        return

    def __fullDetails(self):
        self.window.title('picture editor')
        self.Lsize.insert(1, "0.5")
        self.Lsize.insert(2, "1.2")
        self.Lsize.insert(3, "1.5")
        self.v.set("red")
        self.shape.insert(1, "circle")
        self.shape.insert(2, "square")
        self.shape.insert(3, "X")
        self.options.insert(1, "non-clear")
        self.options.insert(2, "streched")
        self.options.insert(3, "framed")
        self.options.insert(4, "")
        self.options.insert(5, "")
        self.imName.insert(0,"name the image")



    def __position(self):
        self.window.geometry("600x500+400+200")
        self.chPictue.place(x=50,y=50)
        self.note.place(x=50, y=365)
        self.lb.place(x=50, y=100)
        self.Lsize.place(x=50, y=120)
        self.lb2.place(x=50,y=250)
        self.r1.place(x=50,y=280)
        self.r2.place(x=50,y=300)
        self.r3.place(x=50,y=320)
        self.r4.place(x=50,y=340)
        self.cutPictue.place(x=480,y=120)
        self.lb3.place(x=345,y=100)
        self.txt.place(x=345,y=122)
        self.txtAdd.place(x=345,y=180)
        self.lb4.place(x=190,y=100)
        self.shape.place(x=190,y=120)
        self.lb5.place(x=200,y=250)
        self.options.place(x=200,y=280)
        self.saveBtn.place(x=430,y=450)
        self.imName.place(x=430,y=420)
        self.resetBtm.place(x=490,y=320)


win=Tk()

win["bg"]='white'
my_wind=my_window(win)
win.mainloop()
