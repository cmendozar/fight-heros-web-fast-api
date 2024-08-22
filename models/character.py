import random

class Character:
    def __init__(self, data):
        self.id = data.get('id', 'unknown')
        self.name = data.get('name', 'unknown')
        self.alignment = data.get('biography', {}).get('alignment', 'unknown')
        self.intelligence = self.safe_float(data['powerstats'].get('intelligence'))
        self.strength = self.safe_float(data['powerstats'].get('strength'))
        self.speed = self.safe_float(data['powerstats'].get('speed'))
        self.durability = self.safe_float(data['powerstats'].get('durability'))
        self.power = self.safe_float(data['powerstats'].get('power'))
        self.combat = self.safe_float(data['powerstats'].get('combat'))
        self.AS = float(random.randint(0, 10))
        self.HP = self.compute_HP()
        self.FB = None

    def safe_float(self, value):
        """Converts a value to float, treating 'null' or invalid values as 0.0."""
        try:
            return float(value) if value not in ('null', None) else 0.0
        except ValueError:
            return 0.0

    def compute_HP(self):
        return 0.5 * (0.8 * self.strength + 0.7 * self.durability + self.power) * (1 + 0.1 * self.AS) + 100
    
    def attack_damage(self, attack_type):
        if attack_type.lower() == 'mental':
            attack = 0.7 * self.intelligence + 0.2 * self.speed + 0.1 * self.combat
        elif attack_type.lower() == 'strong':
            attack = 0.6 * self.strength + 0.2 * self.power + 0.2 * self.combat
        elif attack_type.lower() == 'fast':
            attack = 0.55 * self.speed + 0.25 * self.durability + 0.2 * self.strength
        else:
            raise ValueError(f"Unknown attack type: {attack_type}")
        
        if self.FB:
            return attack * self.FB
        return attack
    
    def is_aligned(self, team_alignment):
        return self.alignment == team_alignment if team_alignment else False

    def is_alive(self):
        return self.HP > 0
    
    def receive_damage(self, damage):
        self.HP -= damage
        if self.HP < 0:
            self.HP = 0

    def print_stats(self):
        print(f"Character: {self.name} (ID: {self.id})")
        print(f"  Alignment: {self.alignment}")
        print(f"  Intelligence: {self.intelligence}")
        print(f"  Strength: {self.strength}")
        print(f"  Speed: {self.speed}")
        print(f"  Durability: {self.durability}")
        print(f"  Power: {self.power}")
        print(f"  Combat: {self.combat}")
        print(f"  HP: {self.HP}")
        print(f"  FB: {self.FB}")
        print("=" * 50)
