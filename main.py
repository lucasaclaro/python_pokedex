import tkinter
from tkinter import *
from functions import *


master = Tk()
master.title('Pokedex')
master.geometry('1400x800+250+100')
master.minsize(1400, 800)
master.maxsize(1400, 800)
background = PhotoImage(file='images/pokewall.png')
background_master = Label(master, image=background)
background_master.pack()


poke_id = 25



text_choose = Label(master, text="Who is that Pokemon?",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_choose.place(width=300, height=30, x=200, y=250)

text_choose = Label(master, text="Choose id between 1 - 151",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_choose.place(width=300, height=30, x=200, y=300)

entry_id = Entry(master, font=('Verdana', 8, 'bold'), bg='white', fg='#000000', justify=CENTER)
entry_id.place(width=100, height=30, x=300, y=360)



def choose_pokemon():

    master2 = tkinter.Toplevel()
    master2.title('Pokedex')
    master2.geometry('1400x800+250+100')
    master2.minsize(1400, 800)
    master2.maxsize(1400, 800)
    background2 = PhotoImage(file='images/pokemon_wallpapel.png')
    background_master2 = Label(master2, image=background2)
    background_master2.pack()

    poke_id = str(entry_id.get())

    id2 = Label(master2, text=f"#ID {pokemon_id(poke_id)}", font=('Verdana', 12, 'bold'), fg='white', background='black')
    id2.place(width=345, height=50, x=200, y=300)

    name2 = Label(master2, text=pokemon_name(poke_id), font=('Verdana', 30, 'bold'), fg='white', background='black')
    name2.place(width=345, height=50, x=200, y=350)

    type2 = Label(master2, text=pokemon_type(poke_id), font=('Verdana', 16, 'bold'), fg='white', background='black')
    type2.place(width=345, height=50, x=200, y=420)

    text2 = Label(master2, text='MOVES:', font=('Verdana', 16, 'bold'), fg='white', background='black')
    text2.place(width=345, height=50, x=200, y=500)

    move2 = Label(master2, text=pokemon_move(poke_id), font=('Verdana', 14, 'bold'), fg='white', background='black')
    move2.place(width=345, height=50, x=200, y=550)

    move22 = Label(master2, text=pokemon_move2(poke_id), font=('Verdana', 14, 'bold'), fg='white', background='black')
    move22.place(width=345, height=50, x=200, y=600)

    image_pokemon_ = PhotoImage(file=f'images/{poke_id}.png')
    image_master_ = Label(master2, image=image_pokemon_, background='black')
    image_master_.place(width=450, height=500, x=652, y=250)

    master2.mainloop()


button_choose = Button(master, text='GO!', font=('Verdana', 14, 'bold'), bg='#A6A6A6', command=choose_pokemon)
button_choose.place(width=100, height=40, x=300, y=450)




master.mainloop()
