# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import random


class Grid:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.valid_values = ['0', '1', '2', 'm']
        self.field = self.build_grid()

    def build_grid(self):
        f = []
        for i in xrange(self.n):
            row = []
            for j in xrange(self.m):
                c = Cell(self.valid_values[random.randint(0, 3)], 'closed', 'x')
                row.append(c)
            f.append(row)
        return f

    def show(self):
        psudo_field = []
        for i in xrange(len(self.field)):
            psudo_field.append([])
            for j in xrange(len(self.field[i])):
                psudo_field[i].append(self.field[i][j].view)
        return psudo_field

    def open_cell(self, f1, f2):
        value = None
        if self.field[f1][f2].status == 'closed':
            self.field[f1][f2].status = 'open'
            self.field[f1][f2].view = 'O'
            value = self.field[f1][f2].value
        return value


class Cell:
    def __init__(self, value, status, view):
        self.value = value
        self.status = status
        self.view = view

    def is_mine(self):
        return self.value == 'm'


def main():
    cells = []
    grid = Grid(3, 3)
    print grid.show()
    # print grid.open_cell(2,2)

main()