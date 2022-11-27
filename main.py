import tkinter
from tkinter import *
from functions import *


master = Tk()
master.title('Pokedex')
master.geometry('1400x800+250+100')
master.minsize(1400, 800)
master.maxsize(1400, 800)


id = Label(master, text=f"#ID {pokemon_id(8)}", font=('Verdana', 12, 'bold'), fg='white', background='black')
id.place(width=345, height=50, x=540, y=10)

name = Label(master, text=pokemon_name(8), font=('Verdana', 18, 'bold'), fg='white', background='black')
name.place(width=345, height=50, x=540, y=50)

type = Label(master, text=pokemon_type(8), font=('Verdana', 16, 'bold'), fg='white', background='black')
type.place(width=345, height=50, x=540, y=90)

move = Label(master, text=pokemon_move(8), font=('Verdana', 16, 'bold'), fg='white', background='black')
move.place(width=345, height=50, x=540, y=130)

image_pokemon = PhotoImage(file='images/150.png')
image_master = Label(master, image=image_pokemon, background='black')
image_master.place(width=450, height=500, x=500, y=180)


master.mainloop()