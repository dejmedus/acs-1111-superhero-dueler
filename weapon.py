import random

from ability import Ability


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """

        half_damage = self.max_damage // 2
        random_value = random.randint(0, half_damage)
        return random_value
