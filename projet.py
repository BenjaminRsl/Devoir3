from tkinter import *
import random
import math
import copy

fen1 = Tk()


def printer():
    for i in range(0,taille):
        for j in range(0,taille):
            print(" ",M[i,j], end='')
        print("\n")  
        

def creation_auto():
    dejavu=[]
    MAX=math.floor(taille * taille *pourcentage)
    for k in range(0, MAX) :
        x=random.randrange(0,taille)
        y=random.randrange(0,taille)
        while (x,y) in dejavu:
            x=random.randrange(0,taille)
            y=random.randrange(0,taille)
        dejavu.append((x,y))
        can1.create_rectangle(x*c, y*c, x*c+c, y*c+c, fill='red')
        M[y,x]=1


def initialiser():
    i=0
    while i!= taille:
        j=0
        while j!= taille:
            M[i,j]=0
            j+=1
        i+=1

def damier(): 
    ligne_vert()
    ligne_hor()
    

        
def ligne_vert():
    x = 0
    while x != taille+1:
        can1.create_line(x*c,0,x*c,taille*c,width=1,fill='black')
        x+=1
        
def ligne_hor():
    y = 0
    while y != taille+1:
        can1.create_line(0,y*c,taille*c,y*c,width=1,fill='black')
        y+=1


def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au M
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    if (x<taille*c and y< taille*c):
        can1.create_rectangle(x, y, x+c, y+c, fill='red')
        M[y/c,x/c]=1

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au M
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    M[y/c,x/c]=0


def updatedamier ():
    global taille,pourcentage, vitesse
    global c
    vitesse=int(s3.get())
    taille=int( s1.get() )
    pourcentage = int(s2.get())/100
    c=math.floor(85*10/taille)
    can1.delete("all")
    damier()
    initialiser()
    creation_auto()

def go():
    global flag
    if flag ==0:
        flag =1
        generation_suivante()
        
def stop():
    global flag    
    flag =0
    
def nbvoisin(i,j):
    hd=M[(i-1+taille)%taille,(j+1)%taille]
    h=M[(i-1+taille)%taille,j]
    hg=M[(i-1+taille)%taille,(j-1+taille)%taille]
    g=M[i,(j-1+taille)%taille]
    d=M[i,(j+1)%taille]
    bg=M[(i+1)%taille,(j-1+taille)%taille]
    b=M[(i+1)%taille,j]
    bd=M[(i+1)%taille,(j+1)%taille]
    nb=hd+h+hg+g+d+bg+b+bd
    return nb


def generation_suivante():
    global M,N
    i=0
    while i!= taille:
        j=0
        while j!= taille:
            nb=nbvoisin(i,j)
            if(M[i,j]==1):
                if((nb==2) or (nb==3)):
                    N[i,j]=1
                else:
                    N[i,j]=0
            else: 
                if(nb==3):
                    N[i,j]=1
                else:
                    N[i,j]=0
            j+=1
        i+=1
    afficher()
    M=copy.deepcopy(N)
    if flag >0:
        fen1.after(vitesse,generation_suivante)

def afficher(): #fonction redessinant le tableau à partir de dico_etat
    can1.delete("ALL")
    damier()
    i=0
    while i!= taille:
        j=0
        while j!= taille:
            y=i*c
            x=j*c
            if (M[i,j]==1):
                can1.create_rectangle(x, y, x+c, y+c, fill='red')
            elif (M[i,j]==0):
                can1.create_rectangle(x, y, x+c, y+c, fill='white')
            j+=1
        i+=1
        
    
#les différentes variables:



#taille des cellules
c = 28


# taille de la grille

taille = 30

# pourcentage d'occupation

pourcentage=0

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50


flag=0

M = {}
N={}


initialiser();

can1 = Canvas(fen1, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack( expand = YES, fill = BOTH )
can1.master.title( "Scale" )
can1.master.geometry( "1010x850" )

damier()


b1 = Button(fen1, text ='Lancer', relief=RAISED,width=20,height=2, fg="dodger blue", command =go)
b2 = Button(fen1, text ='Stoper',relief=RAISED,width=20,height=2,fg="dodger blue", command =stop)
b3 = Button(fen1, text ='Initialiser',relief=RAISED,width=20,height=2,fg="dodger blue", command =updatedamier)
b4 = Button(fen1, text ='Quitter',relief=RAISED,width=20,height=2,fg="dodger blue", command =fen1.destroy)

s1=Scale( fen1, from_ = 5, to =85, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Taille (en nombre de case)' )
s2=Scale( fen1, from_ = 0, to =80, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Nombre de cellule (en %)' )
s3=Scale( fen1, from_ = 400, to =2000, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150, label='Fréquence (en ms)' )


b4.place(x=855, y=0)
s1.place(x=855, y=100)
s2.place(x=855, y=170)
s3.place(x=855, y=240)

b1.place(x=855, y=780)
b2.place(x=855, y=740)
b3.place(x=855, y=700)



fen1.mainloop()
