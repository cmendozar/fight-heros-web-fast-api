import random
from .character import Character
from .team import Team

class Battle:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def fight(self):
        print(f"Battle Start: Team {self.team1.name} vs Team {self.team2.name}")
        print("=" * 50)
        
        while not self.team1.is_defeated() and not self.team2.is_defeated():
            fighter1 = self.team1.get_next_fighter()
            fighter2 = self.team2.get_next_fighter()
            if fighter1 and fighter2:
                print(f"Fight: {fighter1.name} vs {fighter2.name}")
                print("=" * 30)
                self.fight_one_on_one(fighter1, fighter2)
                print("=" * 30)
        
        if not self.team1.is_defeated():
            print(self.win_msg(self.team1))
        else:
            print(self.win_msg(self.team2))
        print("=" * 50)

    def win_msg(self, team):
        msg = f"""
Team {team.name} WINS! Characters of the
winning team: {', '.join([char.name for char in team.characters])}"""
        return msg
    
    def fight_one_on_one(self, fighter1, fighter2):
        first_attacker, second_attacker = random.choice([(fighter1, fighter2), (fighter2, fighter1)])
        while fighter1.is_alive() and fighter2.is_alive():
            attack_type = random.choice(['Mental', 'Strong', 'Fast'])
            damage = first_attacker.attack_damage(attack_type)
            second_attacker.receive_damage(damage)
            self.print_attack_result(first_attacker, second_attacker, attack_type, damage)
            if not second_attacker.is_alive():
                print(f"{first_attacker.name} wins!")
                break
            attack_type = random.choice(['Mental', 'Strong', 'Fast'])
            damage = second_attacker.attack_damage(attack_type)
            first_attacker.receive_damage(damage)
            self.print_attack_result(second_attacker, first_attacker, attack_type, damage)
            if not first_attacker.is_alive():
                print(f"{second_attacker.name} wins!")
    
    def print_attack_result(self, attacker, defender, attack_type, damage):
        print(
f"""{attacker.name} attacks {defender.name}
with {attack_type} attack causing {round(damage, 2)} damage!
{defender.name}'s HP is now {round(defender.HP, 2)}
"""
        )
