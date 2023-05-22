import turtle
turtle = turtle.Turtle()
main = turtle.screen
escritor = turtle.clone()
turtle.speed(0) 

estado = ['cyntia de boas', 'ornã surtando'] and ['ornã foi embora, cynthia no comando']


def forca():
    global turtle
    #posiciona tartaruga
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.right(-90)
    turtle.fd(50)
    turtle.pd()

    #desenha forca
    turtle.fd(25)
    turtle.right(-90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(250)

def cabeca():
    global turtle
    #posiciona tartaruga
    turtle.pu()
    turtle.goto(-212.13,212.13)
    turtle.left(90)
    turtle.pd()
    #desenha cabeça
    turtle.circle(25)

def braco1():
    global turtle
    turtle.goto(-212.13,212.13)
    #desenha os braços
    turtle.right(45)
    turtle.fd(50)
    turtle.pu()
    turtle.backward(50)
    turtle.pd()

def braco2():
    global turtle
    
    turtle.right(90)
    turtle.fd(50)

def corpo():
    #desenha o corpo 
    global turtle
    turtle.pu()
    turtle.backward(50)
    turtle.right(-45)
    turtle.pd()
    turtle.fd(100)

def pernas():
    global turtle
    #desenha as pernas
    turtle.right(45)
    turtle.fd(50)
    turtle.pu()
    turtle.backward(50)
    turtle.pd()
    turtle.right(-90)
    turtle.fd(50)

forca()
cabeca()
braco1()
braco2()
corpo()
pernas()


escritor.write(estado, align ='left')

main.mainloop()


