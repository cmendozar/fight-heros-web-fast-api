# main.py
import sys
from models.character import Character
from models.team import Team
from models.battle import Battle

def simulate_battle(team_name1, team_name2):
    with open("fight.txt", "w") as f:
        sys.stdout = f
        team1 = Team('Team 1')
        team2 = Team('Team 2')
        battle = Battle(team1, team2)
        battle.fight()
        sys.stdout = sys.__stdout__
