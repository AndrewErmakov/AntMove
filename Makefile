# Укажите путь к интерпретатору Python 2.7
PYTHON_27 = python2.7

run:
	$(PYTHON_27) ant_movement.py

test:
	$(PYTHON_27) test_ant_movement.py
