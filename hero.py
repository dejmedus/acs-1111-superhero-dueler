import random
from ability import Ability
from weapon import Weapon
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
        self.deaths = 0
        self.kills = 0
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

    def add_kill(self, num_kills=1):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths=1):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def round(self, character, opponent):
        damage = character.attack
        opponent.defend(damage)

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''

        while self.is_alive() and opponent.is_alive():
            hero_damage = self.attack()
            opponent.take_damage(hero_damage)

            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

            if self.is_alive() == False and opponent.is_alive() == False:
                print("Draw!")
                self.add_death()
                opponent.add_death()
            elif self.is_alive() == False:
                print(opponent.name, " defeated ", self.name)
                self.add_death()
                opponent.add_kill()
            elif opponent.is_alive() == False:
                print(self.name, " defeated ", opponent.name)
                self.add_kill()
                opponent.add_death()

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)


if __name__ == "__main__":

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
