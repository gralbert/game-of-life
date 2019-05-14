import unittest
from classes import Cell


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell()

    def test_status(self):
        self.assertEqual(self.cell.get_status(), self.cell.status)

    def test_change_color(self):
        self.assertEqual(self.cell.get_neighbours(), self.cell.neighbours)


if __name__ == '__main__':
    unittest.main()

