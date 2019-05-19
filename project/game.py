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
        self.answers = ['yes', 'no']
        # массив допустимых ответов игрока на вопросы
        # с ответами из self.answers:
        self.ans_num = list(map(int, range(1, len(self.answers) + 1)))

        # игровые сообщения
        self.error_message = 'Try again, my darling!\
                              \nIt\'s worth entering a proper number.\n'
        self.exit_message = 'let me out'
        self.bye_message = 'Game is over. Bye!'
        self.separation = '\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n'
        self.file_message = 'Do you want to record a game from a file?\
                            \n1. Yes\n2. No'
        self.file_existence = 'Sorry, save file doesn\'t exist\n'
        self.file_incorrect = 'Sorry, save file is incorrect\n'

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
        with open(r'file.txt', 'wb') as file:
            for player, team in enumerate(self.players_list):
                print(f'Player{player + 1}, you are to choose three units!\n')
                self.print_units()
                for unit_num in range(self.members_num):
                    print(f'Choose the {unit_num + 1} unit:')
                    result, num = self.check_input(self.units_arr)
                    if result:
                        unit = self.units_list[num]()
                        act.add_member(team, unit_num, unit)
                        pickle.dump(unit, file)     # сохранение информации о
                    else:                           # набранной команде
                        return                      # в файле

    # вывод списков команд
    def formed_teams(self, act):
        for player, team in enumerate(self.players_list):
            print(f'Player{player + 1}, here is your dream team!')
            act.print_team(self.players_list[player])

    # считывание информации из файла
    def get_info_from_file(self, act):
        try:
            with open(r'file.txt', 'rb') as file:
                t = self.members_num * self.players_num
                for unit_num in range(t):
                    player = unit_num // self.members_num
                    team = self.players_list[player]
                    try:
                        unit = pickle.load(file)
                    except EOFError:
                        print(self.file_incorrect)
                        return False
                    act.add_member(team, unit_num % self.members_num, unit)
        except FileNotFoundError:
            print(self.file_existence)
            return False
        return True

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
        print(self.file_message)
        result, num = self.check_input(self.ans_num)
        if num == 1:    # if answer is 'no'
            self.start(act)
        elif num == 0:  # if answer if 'yes'
            if self.get_info_from_file(act):
                self.formed_teams(act)
            else:
                self.start(act)
        if not self.game_state:
            return self.bye_message
        self.formed_teams(act)
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

    # запуск тестирования
    def team_formation_tests(self):
        act = actions.Action(self)
        self.get_info_from_file(act)
        answers = []
        for player, team in enumerate(self.players_list):
            for num in range(self.members_num):
                answers.append(team.team_arr[num].type)
        return answers
