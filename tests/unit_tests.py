import unittest
import random
import string
import pickle
import team
import actions

from game import SGame


class GameTest(unittest.TestCase):
    def test_team_formation(self):
        mygame = SGame()
        listik = []             # генерация числовой последовательности,
        answers = []            # поданной на ввод
        act = actions.Action(self)
        total_units_num = mygame.members_num * mygame.players_num
        for i in range(total_units_num):
            listik.append(random.randint(1, len(mygame.units_list)))
        with open('file.txt', 'wb') as tests:
            for num in listik:
                unit = mygame.units_list[num - 1]()
                answers.append(unit.type)
                pickle.dump(unit, tests)
        self.assertEqual(answers, mygame.team_formation_tests())

    # def test_wrong_input(self):
    #     mygame = SGame()
    #     N = random.randint(1, 255)    # генерация строки, поданной на ввод
    #     input_str = ''.join(random.choices(string.ascii_uppercase +
    #                         string.ascii_lowercase + string.digits, k=N))
    #     with open('input.txt', 'w') as tests:
    #       tests.write(input_str)
    #     answer = 'I won\'t play in such a way'
    #     self.assertEqual(answer, mygame.start_tests())


if __name__ == '__main__':
    unittest.main()
