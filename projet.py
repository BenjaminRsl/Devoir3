from tkinter import *
import random
import math


def creation_auto():
    dejavu=[]
    MAX=math.floor(taille/c * taille/c *pourcentage)
    print(MAX)
    for k in range(0, MAX) :
        x=random.randrange(0,taille/c)*c
        y=random.randrange(0,taille/c)*c
        while (x,y) in dejavu:
            x=random.randrange(0,taille/c)*c
            y=random.randrange(0,taille/c)*c
        dejavu.append((x,y))
        can1.create_rectangle(x, y, x+c, y+c, fill='black')
        dico_case[x,y]=1

def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global vitesse
    vitesse = int(eval(scale.get()))
    print(vitesse)

def initialiser():
    i=0
    while i!= taille/c: #assigne une valeur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte ^^)
        j=0
        while j!= taille/c:
            x=i*c
            y=j*c
            dico_case[x,y]=0
            j+=1
        i+=1

def damier(): 
    ligne_vert()
    ligne_hor()
    initialiser()
    creation_auto()
    #change_vit()
        
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

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='black')
    dico_case[x,y]=1

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0


def updatedamier ():
    global taille,pourcentage
    global c
    case=float( s1.get() )
    pourcentage = int(s2.get())/100
    c=math.floor(85*10/case)
    taille =case* c
    print(c)
    print(pourcentage)
    can1.delete("all")
    damier()

def go():
    "démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        play()
        
def stop():
    "arrêt de l'animation"
    global flag    
    flag =0
    
def play(): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
    global flag, vitesse
    v=0
    while v!= taille/c:
        w=0
        while w!= taille/c:
            x=v*c
            y=w*c
            
            # cas spéciaux:
            # les coins
            if x==0 and y==0: #coin en haut à gauche
                compt_viv=0
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==0 and y==int(taille-c): #coin en bas à gauche
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(taille-c) and y==0: #coin en haut à droite
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(taille-c) and y==int(taille-c): #coin en bas à droite
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            # cas spéciaux:
            # les bords du tableau (sans les coins)    
            elif x==0 and 0<y<int(taille-c): # bord de gauche
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(taille-c) and 0<y<int(taille-c): # bord de droite
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(taille-c) and y==0: # bord du haut
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(taille-c) and y==int(taille-c): # bord du bas
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            #cas généraux
            #les cellules qui ne sont pas dans les bords du tableau
            else:
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            w+=1
        v+=1
    redessiner()
    if flag >0: 
        fen1.after(vitesse,play)

        

def redessiner(): #fonction redessinant le tableau à partir de dico_etat
    can1.delete(ALL)
    damier()
    t=0
    while t!= taille/c:
        u=0
        while u!= taille/c:
            x=t*c
            y=u*c
            if dico_etat[x,y]==3:
                dico_case[x,y]=1
                can1.create_rectangle(x, y, x+c, y+c, fill='black')
            elif dico_etat[x,y]==2:
                if dico_case[x,y]==1:
                    can1.create_rectangle(x, y, x+c, y+c, fill='black')
                else:
                    can1.create_rectangle(x, y, x+c, y+c, fill='white')
            elif dico_etat[x,y]<2 or dico_etat[x,y]>3:
                dico_case[x,y]=0
                can1.create_rectangle(x, y, x+c, y+c, fill='white')
            u+=1
        t+=1
        
    
#les différentes variables:



#taille des cellules
c = 12


# taille de la grille

taille = 70*c# pourcentage d'occupation

pourcentage=0.2

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50


flag=0
dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes

initialiser();
#programme "principal" 
fen1 = Tk()

can1 = Canvas(fen1, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack( expand = YES, fill = BOTH )
can1.master.title( "Scale" )
can1.master.geometry( "220x270" )

damier()


b1 = Button(fen1, text ='Go!', command =go)
b2 = Button(fen1, text ='Stop', command =stop)
b3 = Button(fen1, text ='Initialiser', command =updatedamier)
#b4 = Button(fen1, text ='Random', command =creation_auto)

s1=Scale( fen1, from_ = 30, to =85, orient = HORIZONTAL )
s2=Scale( fen1, from_ = 20, to =80, orient = HORIZONTAL )
s1.pack( side =LEFT, fill = X )
s2.pack( side =LEFT, fill = X )
b1.pack(side =LEFT)
b2.pack(side =LEFT)
b3.pack(side =LEFT)
#b4.pack(side =LEFT)



fen1.mainloop()
