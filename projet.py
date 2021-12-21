from tkinter import *
import random
import math

fen1 = Tk()


    

def creation_auto():
    dejavu=[]
    MAX=math.floor(taille/c * taille/c *pourcentage)
    for k in range(0, MAX) :
        x=random.randrange(0,taille/c)*c
        y=random.randrange(0,taille/c)*c
        while (x,y) in dejavu:
            x=random.randrange(0,taille/c)*c
            y=random.randrange(0,taille/c)*c
        dejavu.append((x,y))
        can1.create_rectangle(x, y, x+c, y+c, fill='red')
        M[x,y]=1


def initialiser():
    i=0
    while i!= taille/c:
        j=0
        while j!= taille/c:
            x=i*c
            y=j*c
            M[x,y]=0
            j+=1
        i+=1

def damier(): 
    ligne_vert()
    ligne_hor()
    initialiser()
    creation_auto()

        
def ligne_vert():
    c_x = 0
    while c_x != taille:
        can1.create_line(c_x,0,c_x,taille,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != taille:
        can1.create_line(0,c_y,taille,c_y,width=1,fill='black')
        c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au M
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    if (x<taille and y< taille):
        can1.create_rectangle(x, y, x+c, y+c, fill='red')
        M[x,y]=1

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au M
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    M[x,y]=0


def updatedamier ():
    global taille,pourcentage, vitesse
    global c
    vitesse=int(s3.get())
    case=float( s1.get() )
    pourcentage = int(s2.get())/100
    c=math.floor(85*10/case)
    taille =case* c
    can1.delete("all")
    damier()

def go():
    "démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        generation_suivante()
        
def stop():
    "arrêt de l'animation"
    global flag    
    flag =0
    
def nbvoisin(i,j):
    hd=M[(i-c+taille)%taille,(j+c)%taille]
    h=M[(i-c+taille)%taille,j]
    hg=M[(i-c+taille)%taille,(j-c+taille)%taille]
    g=M[i,(j-c+taille)%taille]
    d=M[i,(j+c)%taille]
    bg=M[(i+c)%taille,(j-c+taille)%taille]
    b=M[(i+c)%taille,j]
    bd=M[(i+c)%taille,(j+c)%taille]
    nb=hd+h+hd+g+d+bg+b+bd
    return nb


def generation_suivante():
    i=0
    while i!= taille/c:
        j=0
        while j!= taille/c:
            x=i*c
            y=j*c
            nb=nbvoisin(x,y)
            if(M[x,y]):
                if((nb==2) or (nb==3)):
                    M[x,y]=1
                elif((nb>2) or (nb==1)):
                    M[x,y]=0
            elif(nb==3):
                M[x,y]=1
               
            j+=1
        i+=1
    afficher()
    if flag >0:
        fen1.after(vitesse,generation_suivante)
       

def afficher(): #fonction redessinant le tableau à partir de dico_etat
    can1.delete("ALL")
    damier()
    i=0
    while i!= taille/c:
        j=0
        while j!= taille/c:
            x=i*c
            y=j*c
            if (M[x,y]==1):
                can1.create_rectangle(x, y, x+c, y+c, fill='red')
            elif (M[x,y]==0):
                can1.create_rectangle(x, y, x+c, y+c, fill='white')
            j+=1
        i+=1
        
    
#les différentes variables:



#taille des cellules
c = 12


# taille de la grille

taille = 70*c# pourcentage d'occupation

pourcentage=0.2

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50


flag=0

M = {} 

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

s1=Scale( fen1, from_ = 30, to =85, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Taille (en nombre de case)' )
s2=Scale( fen1, from_ = 20, to =80, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Nombre de cellule (en %)' )
s3=Scale( fen1, from_ = 40, to =500, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150, label='Fréquence (en ms)' )


b4.place(x=855, y=0)
s1.place(x=855, y=100)
s2.place(x=855, y=170)
s3.place(x=855, y=240)

b1.place(x=855, y=780)
b2.place(x=855, y=740)
b3.place(x=855, y=700)



fen1.mainloop()
