from tkinter import *
global G,M,P,en
G=0
P=0
M=0
def inicio():
    B1=Button(ventana,text="GRANDE",command=A,state="disable",bg="black").grid(column=1,row=1)
    B2=Button(ventana,text="MEDIANA",command=B,state="disable",bg="black").grid(column=2,row=1)
    B3=Button(ventana,text="PEQUEÑA",command=C,state="disable",bg="black").grid(column=3,row=1)
    B4=Button(ventana,text="CUENTA",command=D,state="disable",bg="black").grid(column=4,row=1)
    B5=Button(ventana,text="Apagar",command=lambda:Encen(1),state="disable",bg="black").grid(column=5,row=0)
    B6=Button(ventana,text="encender",command=lambda:Encen(0),bg="RED").grid(column=1,row=0)
    global G,M,P,en
    G=0
    P=0
    M=0
      

def Encen (num):
    global en
    en=num
    E()
def A ():
    global G
    G=G+1
def B ():
    global M
    M=M+1
def C ():
    global P
    P=P+1
def D ():
    global P,G,M
    l=Label(ventana,text="El total de MEDIANAS es:"+str(M)).grid(column=0,row=2) 
    l=Label(ventana,text="El total de GRANDES es:"+str(G)).grid(column=0,row=3)
    l=Label(ventana,text="El total de PEQUEÑAS es:"+str(P)).grid(column=0,row=4)
def E ():
        if(en==0):
            B1=Button(ventana,text="GRANDE",command=A).grid(column=1,row=1)
            B2=Button(ventana,text="MEDIANA",command=B).grid(column=2,row=1)
            B3=Button(ventana,text="PEQUEÑA",command=C).grid(column=3,row=1)
            B4=Button(ventana,text="CUENTA",command=D).grid(column=4,row=1)
            B5=Button(ventana,text="Apagar",command=lambda:Encen(1)).grid(column=5,row=0)
        if(en==1):
            inicio()

        
ventana=Tk()
inicio()
ventana.mainloop()



