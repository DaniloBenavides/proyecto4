import turtle
x=int(input('Igrese numero "N" PAR de puntas: '))
t=turtle.Pen()
t.reset()
y=180+(180/x)
z=(x-2)*(180/x)
if x%2==0:
    for i in range (x):
        t.left(z)
        t.forward(100)
else:
    print("error TIENE QUE SER NUMERO PAR......!!! ")
turtle.getscreen()._root.mainloop()
