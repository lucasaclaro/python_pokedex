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
