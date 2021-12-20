Fenetre1 = Tk()
c=10
i=0

flag=0
dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes


def initialiser(taille):
    i=0
    while i!= taille/c: #assigne une valeur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte ^^)
        j=0
        while j!= taille/c:
            x=i*c
            y=j*c
            dico_case[x,y]=0
            j+=1
        i+=1

class ScaleDemo( Frame ):
    """Demonstrate Canvas and Scale"""
    def __init__( self ):
        """Create a Canvas with a circle controlled by a Scale"""
        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Scale Demo" )
        self.master.geometry( "220x270" )
        # create Scale
        self.control = Scale( self, from_ = 40, to =80, \
        orient = HORIZONTAL, command = self.updatedamier )
        self.control.pack( side = BOTTOM, fill = X )
        self.control.set( 10 )
        # create Canvas and draw circle
        self.display = Canvas( self, bg = "white")
        self.display.bind("<Button-1>", self.click_gauche)
        self.display.bind("<Button-3>", self.click_droit)
        self.display.pack(side =TOP, padx =5, pady =5)
        self.display.pack( expand = YES, fill = BOTH )
    
    def click_gauche(self, event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
        x = event.x -(event.x%c)
        y = event.y -(event.y%c)
        self.display.create_rectangle(x, y, x+c, y+c, fill='black')
        dico_case[x,y]=1
    def click_droit(self, event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
        x = event.x -(event.x%c)
        y = event.y -(event.y%c)
        self.display.create_rectangle(x, y, x+c, y+c, fill='white')
        dico_case[x,y]=0

    def damier(self,taille): 
        self.ligne_vert(taille)
        self.ligne_hor(taille)
        initialiser(taille)
        
    def ligne_vert(self,taille):
        c_x = 0
        while c_x != taille:
            self.display.create_line(c_x,0,c_x,taille,width=1,fill='black')
            c_x+=c
    def ligne_hor(self, taille):
        c_y = 0
        while c_y != taille:
            self.display.create_line(0,c_y,taille,c_y,width=1,fill='black')
            c_y+=c


    def updatedamier ( self, scaleValue ):
        #global taille
        taille = int( scaleValue )* 10
        self.display.delete("all")
        self.damier(taille)

b1 = Button(Fenetre1, text ='Quitter!')
b2 = Button(Fenetre1, text ='Lancer!')
b1.pack()
b2.pack()



ScaleDemo().mainloop()
Fenetre1.mainloop()
