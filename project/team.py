import Units


class Team:
    def __init__(self):
        self.units_num = 3
        self.team_arr = [None] * self.units_num
        self.alive_num = 3
        self.active = ''                        # игрок, являющийся активным

    # добавление нового члена команды
    def add_member(self, member_num, unit):
        self.team_arr[member_num] = unit

    # проверка статуса (в игре/выбыл из игры)
    def check_status(self, unit):
        if unit.status == 'alive':
            return True
        else:
            return False

    # обновление статуса
    def upd_status(self, unit):
        if unit.hp == 0:
            unit.status = 'dead'
            self.alive_num -= 1

    # изменение активного члена команды
    def new_active(self, member):
        self.active = self.team_arr[member]
        print(f'{self.active.type} is your current active unit!\n')

    # поглаживание
    def stroke(self, num):
        member = self.team_arr[num]
        member.change_hp(member.stroke)

    # совершение атаки
    def attack(self, opp_team):
        opponent = opp_team.active
        opponent.change_hp(-1 * self.active.damage)
        print(f'{opponent.type} lost {self.active.damage} hp!\n')

    # совершение эволюции
    def evolve(self, member):
        if self.check_status(member):
            member.evolution()

    # информация о всех членах команды
    def team_info(self):
        for num, unit in enumerate(self.team_arr):
            unit.print_info()

    # информация о не вышедших из сражения юнитах
    def team_alive_info(self):
        for num, unit in enumerate(self.team_arr):
            if self.check_status(unit):
                print(f'Number: {num + 1}')
                unit.print_info()

    # завершение игры
    def has_player_lost(self):
        if self.alive_num <= 0:
            return False
        else:
            return True
