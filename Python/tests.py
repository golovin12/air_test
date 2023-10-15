from unittest import TestCase
from task1 import text_editor, text_editor_re
from task2 import func1, func2, gen1, new_func2


class TestTask1(TestCase):
    def setUp(self):
        self.test_cases = {"asdflj (kla (inner) asd) port (another ))(unclosed": "asdflj  port )(unclosed",
                           "": "",
                           "(": "(",
                           ")": ")",
                           "()": "",
                           ")0(1(2(3)4)5(6)7(8": ")0(157(8",
                           "123(456": "123(456"}

    def test_text_editor(self):
        for test in self.test_cases.items():
            self.assertEqual(text_editor(test[0]), test[1])

    def test_text_editor_re(self):
        for test in self.test_cases.items():
            self.assertEqual(text_editor_re(test[0]), test[1])


class TestTask2(TestCase):
    def setUp(self):
        self.input1 = [(1, 1, 1, 1, 2), (2, 3), [], (2,)]
        self.answer1 = [(1, 1), (1, 1), (1, 1), (1, 1), (2, 4), (2, 4), (3, 27), (2, 4)]
        self.answer2 = [1, 4, 27, 4]

    def test_func1(self):
        self.assertEqual(func1(*self.input1), self.answer1)

    def test_func2(self):
        self.assertEqual(func2(self.answer1), self.answer2)

    def test_combo(self):
        output1 = func1(*self.input1)
        self.assertEqual(output1, self.answer1)
        self.assertEqual(func2(output1), self.answer2)


class TestTask2Optimisation(TestCase):
    def setUp(self):
        self.input1 = [(1, 1), (2, 3), (2,), (2,)]
        self.answer1 = [(1, 1), (1, 1), (2, 4), (3, 27), (2, 4), (2, 4)]
        self.answer2 = [1, 4, 27, 4]

    def test_gen1(self):
        self.assertEqual(list(gen1(*self.input1)), self.answer1)

    def test_func2(self):
        self.assertEqual(func2(self.answer1), self.answer2)

    def test_combo(self):
        output1 = gen1(*self.input1)
        self.assertEqual(list(output1), self.answer1)
        output1 = gen1(*self.input1)
        self.assertEqual(new_func2(output1), self.answer2)
