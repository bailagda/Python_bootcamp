import unittest
import task

class MyTestCase(unittest.TestCase):

    def test00_add(self):
        purse = {"gold_ingots": 3}
        res = task_00.add_ingot(purse)
        self.assertEqual(res.get("gold_ingots"), 4)  # add assertion here
    def test00_get(self):
        purse = {"gold_ingots": 3}
        res = task_00.get_ingot(purse)
        self.assertEqual(res.get("gold_ingots"), 2)

    def test00_empty(self):
        purse = {"gold_ingots": 3}
        res = task_00.empty(purse)
        self.assertEqual(res.get("gold_ingots"), 0)

    def test00_error(self):
        purse = {"gold_ingots": 0}
        res = task_00.get_ingot(purse)
        self.assertEqual(res.get("gold_ingots"), 0)
    def test00_combo(self):
        purse = {"gold_ingots": 10}
        res = task_00.add_ingot(task_00.get_ingot(task_00.add_ingot(task_00.empty(purse))))
        self.assertEqual(res, {"gold_ingots": 1})

    def test01_split(self):
        res = task_00.split_booty({"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10})
        self.assertEqual(res, [{"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1}])
        res = task_00.split_booty({"gold_ingots": 0}, {"gold_ingots": 0}, {"apples": 10})
        self.assertEqual(res, [{'gold_ingots': 0}, {'gold_ingots': 0}, {'gold_ingots': 0}])

if __name__ == '__main__':
    unittest.main()
