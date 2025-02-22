# -*- coding: utf-8 -*- 
from collections import deque

VALUE_ERROR_MESSAGE = "Координаты start_x и start_y должны быть целыми числами или строками, содержащими целые числа."
FIRST_POINT_DIGIT_SUM_ERROR_MESSAGE = "Начальная клетка недоступна: сумма цифр координат превышает 25."

class AntMovement:
    def __init__(self, start_x, start_y, include_start_to_visit=True):
        self.__MAX_DIGITS_SUM = 25
        self.__include_start_to_visit = include_start_to_visit

        self.__start_x = self.__parse_coordinate(start_x)
        self.__start_y = self.__parse_coordinate(start_y)

        if self.__include_start_to_visit and not self.__is_cell_accessible(self.__start_x, self.__start_y):
            raise ValueError(FIRST_POINT_DIGIT_SUM_ERROR_MESSAGE)

        self.__visited_cells = set()
        self.__queue = deque()

    @staticmethod
    def __parse_coordinate(coordinate):
        if isinstance(coordinate, str):
            try:
                coordinate = int(coordinate)
            except ValueError:
                raise ValueError(VALUE_ERROR_MESSAGE)

        if not isinstance(coordinate, int):
            raise ValueError(VALUE_ERROR_MESSAGE)

        return coordinate

    @staticmethod
    def __get_digits_sum(number):
        return sum(int(digit) for digit in str(abs(number)))

    def __is_cell_accessible(self, x, y):
        return self.__get_digits_sum(x) + self.__get_digits_sum(y) <= self.__MAX_DIGITS_SUM
    
    def get_count_visited_cells(self):
        self.__queue.append((self.__start_x, self.__start_y))
        self.__visited_cells.add((self.__start_x, self.__start_y))

        while self.__queue:
            x, y = self.__queue.popleft()
            self.__add_cell_to_visited(x, y)

        if not self.__include_start_to_visit:
            self.__visited_cells.discard((self.__start_x, self.__start_y))

        return len(self.__visited_cells)
    
    def __add_cell_to_visited(self, x, y):
        move_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in move_directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in self.__visited_cells and self.__is_cell_accessible(new_x, new_y):
                self.__visited_cells.add((new_x, new_y))
                self.__queue.append((new_x, new_y))


try:
    ant_move = AntMovement(1000, "1000", True)
    print(ant_move.get_count_visited_cells())
except ValueError as e:
    print("Ошибка: {}".format(e))