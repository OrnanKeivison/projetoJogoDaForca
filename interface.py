import turtle
turtle = turtle.Turtle()
turtle.speed(1) 

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

#posiciona tartaruga
turtle.pu()
turtle.goto(-212.13,212.13)
turtle.left(90)
turtle.pd()
#desenha cabeça
turtle.circle(25)

#desenha os braços
turtle.right(45)
turtle.fd(50)
turtle.pu()
turtle.backward(50)
turtle.pd()
turtle.right(90)
turtle.fd(50)

#desenha o corpo
turtle.pu()
turtle.backward(50)
turtle.right(-45)
turtle.pd()
turtle.fd(100)

turtle.right(45)
turtle.fd(50)
turtle.pu()
turtle.backward(50)
turtle.pd()
turtle.right(-90)
turtle.fd(50)

turtle.mainloop()


