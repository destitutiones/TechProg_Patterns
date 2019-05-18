class Unit:
    def __init__(self):
        self.hp = 0
        self.max_hp = 0
        self.min_hp = 0
        self.damage = 0
        self.status = 'alive'
        self.type = ''
        self.stroke = 5            # кол-во хп, добавляющееся при поглаживании
        self.evolution_delta = 1.3  # процент изменения значений характеристик

    def print_info(self):
        print('* * * * *')
        print(f'type = {self.type},\nhp = {self.hp},\
                \ndamage = {self.damage},\nstatus = {self.status}')
        print('* * * * *\n')

    # изменение кол-ва очков здоровья
    def change_hp(self, delta):
        self.hp = max(self.min_hp, min(self.max_hp, self.hp + delta))

    # совершение эволюции
    def evolution(self):
        self.max_hp = self.max_hp * self.evolution_delta
        self.hp = self.hp * self.evolution_delta
        self.damage = self.damage * self.evolution_delta


class Pikachu(Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 55
        self.hp = self.max_hp
        self.damage = 23
        # self.luck = 0.7
        self.type = 'Pikachu'


class Piplup(Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 48
        self.hp = self.max_hp
        self.damage = 29
        # self.luck = 0.4
        self.type = 'Piplup'


class Charmander(Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 60
        self.hp = self.max_hp
        self.damage = 19
        # self.luck = 0.5
        self.type = 'Charmander'


class Butterfree (Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 37
        self.hp = self.max_hp
        self.damage = 39
        # self.luck = 0.5
        self.type = 'Butterfree'


class Glaceon(Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 33
        self.hp = self.max_hp
        self.damage = 47
        # self.luck = 0.05
        self.type = 'Glaceon'


class Bulbasaur(Unit):
    def __init__(self):
        super().__init__()
        self.max_hp = 68
        self.hp = self.max_hp
        self.damage = 13
        # self.luck = 0.5
        self.type = 'Bulbasaur'
