import requests
import random
 
pokemon_list = ["pikachu","rattata","arbok","charmander","kakuna"]
max_attempts = 3
 
def poke_getter(name):
    url = ("https://pokeapi.co/api/v2/pokemon/" + name.lower().strip())
    
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as error:
        print(f"Network error: could not reach PokeAPI ({error})")
        return None
    
    
    if response.status_code == 404:
        print(f"Invalid Pokemon name: '{name}' was not found.")
        return None
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}.")
        return None
    
    data = response.json()
 
    abilities = []
    for item in data["abilities"]:
        abilities.append(item["ability"]["name"])
 
    return{
        "name" : data["name"],
        "height" : data["height"] / 10,
        "weight" : data["weight"] / 10,
        "abilities" : abilities
    }
 
def game():
 
    pokemon_get = random.choice(pokemon_list)
    pokemon = poke_getter(pokemon_get)
    
    
 
    if pokemon_get is None:
        print(f"Try Again Later")
        return
    
    print("=======Who's That Pokemon??=========")
    print(f"Height: {pokemon['height']} m")
    print(f"Weight: {pokemon['weight']} kg")
    print(f"Abilities: {', '.join(pokemon['abilities'])}")
    print(f'Attempts Left {max_attempts}')
 
    for attempt in range(1, max_attempts + 1):
        pick = input(f"Attempt {attempt}/{max_attempts} Choose a pokemon: ").lower().strip()
 
        if pick == pokemon["name"]:
            print(f"You are Correct!, The pokemon is {pokemon['name']}")
            break
        else:
            lives = max_attempts - attempt
            if lives > 0:
                print(f"You are Wrong!, {lives} attempts left ")
    else:
        
        print(f"You Lost!, The pokemon was {pokemon['name']}")
 
game()