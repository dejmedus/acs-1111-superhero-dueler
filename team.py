import random


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False

        for hero in self.heroes:

            if hero.name == name:
                self.heroes.remove(hero)

                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            attacker = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            attacker.fight(opponent)

            living_heroes = list()
            for hero in self.heroes:
                if hero.is_alive():
                    living_heroes.append(hero)

            living_opponents = list()
            for hero in other_team.heroes:
                if hero.is_alive():
                    living_opponents.append(hero)

        if len(living_heroes) > 0:
            print(self.name, 'Wins!')

        if len(living_opponents) > 0:
            print(other_team, 'Wins!')

    def stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.name + " average K/D was: " +
              str(team_kills/team_deaths))

        for hero in self.heroes:
            if hero.deaths == 0:
                print("survived from " +
                      self.name + ": " + hero.name)
