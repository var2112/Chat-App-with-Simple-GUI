"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import *
from tkinter import font
from functools import partial


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg = str(msg)
            sender = msg.split(':')
            sender_msg = sender[0]
            Text.name_init(sender_msg)
           
            if Text.user == sender_msg:  
              Text.textbox(msg)
             
            else:
                 Text.textbox_recv(msg)
        except OSError:  
            break


def send(event=None):  
    """Handles sending of messages."""
    msg = e11.get()
    e11.set("")  
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    e11.set("{quit}")
    send()

class Text:
    x = 35 
    y = 75
    x1 = 20
    y1 = 75
    x2 = 370
    counter_recv = 0
    counter = 0
    user = ""
    n = 0
    called = False
    def __init__(self,canvas):
        self.canvas = canvas


    @classmethod
    def textbox(cls,msg):   
        cls.counter += 1
        cls.y += 22 
        chat = msg 
        desired_font = font.Font( family = "Arial Baltic",size = 10)      
        text_item = canvas.create_text(Text.x,cls.y,tags = "drag_tb",anchor = SW,text = chat , font = desired_font)
        bbox = canvas.bbox(text_item)
        rect_item = canvas.create_rectangle(bbox,tags="drag_tb",outline="#008ae6", fill="#ccf2ff")
        canvas.tag_raise(text_item,rect_item)
        canvas.scale("drag_tb",cls.x1,cls.y,1.0,1.0)
    
        
    @classmethod
    def textbox_recv(cls,msg):
        cls.counter_recv += 1
        cls.y += 22
        chat = msg
        desired_font = font.Font( family = "Arial Baltic",size = 10)     
        text_item = canvas.create_text(Text.x2,cls.y,tags = "drag_tb2",anchor = NE,text = chat , font = desired_font)
        bbox = canvas.bbox(text_item)
        rect_item = canvas.create_rectangle(bbox,tags="drag_tb2",outline="#001a00", fill="#e6ffe6")
        canvas.tag_raise(text_item,rect_item)
        canvas.scale("drag_tb2",cls.x1,cls.y,1.0,1.0)

    @classmethod
    def name_init(cls,sender):
        if cls.called:
            pass
        else:
            Text.user = sender
            cls.called = True
            return

        
root = Tk()
root.geometry("600x650")

import tkinter.font as tkFont
import emoji

class smile:
    def emo1(self):
        d1 = e11.get() + ("\N{grinning face}")
        e11.set(d1)
    def emo2(self):
        d2 = e11.get() + ("\N{slightly smiling face}")
        e11.set(d2)
    def emo3(self):
        d3 = e11.get() + ("\N{winking face}")
        e11.set(d3)
    def emo4(self):
        d4 = e11.get() + ("\N{rolling on the floor laughing}")
        e11.set(d4)
    def emo5(self):
        d5 = e11.get() + ("\N{face with tears of joy}")
        e11.set(d5)
    def emo6(self):
        d6 = e11.get() + ("\N{smiling face with smiling eyes}")
        e11.set(d6)
    def emo7(self):
        d7 = e11.get() + ("\N{upside-down face}")
        e11.set(d7)
    def emo8(self):
        d8 = e11.get() + ("\N{grinning face with smiling eyes}")
        e11.set(d8)
    def emo9(self):
        d9 = e11.get() + ("\N{smiling face with halo}")
        e11.set(d9)
    def emo10(self):
        d10 = e11.get() + ("\N{kissing face}")
        e11.set(d10)
    def emo11(self):
        d11 = e11.get() + ("\N{kissing face with closed eyes}")
        e11.set(d11)
    def emo12(self):
        d12 = e11.get() + ("\N{kissing face with smiling eyes}")
        e11.set(d12)
    def emo13(self):
        d13 = e11.get() + ("\N{money-mouth face}")
        e11.set(d13)
    def emo14(self):
        d14 = e11.get() + ("\N{hugging face}")
        e11.set(d14)
    def emo15(self):
        d15 = e11.get() + ("\N{thinking face}")
        e11.set(d15)
    def emo16(self):
        d16 = e11.get() + ("\N{zipper-mouth face}")
        e11.set(d16)
    def emo17(self):
        d17 = e11.get() + ("\N{neutral face}")
        e11.set(d17)
    def emo18(self):
        d18 = e11.get() + ("\N{expressionless face}")
        e11.set(d18)
    def emo19(self):
        d19 = e11.get() + ("\N{face without mouth}")
        e11.set(d19)
    def emo20(self):
        d20 = e11.get() + ("\N{smirking face}")
        e11.set(d20)
    def emo21(self):
        d21 = e11.get() + ("\N{unamused face}")
        e11.set(d21)
    def emo22(self):
        d22 = e11.get() + ("\N{face with rolling eyes}")
        e11.set(d22)
    def emo23(self):
        d23 = e11.get() + ("\N{grimacing face}")
        e11.set(d23)
    def emo24(self):
        d24 = e11.get() + ("\N{lying face}")
        e11.set(d24)
    def emo25(self):
        d25 = e11.get() + ("\N{relieved face}")
        e11.set(d25)
    def emo26(self):
        d26 = e11.get() + ("\N{pensive face}")
        e11.set(d26)
    def emo27(self):
        d27 = e11.get() + ("\N{sleepy face}")
        e11.set(d27)
    def emo28(self):
        d28 = e11.get() + ("\N{drooling face}")
        e11.set(d28)
    def emo29(self):
        d29 = e11.get() + ("\N{sleeping face}")
        e11.set(d29)
    def emo30(self):
        d30 = e11.get() + ("\N{face with medical mask}")
        e11.set(d30)
    def emo31(self):
        d31 = e11.get() + ("\N{face with thermometer}")
        e11.set(d31)
    def emo32(self):
        d32 = e11.get() + ("\N{face with head-bandage}")
        e11.set(d32)
    def emo33(self):
        d33 = e11.get() + ("\N{nauseated face}")
        e11.set(d33)

def emoji():
    emo = Tk()
    emo.title("EMOJI")
    emo.configure(bg="black")
    emo.geometry("300x420")
    emo.resizable(0,0)
    e = smile()
    Button(emo,text=("\N{grinning face}"),command=e.emo1,font = tkFont.Font(size=20),bg="white").place(x=10,y=10)
    Button(emo,text=("\N{slightly smiling face}"),command=e.emo2,font = tkFont.Font(size=20),bg="white").place(x=70,y=10)
    Button(emo,text=("\N{winking face}"),command=e.emo3,font = tkFont.Font(size=20),bg="white").place(x=130,y=10)
    Button(emo,text=("\N{rolling on the floor laughing}"),command=e.emo4,font = tkFont.Font(size=20),bg="white").place(x=190,y=10)
    Button(emo,text=("\N{face with tears of joy}"),command=e.emo5,font = tkFont.Font(size=20),bg="white").place(x=250,y=10)
    Button(emo,text=("\N{smiling face with smiling eyes}"),command=e.emo6,font = tkFont.Font(size=20),bg="white").place(x=10,y=70)
    Button(emo,text=("\N{upside-down face}"),command=e.emo7,font = tkFont.Font(size=20),bg="white").place(x=70,y=70)
    Button(emo,text=("\N{grinning face with smiling eyes}"),command=e.emo8,font = tkFont.Font(size=20),bg="white").place(x=130,y=70)
    Button(emo,text=("\N{smiling face with halo}"),command=e.emo9,font = tkFont.Font(size=20),bg="white").place(x=190,y=70)
    Button(emo,text=("\N{kissing face}"),command=e.emo10,font = tkFont.Font(size=20),bg="white").place(x=250,y=70)
    Button(emo,text=("\N{kissing face with closed eyes}"),command=e.emo11,font = tkFont.Font(size=20),bg="white").place(x=10,y=130)
    Button(emo,text=("\N{kissing face with smiling eyes}"),command=e.emo12,font = tkFont.Font(size=20),bg="white").place(x=70,y=130)
    Button(emo,text=("\N{money-mouth face}"),command=e.emo13,font = tkFont.Font(size=20),bg="white").place(x=130,y=130)
    Button(emo,text=("\N{hugging face}"),command=e.emo14,font = tkFont.Font(size=20),bg="white").place(x=190,y=130)
    Button(emo,text=("\N{thinking face}"),command=e.emo15,font = tkFont.Font(size=20),bg="white").place(x=250,y=130)
    Button(emo,text=("\N{zipper-mouth face}"),command=e.emo16,font = tkFont.Font(size=20),bg="white").place(x=10,y=190)
    Button(emo,text=("\N{neutral face}"),command=e.emo17,font = tkFont.Font(size=20),bg="white").place(x=70,y=190)
    Button(emo,text=("\N{expressionless face}"),command=e.emo18,font = tkFont.Font(size=20),bg="white").place(x=130,y=190)
    Button(emo,text=("\N{face without mouth}"),command=e.emo19,font = tkFont.Font(size=20),bg="white").place(x=190,y=190)
    Button(emo,text=("\N{smirking face}"),command=e.emo20,font = tkFont.Font(size=20),bg="white").place(x=250,y=190)
    Button(emo,text=("\N{unamused face}"),command=e.emo21,font = tkFont.Font(size=20),bg="white").place(x=10,y=250)
    Button(emo,text=("\N{face with rolling eyes}"),command=e.emo22,font = tkFont.Font(size=20),bg="white").place(x=70,y=250)
    Button(emo,text=("\N{grimacing face}"),command=e.emo23,font = tkFont.Font(size=20),bg="white").place(x=130,y=250)
    Button(emo,text=("\N{lying face}"),command=e.emo24,font = tkFont.Font(size=20),bg="white").place(x=190,y=250)
    Button(emo,text=("\N{relieved face}"),command=e.emo25,font = tkFont.Font(size=20),bg="white").place(x=250,y=250)
    Button(emo,text=("\N{pensive face}"),command=e.emo26,font = tkFont.Font(size=20),bg="white").place(x=10,y=310)
    Button(emo,text=("\N{sleepy face}"),command=e.emo27,font = tkFont.Font(size=20),bg="white").place(x=70,y=310)
    Button(emo,text=("\N{drooling face}"),command=e.emo28,font = tkFont.Font(size=20),bg="white").place(x=130,y=310)
    Button(emo,text=("\N{sleeping face}"),command=e.emo29,font = tkFont.Font(size=20),bg="white").place(x=190,y=310)
    Button(emo,text=("\N{face with medical mask}"),command=e.emo30,font = tkFont.Font(size=20),bg="white").place(x=250,y=310)
    Button(emo,text=("\N{face with thermometer}"),command=e.emo31,font = tkFont.Font(size=20),bg="white").place(x=10,y=370)
    Button(emo,text=("\N{face with head-bandage}"),command=e.emo32,font = tkFont.Font(size=20),bg="white").place(x=70,y=370)
    Button(emo,text=("\N{nauseated face}"),command=e.emo33,font = tkFont.Font(size=20),bg="white").place(x=130,y=370)
    Button(emo,text="Quit",command=emo.destroy,font = tkFont.Font(size=20),bg="white").place(x=190,y=370)
    emo.mainloop()


vscrollbar = Scrollbar(root)
vscrollbar.pack(side=RIGHT, fill=Y)

canvas = Canvas(root,width=400,height=600,bg="white")
canvas.pack()
vscrollbar.config(command=canvas.yview)

r1 =  canvas.create_rectangle(0,600,450,530,fill="#0B5345")
canvas.move(r1,0,-550)
e11 = StringVar()
e1 = Entry(root,textvariable=e11)
e1.pack()
t1 = Text(canvas)

b1 = Button(root,text="Send",command =send) 
b1.pack()
emoji_button = Button(root,text=("\N{slightly smiling face}"),command=emoji,bg="white",font = tkFont.Font(size=15)).place(x=400,y=600)
#emoji_button.place(x=320,y=340)
quit_button = Button(root, text="Quit", command=root.destroy,bg="white",font = tkFont.Font(size=15)).place(x=500,y=600)
#quit_button.place(x=380,y=390)

root.update()

canvas.config(scrollregion=(0,0,10000,10000))

HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
root.mainloop()
