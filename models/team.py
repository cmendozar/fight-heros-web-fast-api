import random
import os
import requests
from .character import Character

MAX_ID_API = 731
TOKEN = os.environ.get('TOKEN_SUPER_HERO_API')
API_BASE_URL = f"https://www.superheroapi.com/api/{TOKEN}"
TEAM_MEMBERS = 5

class Team:
    def __init__(self, name, random_team=True):
        self.name = name
        self.characters = []
        self.alignment = None
        if random_team:
            print(f"Creating the team {self.name}....")
            print("="*50)
            self.make_random_team()

    
    def is_completed(self):
        return len(self.characters) == TEAM_MEMBERS

    def add_member(self, character):
        if self.is_a_valid_id_member(character.id):
            self.characters.append(character)
            self.check_team_conditions()
            if self.is_completed():
                self.apply_filation_bonus()
                self.alignment = self.compute_alignment()
                self.print_team_info()
        else:
            print(f"Character with ID {character.id} is already in the team.")

    def is_a_valid_id_member(self, character_id):
        existing_ids = {c.id for c in self.characters if c is not None}
        return character_id not in existing_ids

    def check_team_conditions(self):
        if len(self.characters) > TEAM_MEMBERS:
            raise ValueError(f"Only {TEAM_MEMBERS} team members are allowed.")
        elif len(self.characters) == TEAM_MEMBERS:
            print("The team is now complete.")

    def compute_alignment(self):
        alignment = [character.alignment for character in self.characters if character is not None]
        if alignment.count('good') > alignment.count('bad'):
            return 'good'
        return 'bad'
    
    def apply_filation_bonus(self):
        for character in self.characters:
            if character is not None:
                random_number = random.randint(0, 9)
                if character.is_aligned(self.alignment):
                    character.FB = 1 + random_number
                else:
                    character.FB = 1 / (1 + random_number)
    
    def is_defeated(self):
        return all(not character.is_alive() for character in self.characters if character is not None)
    
    def get_next_fighter(self):
        for character in self.characters:
            if character is not None and character.is_alive():
                return character
        return None
    
    def get_random_character(self):
        character_id = random.randint(1, MAX_ID_API)
        url = f"{API_BASE_URL}/{character_id}"
        response = requests.get(url).json()
        if response.get("response") == 'success' and self.is_a_valid_id_member(character_id):
            return Character(response)
        else:
            raise ValueError("Hero not found or invalid ID")
    
    def make_random_team(self):
        while not self.is_completed():
            try:
                character = self.get_random_character()
                self.add_member(character)
            except ValueError as e:
                print(f"Error: {e}")

    def print_team_info(self):
        print(f"Team {self.name} Info:")
        print(f"Alignment: {self.alignment}")
        for character in self.characters:
            if character:
                character.print_stats()
