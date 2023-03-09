import unittest
import task_00
import task_01

class MyTestCase(unittest.TestCase):
    def test00_len(self):
        test1 = task_00.key()
        self.assertEqual(len(test1), 1337)  # add assertion here
    def test00_getithem(self):
        test1 = task_00.key()
        self.assertEqual(test1[404], 3)

    def test00_gt(self):
        test1 = task_00.key()
        self.assertEqual((test1 > 9000), True)
    def test00_pass(self):
        key = task_00.key()
        self.assertEqual(key.passphrase == "zax2rulez", True)

    def test00_str(self):
        key = task_00.key()
        self.assertEqual(str(key) == "GeneralTsoKeycard", True)

    def test01_play(self):
        player1 = task_01.Cheater()
        player2 = task_01.Cooperator()
        gm = task_01.Game()
        gm.play(player1, player2)
        self.assertEqual(player2.history[1], False)

if __name__ == '__main__':
    unittest.main()
