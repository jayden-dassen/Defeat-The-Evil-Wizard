import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.max_attack_power = attack_power

    def attack(self, opponent):
        self.attack_power = self.attack_power - int(random.randrange(1,5))
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def regen_attack_power(self):
        self.attack_power = self.max_attack_power

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        
    def smash(self, opponent):
        opponent.health -= self.attack_power +20 # Adding 20 attack damage by smashing the wizard
        print(f"{self.name} used special ability Smash on {opponent.name} for {self.attack_power+20} damage!")
        
    def upgrade_health(self, opponent):
        self.health = 150 # Special ability is to upgrade health to 150
        print(f"{self.name} has been granted +10 health, upgrading health to 150.")
        
    def heal(self):
        self.health = 140 # Restoring player health back to max health
        print(f"{self.name}'s health has been restored to {self.health}!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        
    def fireball(self, opponent):
        opponent.health -= self.attack_power +5 # Adding 5 attack damage due to the fireball
        print(f"{self.name} used special ability Fireball on {opponent.name} for {self.attack_power+5} damage!")
        
    def vanish(self, opponent):
        self.health += 15 # Adding 15 health to avoid the damage of the next attack from the wizard
        print(f"{self.name} has been granted +15 health to avoid the damage from {opponent.name}'s next attack.")
        
    def heal(self):
        self.health = 100 # Restoring player health back to max health
        print(f"{self.name}'s health has been restored to {self.health}!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
    def summon_minions(self, opponent):
        print("Summoning Minions...")
        opponent.health = 0 # Adding function so if player health is at or below 25, wizard automatically wins.
        print(f"Sorry, {self.name}, you let your guard down and my minions have defeated you.")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=28)
        
    def quick_shot(self, opponent):
        opponent.health -= self.attack_power +10 # Adding 10 attack damage due to the second arrow
        print(f"{self.name} used special ability Quick Shot on {opponent.name} for {self.attack_power+10} damage!")
        
    def evade(self, opponent):
        self.health += 15 # Adding 15 health to avoid the damage of the next attack from the wizard
        print(f"{self.name} has been granted +15 health to avoid the damage from {opponent.name}'s next attack.")
        
    def heal(self):
        self.health = 125 # Restoring player health back to max health
        print(f"{self.name}'s health has been restored to {self.health}!")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=40)
        
    def holy_strike(self, opponent):
        opponent.health -= self.attack_power + 15 # Adding 15 damage for the special ability
        print(f"{self.name} has used the Holy Strike on {opponent.name} for an attack damage of {self.attack_power+15}!")
        
    def divine_shield(self, opponent):
        self.health += 15 # Adding 15 health to avoid damage from attack
        print(f"{self.name} has blocked the attack from {opponent.name} using the Divine Shield!")
        
    def heal(self):
        self.health = 115 # Restoring player health back to max health
        print(f"{self.name}'s health has been restored to {self.health}!")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            player.regen_attack_power()
        elif choice == '2':
            print("1. Quick Shot (Archer)")
            print("2. Evade (Archer)")
            print("3. Holy Strike (Paladin)")
            print("4. Divine Shield (Paladin)")
            print("5. Fireball (Mage)")
            print("6. Vanish (Mage)")
            print("7. Smash (Warrior)")
            print("8. Upgrade Health (Warrior)")
            special_ability = input("Please choose the special ability that fits your character.")
            if special_ability == '1':
                player.quick_shot(wizard)
            elif special_ability == '2':
                player.evade(wizard)
            elif special_ability == '3':
                player.holy_strike(wizard)
            elif special_ability == '4':
                player.divine_shield(wizard)
            elif special_ability =='5':
                player.fireball(wizard)
            elif special_ability == '6':
                player.vanish(wizard)
            elif special_ability == '7':
                player.smash(wizard)
            elif special_ability == '8':
                player.upgrade_health(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            if player.health <= 25:
                wizard.summon_minions(player)
            wizard.regenerate()
            wizard.attack(player)
            wizard.regen_attack_power()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
