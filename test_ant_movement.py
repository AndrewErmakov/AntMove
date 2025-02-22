# -*- coding: utf-8 -*-
import unittest

from ant_movement import AntMovement


class TestAntMovement(unittest.TestCase):
    def test_valid_integer_coordinates(self):
        ant = AntMovement(1000, 1000)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)

    def test_valid_integer_coordinates_with_true_include_start(self):
        ant = AntMovement(1000, 1000, True)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)

    def test_valid_integer_coordinates_with_false_include_start(self):
        ant = AntMovement(1000, 1000, False)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148847)

    def test_valid_string_coordinates(self):
        ant = AntMovement("1000", "1000")
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)

    def test_valid_string_coordinates_with_true_include_start(self):
        ant = AntMovement("1000", "1000", True)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)


    def test_valid_string_coordinates_with_false_include_start(self):
        ant = AntMovement("1000", "1000", False)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148847)

    def test_invalid_float_coordinates(self):
        with self.assertRaises(ValueError) as context:
            AntMovement(1000.5, 1000)
        self.assertEqual(
            str(context.exception),
            "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа.",
        )

    def test_invalid_string_float_coordinates(self):
        with self.assertRaises(ValueError) as context:
            AntMovement("1000.5", "1000")
        self.assertEqual(
            str(context.exception),
            "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа."
        )

    def test_invalid_string_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            AntMovement("1000abc", "1000")
        self.assertEqual(
            str(context.exception),
            "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа.",
        )

    def test_invalid_mixed_coordinates(self):
        with self.assertRaises(ValueError) as context:
            AntMovement("1000", 1000.5)
        self.assertEqual(
            str(context.exception),
            "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа.",
        )

    def test_negative_coordinates(self):
        ant = AntMovement(-1000, -1000)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)

    def test_zero_coordinates(self):
        ant = AntMovement(0, 0)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 1033841)

    def test_small_coordinates(self):
        ant = AntMovement(1, 1)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 1033841)

    def test_large_coordinates(self):
        ant = AntMovement(10000, 10000)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 148848)


    def test_invalid_type_coordinates(self):
        with self.assertRaises(ValueError) as context:
            AntMovement([1000], 1000)
        self.assertEqual(
            str(context.exception),
            "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа.",
        )

    def test_inaccessible_start_cell(self):
        with self.assertRaises(ValueError) as context:
            AntMovement(999, 999)
        self.assertEqual(
            str(context.exception),
            "Начальная клетка недоступна: сумма цифр координат превышает 25."
        )

    def test_inaccessible_start_cell_with_true_include_start(self):
        with self.assertRaises(ValueError) as context:
            AntMovement(999, 999, True)
        self.assertEqual(
            str(context.exception),
            "Начальная клетка недоступна: сумма цифр координат превышает 25."
        )

    def test_inaccessible_start_cell_with_false_include_start(self):
        ant = AntMovement(999, 999, False)
        self.assertIsInstance(ant, AntMovement)
        self.assertEqual(ant.get_count_visited_cells(), 0)

if __name__ == "__main__":
    unittest.main()
