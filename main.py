import tkinter
from tkinter import *
from tkinter import messagebox
from functions import *


master = Tk()
master.title('Pokedex')
master.geometry('1400x800+250+100')
master.minsize(1400, 800)
master.maxsize(1400, 800)
background = PhotoImage(file='images/pokewall.png')
background_master = Label(master, image=background)
background_master.pack()


list_of_names = ['BULBASAUR', 'IVYSAUR', 'VENUSAUR', 'CHARMANDER', 'CHARMELEON', 'CHARIZARD', 'SQUIRTLE',
                 'WARTORTLE', 'BLASTOISE', 'CATERPIE', 'METAPOD', 'BUTTERFREE', 'WEEDLE', 'KAKUNA', 'BEEDRILL',
                 'PIDGEY', 'PIDGEOTTO', 'PIDGEOT', 'RATTATA', 'RATICATE', 'SPEAROW', 'FEAROW', 'EKANS', 'ARBOK',
                 'PIKACHU', 'RAICHU', 'SANDSHREW', 'SANDSLASH', 'NIDORAN-F', 'NIDORINA', 'NIDOQUEEN', 'NIDORAN-M',
                 'NIDORINO', 'NIDOKING', 'CLEFAIRY', 'CLEFABLE', 'VULPIX', 'NINETALES', 'JIGGLYPUFF', 'WIGGLYTUFF',
                 'ZUBAT', 'GOLBAT', 'ODDISH', 'GLOOM', 'VILEPLUME', 'PARAS', 'PARASECT', 'VENONAT', 'VENOMOTH',
                 'DIGLETT', 'DUGTRIO', 'MEOWTH', 'PERSIAN', 'PSYDUCK', 'GOLDUCK', 'MANKEY', 'PRIMEAPE', 'GROWLITHE',
                 'ARCANINE', 'POLIWAG', 'POLIWHIRL', 'POLIWRATH', 'ABRA', 'KADABRA', 'ALAKAZAM', 'MACHOP',
                 'MACHOKE', 'MACHAMP', 'BELLSPROUT', 'WEEPINBELL', 'VICTREEBEL', 'TENTACOOL', 'TENTACRUEL',
                 'GEODUDE', 'GRAVELER', 'GOLEM', 'PONYTA', 'RAPIDASH', 'SLOWPOKE', 'SLOWBRO', 'MAGNEMITE',
                 'MAGNETON', 'FARFETCHD', 'DODUO', 'DODRIO', 'SEEL', 'DEWGONG', 'GRIMER', 'MUK', 'SHELLDER',
                 'CLOYSTER', 'GASTLY', 'HAUNTER', 'GENGAR', 'ONIX', 'DROWZEE', 'HYPNO', 'KRABBY', 'KINGLER',
                 'VOLTORB', 'ELECTRODE', 'EXEGGCUTE', 'EXEGGUTOR', 'CUBONE', 'MAROWAK', 'HITMONLEE', 'HITMONCHAN',
                 'LICKITUNG', 'KOFFING', 'WEEZING', 'RHYHORN', 'RHYDON', 'CHANSEY', 'TANGELA', 'KANGASKHAN',
                 'HORSEA', 'SEADRA', 'GOLDEEN', 'SEAKING', 'STARYU', 'STARMIE', 'MR-MIME', 'SCYTHER', 'JYNX',
                 'ELECTABUZZ', 'MAGMAR', 'PINSIR', 'TAUROS', 'MAGIKARP', 'GYARADOS', 'LAPRAS', 'DITTO', 'EEVEE',
                 'VAPOREON', 'JOLTEON', 'FLAREON', 'PORYGON', 'OMANYTE', 'OMASTAR', 'KABUTO', 'KABUTOPS',
                 'AERODACTYL', 'SNORLAX', 'ARTICUNO', 'ZAPDOS', 'MOLTRES', 'DRATINI', 'DRAGONAIR', 'DRAGONITE',
                 'MEWTWO', 'MEW']


text_choose_id = Label(master, text="Choose id between 1 - 151",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_choose_id.place(width=300, height=30, x=170, y=350)

entry_id = Entry(master, font=('Verdana', 8, 'bold'), bg='white', fg='#000000', justify=CENTER)
entry_id.place(width=100, height=30, x=270, y=400)

text_or = Label(master, text="OR",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_or.place(width=50, height=30, x=296, y=500)

text_choose = Label(master, text="Type the name of pokemon",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_choose.place(width=300, height=30, x=170, y=550)

entry_name = Entry(master, font=('Verdana', 8, 'bold'), bg='white', fg='#000000', justify=CENTER)
entry_name.place(width=100, height=30, x=270, y=600)




def choose_pokemon_id():

    master2 = tkinter.Toplevel()
    master2.title('Pokedex')
    master2.geometry('1400x800+250+100')
    master2.minsize(1400, 800)
    master2.maxsize(1400, 800)
    background2 = PhotoImage(file='images/pokemon_wallpapel.png')
    background_master2 = Label(master2, image=background2)
    background_master2.pack()

    poke_id = int(entry_id.get())



    id = Label(master2, text=f"#ID {pokemon_id(poke_id)}", font=('Verdana', 12, 'bold'), fg='white', background='black')
    id.place(width=345, height=50, x=200, y=300)

    name = Label(master2, text=pokemon_name(poke_id), font=('Verdana', 30, 'bold'), fg='white', background='black')
    name.place(width=345, height=50, x=200, y=350)

    type = Label(master2, text=pokemon_type(poke_id), font=('Verdana', 16, 'bold'), fg='white', background='black')
    type.place(width=345, height=50, x=200, y=420)

    text = Label(master2, text='MOVES:', font=('Verdana', 16, 'bold'), fg='white', background='black')
    text.place(width=345, height=50, x=200, y=500)

    move = Label(master2, text=pokemon_move(poke_id), font=('Verdana', 14, 'bold'), fg='white', background='black')
    move.place(width=345, height=50, x=200, y=550)

    move2= Label(master2, text=pokemon_move2(poke_id), font=('Verdana', 14, 'bold'), fg='white', background='black')
    move2.place(width=345, height=50, x=200, y=600)

    if poke_id > 152:
        messagebox.showinfo(title='Error!', message='Choose ID between 1 - 151.')
    else:
        image_pokemon_ = PhotoImage(file=f'images/{poke_id}.png')
        image_master_ = Label(master2, image=image_pokemon_, background='black')
        image_master_.place(width=450, height=500, x=652, y=250)

    master2.mainloop()

def choose_pokemon_name():

    poke_name = (str(entry_name.get())).lower()
    pokemon_name_exist = poke_name.upper()

    correct_names = []
    incorrect_names = []

    for name in list_of_names:
        if (name == pokemon_name_exist):
            correct_names.append(name)
        else:
            incorrect_names.append(name)

    if len(correct_names) == 0:
        messagebox.showinfo(title='Error!', message='Incorrect name, try again.')
    else:

        master2 = tkinter.Toplevel()
        master2.title('Pokedex')
        master2.geometry('1400x800+250+100')
        master2.minsize(1400, 800)
        master2.maxsize(1400, 800)
        background2 = PhotoImage(file='images/pokemon_wallpapel.png')
        background_master2 = Label(master2, image=background2)
        background_master2.pack()

        poke_name = (str(entry_name.get())).lower()


        id = Label(master2, text=f"#ID {pokemon_id(poke_name)}", font=('Verdana', 12, 'bold'), fg='white',
                   background='black')
        id.place(width=345, height=50, x=200, y=300)

        name = Label(master2, text=pokemon_name(poke_name), font=('Verdana', 30, 'bold'), fg='white',
                     background='black')
        name.place(width=345, height=50, x=200, y=350)

        type = Label(master2, text=pokemon_type(poke_name), font=('Verdana', 16, 'bold'), fg='white',
                     background='black')
        type.place(width=345, height=50, x=200, y=420)

        text = Label(master2, text='MOVES:', font=('Verdana', 16, 'bold'), fg='white', background='black')
        text.place(width=345, height=50, x=200, y=500)

        move = Label(master2, text=pokemon_move(poke_name), font=('Verdana', 14, 'bold'), fg='white',
                     background='black')
        move.place(width=345, height=50, x=200, y=550)

        move2 = Label(master2, text=pokemon_move2(poke_name), font=('Verdana', 14, 'bold'), fg='white',
                      background='black')
        move2.place(width=345, height=50, x=200, y=600)

        image_pokemon_ = PhotoImage(file=f"images/{pokemon_id(f'{poke_name}')}.png")
        image_master_ = Label(master2, image=image_pokemon_, background='black')
        image_master_.place(width=450, height=500, x=652, y=250)

        master2.mainloop()






button_choose_id = Button(master, text='GO!', font=('Verdana', 14, 'bold'), bg='#A6A6A6', command=choose_pokemon_id)
button_choose_id.place(width=100, height=40, x=270, y=450)

button_choose_name = Button(master, text='GO!!', font=('Verdana', 14, 'bold'), bg='#A6A6A6', command=choose_pokemon_name)
button_choose_name.place(width=100, height=40, x=270, y=650)





text_choose = Label(master, text="Choose id between 1 - 151",  font=('Verdana', 12, 'bold'), bg='black', fg='white', justify=CENTER)
text_choose.place(width=300, height=30, x=170, y=350)

entry_id = Entry(master, font=('Verdana', 8, 'bold'), bg='white', fg='#000000', justify=CENTER)
entry_id.place(width=100, height=30, x=270, y=400)



def choose_pokemon():

    master2 = tkinter.Toplevel()
    master2.title('Pokedex')
    master2.geometry('1400x800+250+100')
    master2.minsize(1400, 800)
    master2.maxsize(1400, 800)
    background2 = PhotoImage(file='images/pokemon_wallpapel.png')
    background_master2 = Label(master2, image=background2)
    background_master2.pack()

    poke_id = int(entry_id.get())

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

    if poke_id > 152:
        messagebox.showinfo(title='Error!', message='Choose ID between 1 - 151.')
    else:
        image_pokemon_ = PhotoImage(file=f'images/{poke_id}.png')
        image_master_ = Label(master2, image=image_pokemon_, background='black')
        image_master_.place(width=450, height=500, x=652, y=250)

    master2.mainloop()






master.mainloop()
