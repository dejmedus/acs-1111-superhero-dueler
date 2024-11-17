import random
from ability import Ability
from armor import Armor


class Hero:

    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defended_damage = max(damage - self.defend(), 0)
        self.current_health -= defended_damage

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        return True

    def round(self, character, opponent):
        damage = character.attack
        opponent.defend(damage)

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                hero_damage = self.attack()
                opponent.take_damage(hero_damage)

                opponent_damage = opponent.attack()
                self.take_damage(opponent_damage)

                if self.is_alive() == False and opponent.is_alive() == False:
                    print("Draw!")
                elif self.is_alive() == False:
                    print(opponent.name, " defeated ", self.name)
                elif opponent.is_alive() == False:
                    print(self.name, " defeated ", opponent.name)

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)


if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
