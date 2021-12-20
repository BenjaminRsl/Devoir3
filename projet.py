Fenetre1 = Tk()

c=10

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
        self.display.pack( expand = YES, fill = BOTH )
    
    def damier(self,taille): #fonction dessinant le tableau
        self.ligne_vert(taille)
        self.ligne_hor(taille)
        
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
        val = int( scaleValue )* 10
        self.display.delete("all")
        self.damier(val)

b1 = Button(Fenetre1, text ='Quitter!')
b1.pack()
ScaleDemo().mainloop()
Fenetre1.mainloop()
