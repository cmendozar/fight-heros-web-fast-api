# main.py
from models.character import Character
from models.team import Team
from models.battle import Battle

if __name__ == '__main__':
    team1 = Team('Team 1')
    team2 = Team('Team 2')
    battle = Battle(team1, team2)
    battle.fight()