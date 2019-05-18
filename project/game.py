import Units
import team
import actions


class SGame:
    def __init__(self):
        # информация о доступных юнитах
        self.units_list = [Units.Pikachu,
                           Units.Piplup,
                           Units.Charmander,
                           Units.Butterfree,
                           Units.Glaceon,
                           Units.Bulbasaur]
        self.units_arr = list(map(int, range(1, len(self.units_list) + 1)))

        # информация об игроках
        self.players_num = 2
        self.players_list = []
        for i in range(self.players_num):
            self.players_list.append(team.Team())

        # информация о командах
        self.members_num = 3
        self.team_members = list(map(int, range(1, self.members_num + 1)))

        # информация об игровом процессе
        self.game_state = True  # состояние игры на данный момент
        self.winner = 0

        # игровые сообщения
        self.error_message = 'Try again, my darling!\
                              \nIt\'s worth entering a proper number.\n'
        self.exit_message = 'let me out'
        self.bye_message = 'Game is over. Bye!'
        self.separation = '\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'

    # вывод списка доступных unit'ов
    def print_units(self):
        print('Here is the list of the units:\n')
        for num, unit in enumerate(self.units_list):
            print(f'{num + 1}. {unit.__name__}')

    # проверка корректности ввода
    def check_input(self, valid_values):
        while self.game_state:
            t = input()                         # exit
            if t.lower() == self.exit_message:
                print(self.bye_message)
                self.game_state = False
            else:
                try:
                    val = int(t)
                    if val not in valid_values:
                        print(self.error_message)
                        continue                # wrong input
                    return True, (val - 1)      # proper input
                except ValueError:
                    print(self.error_message)
                    continue                     # wrong input
        return self.game_state, -1

    # формирование команд игроков
    def start(self, act):
        for player, team in enumerate(self.players_list):
            print(f'Player{player + 1}, you are to choose three units!\n')
            self.print_units()
            for unit_num in range(self.members_num):
                print(f'Choose the {unit_num + 1} unit:')
                result, num = self.check_input(self.units_arr)
                if result:
                    act.add_member(team, unit_num, self.units_list[num]())
                else:
                    return
            print(f'Player{player + 1}, here is your dream team!')
            act.print_team(self.players_list[player])

    # выбор активного персонажа вторым игроком
    def first_iter(self, act):
        for player, team in enumerate(self.players_list):
            if player == 0:
                pass
            else:
                print(f'Player{player + 1}, choose your fighter!\n')
                act.print_team_info(self.players_list[player])
                result, num = self.check_input(self.team_members)
                if result:
                    act.choose_active(team, num)
                else:
                    return self.bye_message
        print(self.separation)

    # запуск игрового процесса
    def play(self):
        act = actions.Action(self)
        self.start(act)
        if not self.game_state:
            return self.bye_message
        print('\nLet the fight begin!\n')
        self.first_iter(act)
        while self.game_state:
            if not self.game_state:
                return self.bye_message
            for player, team in enumerate(self.players_list):
                # Выбор персонажа для боя (активного персонажа)
                print(f'Player{player + 1}, choose your fighter!\n')
                act.print_team_info(self.players_list[player])
                result, num = self.check_input(act.gen_list_of_alive(team))
                if result:
                    act.choose_active(team, num)
                else:
                    return self.bye_message
                # Выбор персонажа для поглаживания
                if act.check_stroke(team):
                    print(f'Player{player + 1}, '
                          f'choose which unit to stroke!\n')
                    result, num = \
                        self.check_input(act.gen_list_of_inactive(team))
                    if result:
                        act.inactive_members(team, num)
                    else:
                        print(self.bye_message)
                        return
                # Атака
                act.make_an_attack(self.players_list[player],
                                  self.players_list[(player + 1) % 2], player)
                print(self.separation)
                if not self.game_state:
                    break
        print(f'The game is over! You all fought like lions '
              f'but Player{self.winner + 1} has won. Congratulations!')
        return
