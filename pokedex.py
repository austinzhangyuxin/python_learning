import sys
from pokemongo_api import PGoApi

def get_pokemon_info(pokedex_number):
    api = PGoApi()
    api.activate_signature("libencrypt.so")  # You'll need this library for complete functionality

    try:
        response = api.getProfile()
        if response['status_code'] == 1:
            profile = response['responses']['GET_PLAYER']['player_data']
            print(f"Trainer level: {profile['level']}")

            # Get Pokémon info based on Pokedex number
            response = api.getInventory()
            if response['status_code'] == 1:
                inventory_items = response['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']
                for item in inventory_items:
                    if 'pokemon_data' in item:
                        pokemon = item['pokemon_data']
                        if pokemon.get('pokedex_id', 0) == pokedex_number:
                            print(f"Pokemon Name: {pokemon['pokemon_id']}")
                            print(f"CP: {pokemon.get('cp', 'N/A')}")
                            print(f"IV: {pokemon.get('individual_attack', 'N/A')}/{pokemon.get('individual_defense', 'N/A')}/{pokemon.get('individual_stamina', 'N/A')}")
                            break
                else:
                    print(f"No Pokémon found with Pokedex number {pokedex_number}")
            else:
                print("Error fetching inventory data")
        else:
            print("Error fetching profile data")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        pokedex_number = int(input("Enter a Pokedex number: "))
        get_pokemon_info(pokedex_number)
    except ValueError:
        print("Invalid input. Please enter a valid Pokedex number (e.g., 25 for Pikachu).")

