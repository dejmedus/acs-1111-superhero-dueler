import random


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name,  starting_health=100):
        '''Instance properties:
          name: String

          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 1) randomly choose winner,
        winner = random.choices([self.name, opponent.name])[0]
        print(winner, 'Wins!')


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)
    hero1.fight(hero2)
