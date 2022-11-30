import requests
import PIL
from PIL import Image
import urllib.request



def show_pokemon(pokemon):

        link = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        request = requests.get(link)
        request_json = request.json()
        pokemon_id = request_json['id']
        pokemon_name = request_json['forms'][0]['name']
        pokemon_type = request_json['types'][0]['type']['name']
        pokemon_move = request_json['moves'][0]['move']['name']
        print(f"{pokemon_id} : {pokemon_name} | Type: {pokemon_type} | Move: {pokemon_move}.")
        pokemon_image_link = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/'
        urllib.request.urlretrieve(f'{pokemon_image_link}{pokemon}.png', f'{pokemon}.png')
        pokemon_image = request_json['sprites']['other']['home']['front_default']
        image_ = Image.open(f'{pokemon}.png')
        image_.show()

def show_151_pokemons():
    pokemon_ = 1

    print('151 pokemons:')

    while True:

        link = f'https://pokeapi.co/api/v2/pokemon/{pokemon_}'
        request = requests.get(link)
        request_json = request.json()
        pokemon_id = request_json['id']
        pokemon_name = request_json['forms'][0]['name']
        pokemon_type = request_json['types'][0]['type']['name']
        pokemon_move = request_json['moves'][0]['move']['name']
        print(f"{pokemon_id}: {pokemon_name} | Type: {pokemon_type} | Move: {pokemon_move}.")
        pokemon_ += 1

        if pokemon_ == 152:
            break

def pokemon_id(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_id = (request_json['id'])
    return pokemon_id

def pokemon_name(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_name = request_json['forms'][0]['name']
    return pokemon_name.upper()

def pokemon_type(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_type = request_json['types'][0]['type']['name']
    return pokemon_type.upper()


def pokemon_move(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_move = request_json['moves'][0]['move']['name']
    return pokemon_move.upper()

def pokemon_move2(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_move2 = request_json['moves'][1]['move']['name']
    return pokemon_move2.upper()


def pokemon_image(id):
    link = f'https://pokeapi.co/api/v2/pokemon/{id}'
    request = requests.get(link)
    request_json = request.json()
    pokemon_image_link = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/'
    urllib.request.urlretrieve(f'{pokemon_image_link}{id}.png', f'{id}.png')
    pokemon_image = request_json['sprites']['other']['home']['front_default']
    image_ = Image.open(f'{id}.png')
    imagem_return = image_.show()
    return imagem_return

def download_images():

    id = 1

    while True:
        pokemon_image(id)
        id +=1
        if id == 152:
            break


def generate_list_of_names():
    count = 1
    list_names = []
    while True:
        name = pokemon_name(count)
        list_names.append(name)
        count +=1
        if count == 152:
            break
    return list_names

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

