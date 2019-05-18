import Units
import team


class Action:
    def __init__(self, game):
        self.game = game

        # игровые сообщения
        self.dead_message = 'This unit is out of the game,\
                                please, choose another one\n'
        self.inactive_message = 'This unit can\'t be chosen as an active one,\
                                    please, choose another one\n'

    # вывод списка команды
    def print_team(self, team):
        for num, unit in enumerate(team.team_arr):
            print(f'{num + 1}. {unit.type}')
        print('\n')

    # вывод списка команды с информацией о каждом её члене
    # из соответствующего списка
    def print_team_info(self, team):
        team.team_alive_info()

    # генерация списка доступных юнитов (для проверки ввода)
    def gen_list_of_alive(self, team):
        list_of_alive = []
        for num, unit in enumerate(team.team_arr):
            if team.check_status(unit):
                list_of_alive.append(num + 1)
        return list_of_alive

    # генерация списка неактивных (и живых) юнитов
    def gen_list_of_inactive(self, team):
        list_of_inactive = []
        for num, unit in enumerate(team.team_arr):
            if team.check_status(unit) and team.active != unit:
                list_of_inactive.append(num + 1)
        return list_of_inactive

    # добавление члена в команду
    def add_member(self, team, member_num, unit):
        team.add_member(member_num, unit)

    # выбор активного персонажа
    def choose_active(self, team, num):
        member = team.team_arr[num]
        if team.check_status(member):   # проверяем, можно ли сделать активным
            team.new_active(num)
        else:
            print(self.inactive_message)

    # проверка наличия юнитов для поглаживания
    def check_stroke(self, team):
        if team.alive_num <= 1:
            return False
        else:
            return True

    # проведение операций с неактивными персонажами
    def inactive_members(self, team, num):
        if num == -1:
            pass
        else:
            member = team.team_arr[num]
            if team.check_status(member):
                team.stroke(num)
            else:
                print(self.inactive_message)

    # совершение атаки
    def make_an_attack(self, curr_team, opp_team, player):
        curr_team.attack(opp_team)
        opp_team.upd_status(opp_team.active)
        if not opp_team.check_status(opp_team.active):
            print(f'{opp_team.active.type} is d e a d!')
            curr_team.evolve(curr_team.active)
            self.game.game_state = opp_team.has_player_lost()
            if not self.game.game_state:
                self.game.winner = player
