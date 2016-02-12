# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import random


def get_layout():
    layout = raw_input('Enter the minefield layout: ')
    fields = layout.split(',')
    grid = len(fields)

    # check if the ip was correct
    for f in fields:
        if len(f) != grid:
            print 'Not a correct minefield layout! Game over!'
            exit(0)

    field = []
    for row in xrange(grid):
        field.append(['x'] * grid)
    return field


def get_option():
    op = raw_input('Enter an option: ')
    return int(op[2]), int(op[4]), op[0]


death = False
mine_field = get_layout()
print '\ngiven mine field \n'
print mine_field
print '\n'
mines = 2  # random.randint(0, len(mine_field)-1)
mine_blocks = {}
for mine in xrange(mines):
    mine_blocks[mine] = [random.randint(0, len(mine_field)-1), random.randint(0, len(mine_field)-1)]
mine_blocks = mine_blocks.values()
while not death:
    try:
        op1, op2, flag = get_option()
    except:
        print 'wrong option! \n'
        continue
    if flag == 'o':
        for mine in mine_blocks:
            if [op1, op2] in mine_blocks:
                death = True
                print 'Oops, you stepped on a mine! Game over!'
                exit(0)
    try:
        mine_field[op1][op2] = flag
    except IndexError:
        print 'wrong option given!'
        continue
    except:
        print 'Wrong option given!'
        continue
    count = 0
    for g in mine_field:
        if 'x' not in g:
            count += 1
        if count == len(mine_field):
            print 'Wow you cleared the minefield! Game over'
            exit(0)
    print '\n mine field now'
    print mine_field
    print '\n'
