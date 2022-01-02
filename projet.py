from tkinter import *
import random
import math
import copy


############# Variables #############

#taille des cellules
c = 25

# taille de la grille
taille = 25

# pourcentage d'occupation pour le random
pourcentage=0

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50

#coefficient utilise pour l'adaptation de la taille demandé
coeff=c*taille

#draoeau pour savoir si on est en marche ou à l'arrêt
marche=0

#Deux dictionnaires
M = {}
N={}


############# Fonctions #############    
    
#fonction qui rend un pourcentage de cellule vivante
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

#initialisation de toutes les cellules à morte
def initialiser():
    i=0
    while i!= taille:
        j=0
        while j!= taille:
            M[i,j]=0
            j+=1
        i+=1

# crée notre damier
def damier(): 
    ligne_verticale()
    ligne_horizontale()
    

#crée les lignes verticales        
def ligne_verticale():
    x = 0
    while x != taille+1:
        can1.create_line(x*c,0,x*c,taille*c,width=1,fill='black')
        x+=1
  
#crée les lignes horizontale
def ligne_horizontale():
    y = 0
    while y != taille+1:
        can1.create_line(0,y*c,taille*c,y*c,width=1,fill='black')
        y+=1

#fonction d'évenement lorsqu'il y aun click gauche
def click_gauche(event): 
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    if (x<taille*c and y< taille*c):
        can1.create_rectangle(x, y, x+c, y+c, fill='red')
        M[y/c,x/c]=1

#fonction d'évenement lorsqu'il y aun click droit
def click_droit(event): 
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    M[y/c,x/c]=0

#fonction qui réinitialise tout le damier et qui le modifie
def updatedamier ():
    global taille,pourcentage, vitesse
    global c
    vitesse=int(s3.get())
    taille=int( s1.get() )
    pourcentage = int(s2.get())/100
    c=math.floor(coeff/taille)
    can1.delete("all")
    damier()
    initialiser()
    creation_auto()

#fonction qui met en action les générations suivantes
def action():
    global marche
    if marche ==0:
        marche =1
        generation_suivante()

#arret du calcul des générations suivantes        
def stop():
    global marche    
    marche =0
  
#calcul le nombre de voisin pour une cellule de coordonnée (i,j)    
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

#calcul la génération suivante N du dictionnaire M
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

    M=copy.deepcopy(N)
    afficher()
    if marche >0:
        fen1.after(vitesse,generation_suivante)

#affiche notre damier en fonction du dictionnaire M
def afficher(): 
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
  
        
############## Fonction principale ##############

#initialisation du dictionnaire M
initialiser();

#création de la fenètre principale
fen1 = Tk()
fen1.title( "Devoir 3" )
fen1.geometry( "800x630" )

#création des 2 frames
frame1 = Frame(fen1)
frame2 = Frame(fen1)

#placement des 2 frames
frame1.pack(side=LEFT,fill=BOTH, expand=True)
frame2.pack(fill=Y, expand=True)

#création du canvas pour le damier
can1 = Canvas(frame1, bg ='white')
#attente des évènements de click
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack( expand = YES, fill = BOTH )

#création du damier sur le canevas précédent
damier()

#création des boutons
b1 = Button(frame2, text ='Lancer', relief=RAISED,width=20,height=2, fg="dodger blue", command =action)
b2 = Button(frame2, text ='Stoper',relief=RAISED,width=20,height=2,fg="dodger blue", command =stop)
b3 = Button(frame2, text ='Initialiser',relief=RAISED,width=20,height=2,fg="dodger blue", command =updatedamier)
b4 = Button(frame2, text ='Quitter',relief=RAISED,width=20,height=2,fg="dodger blue", command =fen1.destroy)

#création des échelles
s1=Scale( frame2, from_ = 5, to =85, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Taille (en nombre de case)' )
s2=Scale( frame2, from_ = 0, to =80, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150,label='Nombre de cellule (en %)' )
s3=Scale( frame2, from_ = 400, to =2000, orient = HORIZONTAL,relief=RAISED,fg="dodger blue",length=150, label='Fréquence (en ms)' )


#placement des éléments
b1.pack(side=TOP)
b2.pack(side=TOP)
b3.pack(side=TOP)

s1.pack(padx=5,pady=5)
s2.pack(padx=5,pady=5)
s3.pack(padx=5,pady=5)

b4.pack(side=BOTTOM)

#attente
fen1.mainloop()
