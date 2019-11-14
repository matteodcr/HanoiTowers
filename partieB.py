def largeur_pgdisque(n):
    petit_disque = 40
    return (petit_disque+30*(n))

def base(n):
    for i in range(0,2):
        forward(3*2*20+3*largeur_pgdisque(n))
        right(90)
        forward(20)
        right(90)

def tour(n):
    down()
    dep = (3*2*20+3*largeur_pgdisque(n))/6

    forward(dep)
    backward(3)
    left(90)
    forward((n+1)*20)
    right(90)
    forward(6)
    right(90)
    forward((n+1)*20)
    left(90)
    forward(dep)
    backward(3)
    up()
        

def dessine_plateau(n):
    up()
    goto(-300,200)
    down()
    base(n)
    for i in range(0,3):
        tour(n)
def dessine_disque(plateau, nd, n,couleur):
    dep = (3*2*20+3*largeur_pgdisque(n))/6
    postour,posdisque, len = position_disque(plateau,nd)
    goto(-300,200)
    up()
    if postour == 0 :
        goto((-300+dep),200)
    if postour == 1 :
        goto((-300+3*dep),200)
    if postour == 2 :
        goto((-300+5*dep),200)
    down()
    if couleur == 'noir':fillcolor('black')
    if couleur == 'blanc':fillcolor('white')
        
   
    begin_fill()
    left(90)
    up()
    forward(20*(len-posdisque))
    right(90)
    forward((40+30*nd)/2)
    right(90)
    forward(20)
    right(90)
    forward(40+30*nd)
    right(90)
    forward(20)
    right(90)
    forward((40+30*nd)/2)
    end_fill()

def efface_disque(plateau, nd, n, state):
    dessine_disque(plateau, nd,n,'blanc')
    if state == 'single':
        goto(-300,200)
        pencolor("red")
        for i in range(0,3):
            tour(n)

def dessine_config(plateau, n):
    for index_tour,value_tour in enumerate(plateau):
        l = list(plateau[index_tour])
        for i in range(0,len(l)) :
            dessine_disque(plateau, l[i]-1,n,'noir')

            
def efface_tout(plateau, n):
    for index_tour,value_tour in enumerate(plateau):
        l = list(plateau[index_tour])
        for i in range(0,len(l)):
            efface_disque(plateau, l[i]-1,n, None)
        goto(-300,200)
        pencolor("red")
    for i in range(0,3):
        tour(n)

speed(5)
