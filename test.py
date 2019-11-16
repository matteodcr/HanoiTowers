import turtle

def appui_sur_a():
    print("Touche 'a' pressée !")

def appui_quelconque():
    print("Touche pressée !")

def toto(x, y):
    print("toto : {}, {}".format(x, y))

def tutu(x, y):
    print("tutu : {}, {}".format(x, y))
    
def tata(x, y):
    print("tata : {}, {}".format(x, y))

def titi(x, y):
    print("titi : {}, {}".format(x, y))
    
def tete(x, y):
    print("tete : {}, {}".format(x, y))

if __name__ == "__main__":
    #Pas besoin de turtle.listen() vu que l'on ne s'occupe pas du clavier

    #Clique gauche : juste toto au final
    turtle.onscreenclick(titi, 1)
    turtle.onscreenclick(toto, 1)  # <=>  turtle.onscreenclick(toto, 1, False)
   
    #Clique central : juste tata
    turtle.onscreenclick(tata, 2)

    #Clique droit : tete et tutu
    turtle.onscreenclick(tete, 3)
    turtle.onscreenclick(tutu, 3, True)
    
    turtle.mainloop()