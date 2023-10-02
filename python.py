from PyQt5 import uic
from math import sin, cos, tan, radians
import os
import csv
import numpy as np
import sys
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QTableWidgetItem, \
    QAbstractScrollArea, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import webbrowser
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QInputDialog


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.setWindowTitle('Помощник вертикальца')
        self.initUI()

    def initUI(self):  # ссоздание кнопок для перехода на разные темы
        self.pushButton.clicked.connect(self.graphics)
        self.pushButton.setStyleSheet("background-color : orange")
        self.pushButton_2.clicked.connect(self.kvadro_ur)
        self.pushButton_2.setStyleSheet("background-color : orange")
        self.pushButton_3.clicked.connect(self.decay)
        self.pushButton_3.setStyleSheet("background-color : orange")
        self.pushButton_4.clicked.connect(self.sin_etc)
        self.pushButton_4.setStyleSheet("background-color : orange")
        self.pushButton_5.clicked.connect(self.just_calc)
        self.pushButton_5.setStyleSheet("background-color : cyan")
        self.pushButton_6.clicked.connect(self.sistem_calc)
        self.pushButton_6.setStyleSheet("background-color : cyan")
        self.pushButton_7.clicked.connect(self.theory)
        self.pushButton_7.setStyleSheet("background-color : green")
        self.pushButton_8.clicked.connect(self.tests)
        self.pushButton_8.setStyleSheet("background-color : green")

    def graphics(self):
        self.new = Graphics()
        self.new.show()
        self.close()

    def kvadro_ur(self):
        self.new = Quadratic()
        self.new.show()
        self.close()

    def decay(self):
        self.new = Decay()
        self.new.show()
        self.close()

    def sin_etc(self):
        self.new = Sin_etc()
        self.new.show()
        self.close()

    def just_calc(self):
        self.new = Just_calc()
        self.new.show()
        self.close()

    def sistem_calc(self):
        self.new = Sistem_calc()
        self.new.show()
        self.close()

    def theory(self):
        self.new = Theory()
        self.new.show()
        self.close()

    def tests(self):
        self.new = Tests()
        self.new.show()
        self.close()


class Graphics(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('graphics.ui', self)
        self.setWindowTitle('Построение графиков функций')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.parabola)
        self.pushButton_2.clicked.connect(self.giperbola)
        self.pushButton_3.clicked.connect(self.line)

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def parabola(self):
        self.new = Parabola()
        self.new.show()
        self.close()

    def giperbola(self):
        self.new = Giperbola()
        self.new.show()
        self.close()

    def line(self):
        self.new = Line()
        self.new.show()
        self.close()


class Parabola(QDialog):
    def __init__(self):
        super(Parabola, self).__init__()
        self.setWindowTitle('Построение графика квадратичной функции')
        self.initUI()

    def initUI(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 20))
        self.button = QPushButton('Написать формулу')
        self.button.clicked.connect(self.run)
        self.button_1 = QPushButton('Решение')
        self.button_2 = QPushButton(self)
        self.button_2.setText('‹-')
        self.button_2.move(2, 2)
        self.button_2.setMaximumSize(60, 60)
        self.button_2.setFont(QFont('Arial', 20))
        self.button_2.clicked.connect(self.back)
        layout = QVBoxLayout()
        layout.addWidget(self.button_2)
        layout.addWidget(self.canvas)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.button_1)
        self.setLayout(layout)
        self.button_1.clicked.connect(self.resh)

    def resh(self):
        if self.label.text() == '':
            return
        else:
            f = open('resh.txt', 'w', encoding="utf-8")
            f.write(f'{self.label.text()} - квадратичная функция, график - парабола, ')
            formula = self.label.text().split('= ')[1]
            if formula[0] == '-':
                f.write(f'ветви вниз, так как а = {formula[:2]}\n')
            else:
                if formula[0] == 'x':
                    f.write(f'ветви вверх, так как а = {1}\n')
                else:
                    f.write(f'ветви вверх, так как а = {formula[0]}\n')
            sp_formula = formula.split()
            a = 1
            if sp_formula[0] != 'x':
                a = int(sp_formula[0])
            sp_formula = list(reversed(sp_formula))
            index_x = sp_formula.index('x')
            print(index_x)
            print(sp_formula)
            b = 0
            sp_formula = list(reversed(sp_formula))
            print(sp_formula)
            if len(sp_formula) - index_x != 0 and len(sp_formula) - index_x != 2 and len(sp_formula) - index_x != 1:
                b = int(sp_formula[len(sp_formula) - index_x - 3])
                print(b)
                if sp_formula[len(sp_formula) - index_x - 4] == '-':
                    b *= -1
            f.write('1. Найдём координаты вершины параболы\n')
            f.write(f'x₀ = -b / 2a = -({b}) / 2 * ({a}) = {b * -1 / 2 * a}\n')
            x_0 = b * -1 / 2 * a
            print(formula)
            for x in [x_0]:
                y_0 = eval(formula)
            f.write(f'y₀ = {y_0}\n')
            f.write('2. Найдём координаты точек\n')
            sp_y = [eval(formula) for x in [x_0 - 2, x_0 - 1, x_0 + 1, x_0 + 2]]
            f.write(f'y({x_0 - 2}) = {sp_y[0]}\n')
            f.write(f'y({x_0 - 1}) = {sp_y[1]}\n')
            f.write(f'y({x_0}) = {y_0}\n')
            f.write(f'y({x_0 + 1}) = {sp_y[2]}\n')
            f.write(f'y({x_0 + 2}) = {sp_y[3]}\n')
            f.close()
            os.system('resh.txt')

    def back(self):
        self.new = Graphics()
        self.new.show()
        self.close()

    def run(self):  # считывание формулы в диалоговом окне
        name, ok_pressed = QInputDialog.getText(self, "Формула",
                                                "Введите формулу квадратичной функции вида:\n"
                                                "a * x ** 2 + b * x + c")
        if ok_pressed:
            self.label.setText(f'y = {name}')
            self.plot(name)

    def plot(self, formula):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        y = lambda x: eval(formula)  # задаём формулу
        xs = np.linspace(-10, 10, 100)
        sp_y = [eval(formula) for x in xs]
        sp_y.sort()
        min_y = sp_y[0]
        max_y = sp_y[-1]
        if min_y > 1:
            min_y = 1
        # делаем сетку
        ax.set_xticks(np.arange(-10, 11, 5))
        ax.set_xticks(np.arange(-10, 11, 5), minor=True, color='black')
        if min_y % 10 != 0:
            min_y -= min_y % 10
        if max_y % 10 != 0:
            max_y -= 10 - max_y % 10
        ax.set_yticks(np.arange(min_y, max_y, 10))
        ax.set_yticks(np.arange(min_y, max_y, 10), minor=True, color='black')
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        # рисуем оси координат
        ax.plot(0, 0, 'o', color='black')
        ax.plot(np.arange(-11, 11), np.arange(-11, 11) * 0, color='black')
        ax.plot(np.arange(min_y - 1, max_y + 1) * 0, np.arange(min_y - 1, max_y + 1), color='black')
        # рисуем график
        ax.plot(xs, y(xs), color='blue')
        self.canvas.draw()


class Giperbola(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Построение дробно-линейной функции')
        self.initUI()

    def initUI(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 20))
        self.button = QPushButton('Написать формулу')
        self.button.clicked.connect(self.run)
        self.button_1 = QPushButton('Решение')
        self.button_2 = QPushButton(self)
        self.button_2.setText('‹-')
        self.button_2.move(2, 2)
        self.button_2.setMaximumSize(60, 60)
        self.button_2.setFont(QFont('Arial', 20))
        self.button_2.clicked.connect(self.back)
        layout = QVBoxLayout()
        layout.addWidget(self.button_2)
        layout.addWidget(self.canvas)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.button_1)
        self.setLayout(layout)
        self.button_1.clicked.connect(self.resh)

    def resh(self):  # записывание оформления
        if self.label.text() == '':
            return
        else:
            f = open('resh.txt', 'w', encoding="utf-8")
            f.write(f'{self.label.text()} - дробно-линейная функция, график - гипербола\n')
            formula = self.label.text().split('= ')[1]
            sp_formula = self.label.text().split('= ')[1].split(' / ')
            if sp_formula[1] == 'x' and '+' not in sp_formula[1] and '-' not in sp_formula[1] and (
                    'x' not in sp_formula[0]):
                f.write('Асимптоты: x = 0, y = 0\n')
                if int(sp_formula[0]) < 0:
                    f.write('График расположен во 2 и 4 четвертях.\n')
                else:
                    f.write('График расположен во 1 и 3 четвертях.\n')
                f.write('Подставляем любые значения x(кроме 0).')
            else:
                znam = sp_formula[1][1:-1]
                print(znam)
                sp_znam = znam.split()
                if '+' in znam:
                    c = 1
                    if znam[0] != 'x':
                        c = sp_znam[0]
                    as_x = int(sp_znam[-1]) * -1 / int(c)
                elif '-' in znam:
                    c = 1
                    if znam[0] != 'x':
                        c = sp_znam[0]
                    as_x = int(sp_znam[-1]) / int(c)
                else:
                    as_x = 0
                f.write(f'Недопустимое значение: x = {as_x}\n')
                f.write('Подставляем любые допустимые значения x.')

            f.close()
            os.system('resh.txt')

    def back(self):
        self.new = Graphics()
        self.new.show()
        self.close()

    def run(self):  # считывание формулы в диалоговом окне
        name, ok_pressed = QInputDialog.getText(self, "Формула",
                                                "Введите формулу дробно-линейной функции вида:\n"
                                                "(a * x + b) / (c * x + d) или k / x")
        if ok_pressed:
            self.label.setText(f'y = {name}')
            self.plot(name)

    def plot(self, formula):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        y = lambda x: eval(formula)  # задаём формулу
        xs = np.linspace(-10, 10, 100)
        sp_y = [eval(formula) for x in xs]
        sp_y.sort()
        min_y = sp_y[0]
        max_y = sp_y[-1]
        if min_y > 1:
            min_y = 1
        # делаем сетку
        ax.set_xticks(np.arange(-10, 11, 5))
        ax.set_xticks(np.arange(-10, 11, 5), minor=True, color='black')
        if min_y % 5 != 0:
            min_y -= min_y % 5
        if max_y % 5 != 0:
            max_y -= 5 - max_y % 5
        ax.set_yticks(np.arange(min_y, max_y, 5))
        ax.set_yticks(np.arange(min_y, max_y, 5), minor=True, color='black')
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        # рисуем оси координат
        ax.plot(0, 0, 'o', color='black')
        ax.plot(np.arange(-11, 11), np.arange(-11, 11) * 0, color='black')
        ax.plot(np.arange(min_y - 1, max_y + 1) * 0, np.arange(min_y - 1, max_y + 1), color='black')
        # рисуем график
        ax.plot(xs, y(xs), color='green')
        self.canvas.draw()


class Line(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Построение линейной функции')
        self.initUI()

    def initUI(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 20))
        self.button = QPushButton('Написать формулу')
        self.button.clicked.connect(self.run)
        self.button_1 = QPushButton('Решение')
        self.button_1.clicked.connect(self.resh)
        self.button_2 = QPushButton(self)
        self.button_2.setText('‹-')
        self.button_2.move(2, 2)
        self.button_2.setMaximumSize(60, 60)
        self.button_2.setFont(QFont('Arial', 20))
        self.button_2.clicked.connect(self.back)
        layout = QVBoxLayout()
        layout.addWidget(self.button_2)
        layout.addWidget(self.canvas)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.button_1)
        self.setLayout(layout)

    def resh(self):
        sp = []
        sp_y = []
        if self.label.text() == '':
            return
        else:
            f = open('resh.txt', 'w', encoding="utf-8")
            f.write(f'{self.label.text()} - линейная функция, график - прямая\n')
            f.write('x | 0 | 1\n')
            f.write('—————————\n')
            sp = self.label.text().split('= ')
            sp_y = [eval(sp[1]) for x in [0, 1]]
            y1 = ' ' + str(sp_y[0]) + ' '
            if sp_y[0] < 0:
                y1 = str(sp_y[0]) + ' '
            y2 = ' ' + str(sp_y[1]) + ' '
            if sp_y[1] < 0:
                y2 = str(sp_y[1]) + ' '
            f.write(f'y |{y1}|{y2}')
            f.close()
            os.system('resh.txt')

    def back(self):
        self.new = Graphics()
        self.new.show()
        self.close()

    def run(self):  # считывание формулы в диалоговом окне
        name, ok_pressed = QInputDialog.getText(self, "Формула",
                                                "Введите формулу линейной функции вида:\n"
                                                "k * x + b")
        if ok_pressed:
            self.label.setText(f'y = {name}')
            self.plot(name)

    def plot(self, formula):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        y = lambda x: eval(formula)  # задаём формулу
        xs = np.linspace(-10, 10, 100)
        sp_y = [eval(formula) for x in xs]
        sp_y.sort()
        min_y = sp_y[0]
        max_y = sp_y[-1]
        if min_y > 1:
            min_y = 1
        # делаем сетку
        ax.set_xticks(np.arange(-10, 11, 5))
        ax.set_xticks(np.arange(-10, 11, 5), minor=True, color='black')
        if min_y % 5 != 0:
            min_y -= min_y % 5
        if max_y % 5 != 0:
            max_y -= 5 - max_y % 5
        ax.set_yticks(np.arange(min_y, max_y, 5))
        ax.set_yticks(np.arange(min_y, max_y, 5), minor=True, color='black')
        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.5)
        # рисуем оси координат
        ax.plot(0, 0, 'o', color='black')
        ax.plot(np.arange(-11, 11), np.arange(-11, 11) * 0, color='black')
        ax.plot(np.arange(min_y - 1, max_y + 1) * 0, np.arange(min_y - 1, max_y + 1), color='black')
        # рисуем график
        ax.plot(xs, y(xs), color='red')
        self.canvas.draw()


class Quadratic(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qudratic.ui', self)
        self.setWindowTitle('Решение квадратных уравнений')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.count)
        self.pushButton.clicked.connect(self.resh)

    def resh(self):
        os.system('resh.txt')

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def count(self):
        f = open("resh.txt", 'w', encoding="utf-8")  # открываем файл для записи решения
        a = int(self.spinBox.text())
        b = int(self.spinBox_2.text())
        c = int(self.spinBox_3.text())
        znak1 = '+'
        b1 = b
        if b < 0:
            znak1 = '-'
            b1 *= -1
        znak2 = '+'
        c1 = c
        if c < 0:
            znak2 = '-'
            c1 *= -1
        f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = 0\n')
        # проверка на линейность
        if a == 0:
            f.write(f'{str(b)}x {znak2} {str(c1)} = 0\n')
            x = -1 * c / b
            f.write(f'x = {str(-1 * c)} / {b}\n')
            f.write(f'x = {x}')
            self.label_7.setText(f'x = {x}\n')
            f.close()
            return
        # считаем дискриминант
        d = b ** 2 - 4 * a * c
        f.write(f'D = ({str(b)})² - 4 * ({str(a)}) * ({str(c)}) = {str(d)}\n')
        if d < 0:
            self.label_7.setText('Нет корней, так как дискриминант меньше нуля.')
            f.write('Нет корней, так как дискриминант меньше нуля.\n')
        elif d == 0:
            x = (- 1 * b) / (2 * a)
            self.label_7.setText(f'x = {x}')
            f.write(f'x = (-1 * {str(b)}) / (2 * {str(a)}) = {str(x)}\n')
        else:
            x1 = (- 1 * b + d ** 0.5) / (2 * a)
            x2 = (- 1 * b - d ** 0.5) / (2 * a)
            self.label_7.setText(f'x₁ = {x1}   x₂ = {x2}')
            f.write(f'x₁ = (-({str(b)}) + √{str(d)}) / (2 * {str(a)}) = {str(x1)}\n')
            f.write(f'x₂ = (-({str(b)}) - √{str(d)}) / (2 * {str(a)}) = {str(x2)}')
        f.close()


class Decay(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('decay.ui', self)
        self.setWindowTitle('Разложение квадратного трёхчлена на множители')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.count)
        self.pushButton.clicked.connect(self.resh)

    def resh(self):  # открытие решения
        os.system('resh.txt')

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def count(self):
        f = open("resh.txt", 'w', encoding="utf-8")  # открываем файл для записи
        a = int(self.spinBox.text())
        b = int(self.spinBox_2.text())
        c = int(self.spinBox_3.text())
        znak1 = '+'
        b1 = b
        if b < 0:
            znak1 = '-'
            b1 *= -1
        znak2 = '+'
        c1 = c
        if c < 0:
            znak2 = '-'
            c1 *= -1
        f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)}\n')
        # проверка на линейность
        if a == 0:
            self.label_7.setText('Нельзя разложить на множители, так как уравнение линейное.')
            f.write('Нельзя разложить на множители, так как уравнение линейное.')
            f.close()
            return
        # находим корни квадратного уравнения
        f.write('Находим корни квадратного уранения\n')
        f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = 0\n')
        d = b ** 2 - 4 * a * c
        f.write(f'D = ({str(b)})² - 4 * ({str(a)}) * ({str(c)}) = {str(d)}\n')
        if d < 0:
            self.label_7.setText('Нельзя разложить на множители, так как корней нет.')
            f.write('Нельзя разложить на множители, так как корней нет.')
        elif d == 0:
            x = (- 1 * b) / (2 * a)
            f.write(f'x = (-1 * {str(b)}) / (2 * {str(a)}) = {str(x)}\n')
            znak = ''
            if x < 0:
                znak = '+'
                x *= -1
            else:
                znak = '-'
            if a != 1:
                self.label_7.setText(f'{a} * (x {znak} {x})²')
                f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = {a} * (x {znak} {x})²')
            else:
                self.label_7.setText(f'(x {znak} {x})²')
                f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = {a} * (x {znak} {x})²')
        else:
            x1 = (- 1 * b + d ** 0.5) / (2 * a)
            x2 = (- 1 * b - d ** 0.5) / (2 * a)
            f.write(f'x₁ = (-({str(b)}) + √{str(d)}) / (2 * {str(a)}) = {str(x1)}\n')
            f.write(f'x₂ = (-({str(b)}) - √{str(d)}) / (2 * {str(a)}) = {str(x2)}\n')
            znak3 = ''
            if x1 < 0:
                znak3 = '+'
                x1 *= -1
            else:
                znak3 = '-'
            znak4 = ''
            if x2 < 0:
                znak4 = '+'
                x2 *= -1
            else:
                znak4 = '-'
            if a != 1:
                self.label_7.setText(f'{a} * (x {znak3} {x1}) * (x {znak4} {x2})')
                f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = {a} * (x {znak3} {x1}) * (x {znak2} {x2})')
            else:
                self.label_7.setText(f'(x {znak3} {x1}) * (x {znak4} {x2})')
                f.write(f'{str(a)}x² {znak1} {str(b1)}x {znak2} {str(c1)} = (x {znak3} {x1}) * (x {znak4} {x2})')
        f.close()


class Sin_etc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sin_etc.ui', self)
        self.setWindowTitle('Синусы, косинусы, тангенсы, котангенсы')
        self.initUI()

    def initUI(self):
        self.ComboBox.addItems(['sin', 'cos', 'tg', 'ctg'])
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.tabl)
        self.pushButton_3.clicked.connect(self.count)

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def tabl(self):
        os.system('"sin_cos_tg_ctg.xlsx"')

    def count(self):
        corner = int(self.spinBox.text())
        minus_sin = False
        minus_cos = False
        while corner >= 360:
            corner -= 360
        if corner >= 270:
            corner = 360 - corner
            minus_sin = True
        if corner >= 180:
            corner -= 180
            minus_sin = True
            minus_cos = True
        if corner >= 90:
            corner = 180 - corner
            minus_cos = True
        radian = radians(corner)
        if self.ComboBox.currentText() == 'sin':
            if corner == 0:
                self.label.setText('0')
            elif corner == 30:
                if minus_sin:
                    self.label.setText('-' + '1/2')
                else:
                    self.label.setText('1/2')
            elif corner == 45:
                if minus_sin:
                    self.label.setText('-' + '√2/2')
                else:
                    self.label.setText('√2/2')
            elif corner == 60:
                if minus_sin:
                    self.label.setText('-' + '√3/2')
                else:
                    self.label.setText('√3/2')
            elif corner == 90:
                if minus_sin:
                    self.label.setText('-' + '1')
                else:
                    self.label.setText('1')
            else:
                if minus_sin:
                    self.label.setText('-' + str(round(sin(radian), 4)))
                else:
                    self.label.setText(str(round(sin(radian), 4)))
        elif self.ComboBox.currentText() == 'cos':
            if corner == 0:
                if minus_cos:
                    self.label.setText('-' + '1')
                else:
                    self.label.setText('1')
            elif corner == 30:
                if minus_cos:
                    self.label.setText('-' + '√3/2')
                else:
                    self.label.setText('√3/2')
            elif corner == 45:
                if minus_cos:
                    self.label.setText('-' + '√2/2')
                else:
                    self.label.setText('√2/2')
            elif corner == 60:
                if minus_cos:
                    self.label.setText('-' + '1/2')
                else:
                    self.label.setText('1/2')
            elif corner == 90:
                self.label.setText('0')
            else:
                if minus_cos:
                    self.label.setText('-' + str(round(cos(radian), 4)))
                else:
                    self.label.setText(str(round(cos(radian), 4)))
        elif self.ComboBox.currentText() == 'tg':
            if corner == 0:
                self.label.setText('0')
            elif corner == 30:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('√3/3')
                else:
                    self.label.setText('-' + '√3/3')
            elif corner == 45:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('1')
                else:
                    self.label.setText('-' + '1')
            elif corner == 60:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('√3')
                else:
                    self.label.setText('-' + '√3')
            elif corner == 90:
                self.label.setText('-')
            else:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText(str(round(tan(radian), 4)))
                else:
                    self.label.setText('-' + str(round(tan(radian), 4)))
        if self.ComboBox.currentText() == 'ctg':
            if corner == 0:
                self.label.setText('-')
            elif corner == 30:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('√3')
                else:
                    self.label.setText('-' + '√3')
            elif corner == 45:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('1')
                else:
                    self.label.setText('-' + '1')
            elif corner == 60:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText('√3/3')
                else:
                    self.label.setText('-' + '√3/3')
            elif corner == 90:
                self.label.setText('0')
            else:
                if (minus_sin and minus_cos) or (minus_sin is False and minus_sin is False):
                    self.label.setText(str(round(cos(radian) / sin(radian), 4)))
                else:
                    self.label.setText('-' + str(round(cos(radian) / sin(radian), 4)))


class Just_calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.setWindowTitle('Калькулятор для счёта')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.sp = []
        self.primer = []
        self.begin = True
        self.button.clicked.connect(self.back)
        self.btn1.clicked.connect(self.run)
        self.btn2.clicked.connect(self.run)
        self.btn3.clicked.connect(self.run)
        self.btn4.clicked.connect(self.run)
        self.btn5.clicked.connect(self.run)
        self.btn6.clicked.connect(self.run)
        self.btn7.clicked.connect(self.run)
        self.btn8.clicked.connect(self.run)
        self.btn9.clicked.connect(self.run)
        self.btn0.clicked.connect(self.run)
        self.btn_mult.clicked.connect(self.run)
        self.btn_plus.clicked.connect(self.run)
        self.btn_minus.clicked.connect(self.run)
        self.btn_div.clicked.connect(self.run)
        self.btn_dot.clicked.connect(self.run)
        self.btn_pow.clicked.connect(self.run)
        self.btn_sqrt.clicked.connect(self.run)
        self.btn_fact.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_eq.clicked.connect(self.ravno)

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def ravno(self):
        delen = False
        if '/' in self.primer:
            for i in self.primer:
                if i == '/':
                    delen = True
                elif delen:
                    if i != '0':
                        delen = False
        kor = False
        if '**' in self.primer:
            for i in range(len(self.primer)):
                if self.primer[i] == '**':
                    kor = True
                elif kor and self.primer[i] == '0.5':
                    if self.primer[i - 2][0] == '-':
                        break
                    else:
                        kor = False

        if delen or kor:
            self.table.display('error')
            self.primer = []
        else:
            self.table.display(eval(' '.join(self.primer)))
            self.primer = []
            self.primer.append(str(self.table.value()))

    def clear(self):
        self.primer = []
        self.table.display('')

    def run(self):
        if self.begin:
            self.table.display('')
            self.begin = False
        if self.sender().text() == '+':
            self.primer.append('+')
        elif self.sender().text() == '-':
            if not (bool(self.primer)):
                self.minus = True
            self.primer.append('-')
        elif self.sender().text() == '*':
            self.primer.append('*')
        elif self.sender().text() == '/':
            self.primer.append('/')
        elif self.sender().text() == '^':
            self.primer.append('**')
        elif self.sender().text() == '!':
            rez = 1
            for i in range(1, int(self.primer[-1]) + 1):
                rez *= i
            self.primer[-1] = str(rez)
        elif self.sender().text() == '√':
            self.primer.append('**')
            self.primer.append('0.5')
            print(self.primer)
        elif self.sender().text() == '.':
            self.primer[-1] += '.'
            self.table.display(self.primer[-1])
        else:
            if bool(self.primer):
                if self.primer[-1] in ['-', '+', '/', '*']:
                    if len(self.primer) == 1 and self.primer[-1] == '-':
                        self.primer[-1] += self.sender().text()
                    else:
                        self.primer.append(self.sender().text())
                else:
                    self.primer[-1] += self.sender().text()
            else:
                self.primer.append(self.sender().text())
            self.table.display(self.primer[-1])


class Sistem_calc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sistem_calc.ui', self)
        self.setWindowTitle('Калькулятор для перевода в разные системы счисления')
        self.initUI()

    def initUI(self):
        self.sl = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        self.indexes = {'2': '', '8': '', '10': '', '16': ''}
        self.ComboBox.addItems(['2', '8', '10', '16'])
        self.label_3.setText('')
        self.ComboBox_2.addItems(['2', '8', '10', '16'])
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.count)

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def from_des(self, sp, sist2):
        num = int(''.join(map(str, sp)))
        print(num)
        ost = []
        new = ''
        rez = num // sist2
        ost.append(num - rez * sist2)
        while rez >= sist2:
            num = rez
            rez = num // sist2
            ost.append(num - rez * sist2)
        ost.append(rez)
        ost.reverse()
        if sist2 != 16:
            for i in ost:
                new += str(i)
        else:
            for i in ost:
                if i >= 10:
                    for k, v in self.sl.items():
                        if v == i:
                            new += k
                else:
                    new += str(i)
        return new

    def to_des(self, sp, sist1):
        transl_sp = reversed(sp)
        summa = 0
        for index, el in enumerate(transl_sp):
            summa += el * sist1 ** index
        return summa

    def count(self):
        self.label_3.setText('')
        zn = self.lineEdit.text()
        sist1 = int(self.ComboBox.currentText())
        sist2 = int(self.ComboBox_2.currentText())
        sp = [i for i in zn]
        if sist1 == 16:
            for i in range(len(sp)):
                if sp[i].isdigit():
                    if int(sp[i]) >= sist1:
                        self.label_3.setText('Число не соответствует введённой системе счисления.')
                        return
                    else:
                        sp[i] = int(sp[i])
                else:
                    if sp[i] in self.sl.keys():
                        sp[i] = self.sl[sp[i]]
                    else:
                        self.label_3.setText('Число не соответствует введённой системе счисления.')
                        return
        else:
            for i in range(len(sp)):
                if sp[i].isdigit():
                    if int(sp[i]) >= sist1:
                        self.label_3.setText('Число не соответствует введённой системе счисления.')
                        return
                    else:
                        sp[i] = int(sp[i])
                else:
                    self.label_3.setText('Число не соответствует введённой системе счисления.')
                    return
        if sist1 == sist2:
            self.lineEdit_2.setText(zn)
        elif sist1 == 10:
            new = self.from_des(sp, sist2)
            self.lineEdit_2.setText(new)
        elif sist2 == 10:
            new = str(self.to_des(sp, sist1))
            self.lineEdit_2.setText(new)
        else:
            one = str(self.to_des(sp, sist1))
            new_sp = map(int, list(one))
            new = self.from_des(new_sp, sist2)
            self.lineEdit_2.setText(new)


class Theory(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('theory.ui', self)
        self.setWindowTitle('Теория')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.show_theory)
        self.ComboBox.addItems(['Решение квадратных уравнений', 'Разложение квадратного трёхчлена на множители',
                                'Синусы, косинусы, тангенсы и котангенсы',
                                'Тригономерия', 'Перевод в другую систему счисления'])

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def show_theory(self):
        self.new = Picture(self.ComboBox.currentText())
        self.close()
        self.new.show()


class Picture(QDialog):
    def __init__(self, theme):
        super(Picture, self).__init__()
        uic.loadUi('picture.ui', self)
        self.setWindowTitle('Показ теории')
        self.theme = theme
        self.initUI()

    def initUI(self):
        self.label_5.setText(self.theme.capitalize())
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.back)
        self.con = sqlite3.connect('theory.db')
        cur = self.con.cursor()
        picture = cur.execute(f"""SELECT picture FROM theory
                                                WHERE name = '{self.theme}'""").fetchall()
        self.find_id = cur.execute(f"""SELECT notes.id_th FROM notes
                                                                INNER JOIN theory
                                                                ON notes.id_th = theory.id
                                                                WHERE theory.name = '{self.theme}'""").fetchall()
        self.pixmap = QPixmap(picture[0][0])
        self.image = QLabel(self)
        self.image.move(60, 60)
        self.image.setPixmap(self.pixmap)
        count = cur.execute(f"""SELECT open FROM theory
                                                WHERE name = '{self.theme}'""").fetchall()
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.label_4.setText(str(count[0][0]))
        self.draw_tabl()

    def draw_tabl(self):
        cur = self.con.cursor()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.setRowCount(0)
        result = cur.execute(f"""SELECT notes.notes FROM notes
                                                INNER JOIN theory
                                                ON notes.id_th = theory.id
                                                WHERE theory.name = '{self.theme}'""").fetchall()
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def back(self):
        cur = self.con.cursor()
        # прибавляет 1 к количеству вхождений
        cur.execute(f"""UPDATE theory SET open = open + 1 WHERE id = {self.find_id[0][0]}""").fetchall()
        self.con.commit()
        self.new = Theory()
        self.close()
        self.new.show()

    def add(self):
        note = self.plainTextEdit.toPlainText()
        cur = self.con.cursor()

        result = cur.execute(f"""SELECT notes.notes FROM notes
                                                        INNER JOIN theory
                                                        ON notes.id_th = theory.id
                                                        WHERE theory.name = '{self.theme}'""").fetchall()
        if result[0][0] == 'Заметок пока нет':  # заменяет первую заметку
            cur.execute(f"""UPDATE notes SET notes = '{note}' WHERE id_th = {self.find_id[0][0]}""").fetchall()
        else:  # прибавляет заметку
            cur.execute(f"""INSERT INTO notes(id_th,notes) VALUES({self.find_id[0][0]}, '{note}')""").fetchall()
        self.con.commit()
        self.plainTextEdit.clear()
        self.draw_tabl()


class Tests(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tests.ui', self)
        self.setWindowTitle('Тесты')
        self.initUI()

    def initUI(self):
        self.button = QPushButton(self)
        self.button.setText('‹-')
        self.button.move(2, 2)
        self.button.resize(60, 60)
        self.button.setFont(QFont('Arial', 20))
        self.button.clicked.connect(self.back)
        self.pushButton.clicked.connect(lambda: self.open(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.open(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.open(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.open(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.open(self.pushButton_5.text()))

    def back(self):
        self.new = Menu()
        self.new.show()
        self.close()

    def open(self, text):
        with open('tests.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            sp = list(reader)
            for i in sp:
                if i[0] == text:
                    webbrowser.open(i[1])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())