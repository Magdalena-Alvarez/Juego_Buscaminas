# -*- coding: cp1252 -*-
from tkinter import*
from random import *
def verificarBombas(x):
    global tablero
    cb=0
    if tablero[x-1]=='x' and x!=13 and x!=19 and x!=25 and x!= 7:
        cb+=1
    if  x!=30 and x!=6 and x!=12 and x!=18 and x!= 24 and tablero[x+1]=='x':
        cb+=1
    if (x not in range(25,31))and tablero[x+6]=='x':
        cb+=1
    if (x not in range(1,7)) and tablero[x-6]=='x':
        cb+=1
    if (x not in range(1,7))and x!=12 and x!=18 and x!= 24 and x!=30 and tablero[x-5]=='x':
        cb+=1
    if (x not in range(1,8)) and x!=13 and x!=19 and x!=25 and tablero[x-7]=='x':
        cb+=1
    if (x not in range(24,31)) and x!=12 and x!=18 and x!=6 and tablero[x+7]=='x':
        cb+=1
    if (x not in range(25,31)) and x!=13 and x!=19 and x!=7 and x!=1 and tablero [x+5]=='x' :
        cb+=1
    return cb

def jugada(x):
    global tablero
    if tablero[x]=='x':
            botones[x-1].config(text='x', bg='red')
            final.config(text='Perdiste, ¿volver a jugar?',font='georgia')
            for i in range(0,30):
                if tablero[i+1]=='x':
                    botones[i].config(text='x',bg='red')
                else:
                    botones[i].config(text=verificarBombas(i+1),fg='blue')
    else:
        a=verificarBombas(x)
       
        if a ==0:
            botones[x-1].config(text=a,bg='gray')
            if x!=13 and x!=19 and x!=25 and x!=7:
                botones[x-2].config(text=verificarBombas(x-1),fg='blue')
            if  x!=30 and x!=6 and x!=12 and x!=18 and x!= 24:
                botones[x].config(text=verificarBombas(x+1),fg='blue')
            if (x not in range(25,31)):
                botones[x+5].config(text=verificarBombas(x+6),fg='blue')
            if (x not in range(1,7)):
                botones[x-7].config(text=verificarBombas(x-6),fg='blue')
            if (x not in range(1,7))and x!=12 and x!=18 and x!= 24 and x!=30:
                botones[x-6].config(text=verificarBombas(x-5),fg='blue')
            if (x not in range(1,8)) and x!=13 and x!=19 and x!=25:
                botones[x-8].config(text=verificarBombas(x-7),fg='blue')
            if (x not in range(24,31)) and x!=12 and x!=18 and x!=6:
                botones[x+6].config(text=verificarBombas(x+7),fg='blue')
            if (x not in range(25,31)) and x!=13 and x!=19 and x!=7 and x!=1:
                botones[x+4].config(text=verificarBombas(x+5),fg='blue')
        else:
             botones[x-1].config(text=a,fg='blue')
def crearTablero():
    global tablero, bombas
    for i in range(0,6):
        bombas[i]=randint(1,30)
    for j in range(0,6):
        for i in range(0,6):
            if i!=j and bombas[i]== bombas[j]:
                bombas[i]=randint(1,30)
    
    for i in range(0,31):
        tablero.append('-')
    for c in range(0,6):
        j=bombas[c]
        tablero[j]= 'x'
    for j in range(1,31):
         if tablero[j]!='x':
             tablero[j]=verificarBombas(j)
    
def reiniciar():
    global tablero, bombas
    for i in range(0,6):
        bombas[i]=0
    tablero=[]
    for i in range(0,6):
        bombas[i]=randint(1,30)
    for j in range(0,6):
        for i in range(0,6):
            if i!=j and bombas[i]== bombas[j]:
                bombas[i]=randint(1,30)
    
    for i in range(0,31):
        tablero.append('-')
    for c in range(0,6):
        j=bombas[c]
        tablero[j]= 'x'
    for j in range(1,31):
         if tablero[j]!='x':
             tablero[j]=verificarBombas(j)
    for i in range(0,30):
            botones[i].config(text='', bg='light gray')
    final.config(text='')
   
ventana=Tk()
ventana.title("MAGDAX'S BUSCAMINAS")
bombas=[0,0,0,0,0,0]
tablero=[]
botones=[]
a=0
crearTablero()
#marcos
marco0=Frame(ventana)
marco1=Frame(ventana)
marco2=Frame(ventana)
marco3=Frame(ventana)
marco4=Frame(ventana)
marco5=Frame(ventana)
marco6=Frame(ventana)
marco7=Frame(ventana)
marco8=Frame(ventana)
marcoF=Frame(ventana)
titulo=Label(marco0,text='BUSCAMINAS',font='arial')
final=Label(marcoF)
#botones
botones=[]
boton1=Button(marco1,command=lambda:jugada(1),width=2, height=1)
botones.append(boton1)
boton2=Button(marco1,command=lambda:jugada(2),width=2, height=1)
botones.append(boton2)
boton3=Button(marco1,command=lambda:jugada(3),width=2, height=1)
botones.append(boton3)
boton4=Button(marco1,command=lambda:jugada(4),width=2, height=1)
botones.append(boton4)
boton5=Button(marco1,command=lambda:jugada(5),width=2, height=1)
botones.append(boton5)
boton6=Button(marco1,command=lambda:jugada(6),width=2, height=1)
botones.append(boton6)
boton7=Button(marco2,command=lambda:jugada(7),width=2, height=1)
botones.append(boton7)
boton8=Button(marco2,command=lambda:jugada(8),width=2, height=1)
botones.append(boton8)
boton9=Button(marco2,command=lambda:jugada(9),width=2, height=1)
botones.append(boton9)
boton10=Button(marco2,command=lambda:jugada(10),width=2, height=1)
botones.append(boton10)
boton11=Button(marco2,command=lambda:jugada(11),width=2, height=1)
botones.append(boton11)
boton12=Button(marco2,command=lambda:jugada(12),width=2, height=1)
botones.append(boton12)
boton13=Button(marco3,command=lambda:jugada(13),width=2, height=1)
botones.append(boton13)
boton14=Button(marco3,command=lambda:jugada(14),width=2, height=1)
botones.append(boton14)
boton15=Button(marco3,command=lambda:jugada(15),width=2, height=1)
botones.append(boton15)
boton16=Button(marco3,command=lambda:jugada(16),width=2, height=1)
botones.append(boton16)
boton17=Button(marco3,command=lambda:jugada(17),width=2, height=1)
botones.append(boton17)
boton18=Button(marco3,command=lambda:jugada(18),width=2, height=1)
botones.append(boton18)
boton19=Button(marco4,command=lambda:jugada(19),width=2, height=1)
botones.append(boton19)
boton20=Button(marco4,command=lambda:jugada(20),width=2, height=1)
botones.append(boton20)
boton21=Button(marco4,command=lambda:jugada(21),width=2, height=1)
botones.append(boton21)
boton22=Button(marco4,command=lambda:jugada(22),width=2, height=1)
botones.append(boton22)
boton23=Button(marco4,command=lambda:jugada(23),width=2, height=1)
botones.append(boton23)
boton24=Button(marco4,command=lambda:jugada(24),width=2, height=1)
botones.append(boton24)
boton25=Button(marco5,command=lambda:jugada(25),width=2, height=1)
botones.append(boton25)
boton26=Button(marco5,command=lambda:jugada(26),width=2, height=1)
botones.append(boton26)
boton27=Button(marco5,command=lambda:jugada(27),width=2, height=1)
botones.append(boton27)
boton28=Button(marco5,command=lambda:jugada(28),width=2, height=1)
botones.append(boton28)
boton29=Button(marco5,command=lambda:jugada(29),width=2, height=1)
botones.append(boton29)
boton30=Button(marco5,command=lambda:jugada(30),width=2, height=1)
botones.append(boton30)
boton31=Button(marco6,command=lambda:jugada(31),width=2, height=1)
botones.append(boton31)
reinicio=Button(marco6,text='Volver a jugar',command=reiniciar)

for a in range(0,30):
    botones[a].config(bg='light gray')
#marco0
marco0.pack()
titulo.pack()

#marco1
marco1.pack()
boton1.pack(side=LEFT)
boton2.pack(side=LEFT)
boton3.pack(side=LEFT)
boton4.pack(side=LEFT)
boton5.pack(side=LEFT)
boton6.pack(side=LEFT)
#marco2
marco2.pack()
boton7.pack(side=LEFT)
boton8.pack(side=LEFT)
boton9.pack(side=LEFT)
boton10.pack(side=LEFT)
boton11.pack(side=LEFT)
boton12.pack(side=LEFT)
#marco3
marco3.pack()
boton13.pack(side=LEFT)
boton14.pack(side=LEFT)
boton15.pack(side=LEFT)
boton16.pack(side=LEFT)
boton17.pack(side=LEFT)
boton18.pack(side=LEFT)
#marco4
marco4.pack()
boton19.pack(side=LEFT)
boton20.pack(side=LEFT)
boton21.pack(side=LEFT)
boton22.pack(side=LEFT)
boton23.pack(side=LEFT)
boton24.pack(side=LEFT)
#marco5
marco5.pack()
boton25.pack(side=LEFT)
boton26.pack(side=LEFT)
boton27.pack(side=LEFT)
boton28.pack(side=LEFT)
boton29.pack(side=LEFT)
boton30.pack(side=LEFT)
#marco6
marco6.pack()
reinicio.pack()
#marco7

#marco8

#marcoF
marcoF.pack()
final.pack()
ventana.mainloop()
