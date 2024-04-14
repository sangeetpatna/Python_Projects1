from tkinter import *

calc=Tk()
calc.geometry("306x500")
calc.title("Two_num_Calc")
calc.resizable(0,0)
calc.config(background='silver')

digit=StringVar()
fn=""
sn=""
osign="" 

def btnClick(num):
    digit.set(digit.get()+num)
    
def clear():
    digit.set(" ")
    
def ce():
    global sn
    sn=digit.get()
    digit.set(" ") 
    
def pn():
    global fn,sn
    fn=digit.get()
    sn=digit.get()
    digit.set(float(fn)*(-1))
    digit.set(float(sn)*(-1))
    
def operator(op):
    global fn,osign
    fn=digit.get()
    digit.set(" ")
    osign=op
    
def percent():
    global fn,sn,osign
    sn=digit.get()
    if osign=="x":
        digit.set((float(fn))*(float(sn))/100)
        
    else:
        fn=digit.get()
        digit.set((float(fn)/100))   

def res():
    global fn,sn,osign
    sn=digit.get()
    if osign=='+':
        digit.set((float(fn))+(float(sn)))
    elif osign=='-':
        digit.set((float(fn))-(float(sn)))
    elif osign=='x':
        digit.set((float(fn))*(float(sn)))
    elif osign=='÷':
        digit.set((float(fn))/(float(sn)))
    elif osign=="X²":
        digit.set((float(fn))**2)
    elif osign=="X³":
        digit.set((float(fn))**3)
    elif osign=='1/X':
        digit.set(1/float(fn))
    elif osign=='√':
        digit.set(float(fn)**0.5)

label1=Label(calc,text="Basic Calculator",font=("algerian",15),fg="maroon",bg="silver")
label1.place(x=10,y=10)
e1=Entry(calc,font=("algerian",24,"bold"),bg="black",fg="skyblue",bd="8",width=14,textvariable=digit)
butdel=Button(calc,text="X³",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=lambda:operator("X³"))
butdel.place(x=240,y=110)
e1.place(x=5,y=55)
butper=Button(calc,text="%",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=percent)
butper.place(x=3,y=110)
butce=Button(calc,text="CE",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=ce)
butce.place(x=82,y=110)
butc=Button(calc,text="C",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=clear)
butc.place(x=161,y=110)
but1x=Button(calc,text="1/X",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:operator("1/X"))
butx2=Button(calc,text="X²",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:operator("X²"))
but1x.place(x=3,y=175)
butxsq=Button(calc,text="√X",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:operator("√"))
butxsq.place(x=161,y=175)
butdiv=Button(calc,text="÷",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=lambda:operator("÷"))
butdiv.place(x=240,y=175 )
butmul=Button(calc,text="x",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=lambda:operator("x"))
butmul.place(x=240,y=240)
butsub=Button(calc,text="-",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=lambda:operator("-"))
butsub.place(x=240,y=305)
butx2.place(x=82,y=175)
butpl=Button(calc,text="+",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=lambda:operator("+"))
butpl.place(x=240,y=370)
buteq=Button(calc,text="=",font=24,fg="maroon",bg="silver",bd="2",height=2,width=5,command=res)
buteq.place(x=240,y=435)
butpm=Button(calc,text="+/-",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=pn)
butpm.place(x=3,y=435)
but0=Button(calc,text="0",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("0"))
but0.place(x=82,y=435)
butdec=Button(calc,text=".",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("."))
butdec.place(x=161,y=435)
but1=Button(calc,text="1",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("1"))
but1.place(x=3,y=370)
but2=Button(calc,text="2",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("2"))
but2.place(x=82,y=370)
but3=Button(calc,text="3",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("3"))
but3.place(x=161,y=370)
but4=Button(calc,text="4",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("4"))
but4.place(x=3,y=305)
but5=Button(calc,text="5",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("5"))
but5.place(x=82,y=305)
but6=Button(calc,text="6",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("6"))
but6.place(x=161,y=305)
but7=Button(calc,text="7",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("7"))
but7.place(x=3,y=240)
but8=Button(calc,text="8",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("8"))
but8.place(x=82,y=240)
but9=Button(calc,text="9",font=24,fg="maroon",bg="silver",bd="2",height=2,width=6,command=lambda:btnClick("9"))
but9.place(x=161,y=240)
calc.mainloop()