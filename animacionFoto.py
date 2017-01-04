from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
img = PhotoImage(file="yo.gif")
canvas.create_image(0,0,anchor=NW,image=img)

def mover(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
        
canvas.bind_all('<KeyPress-Up>', mover)
canvas.bind_all('<KeyPress-Down>', mover)
canvas.bind_all('<KeyPress-Left>', mover)
canvas.bind_all('<KeyPress-Right>', mover)

tk.mainloop()
