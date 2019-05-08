# Tyler Kaim, Warren Goodson
# Project 01


import sys
def main():
    dfa = {0: {'a': 1, 'b': 2, 'c':3},
           1: {'a': 4, 'b': 5, 'c': 6},
           2: {'a': 7, 'b': 8, 'c': 9},
           3: {'a': 10, 'b': 11, 'c': 12},
           4: {'a': 38, 'b': 13, 'c': 14},
           5: {'a': 15, 'b': 16, 'c': 17},
           6: {'a': 18, 'b': 19, 'c': 20},
           7: {'a': 21, 'b': 22, 'c': 23},
           8: {'a': 24, 'b': 39, 'c': 25},
           9: {'a': 27, 'b': 26, 'c': 28},
           10: {'a': 29, 'b': 30, 'c': 31},
           11: {'a': 32, 'b': 33, 'c': 34},
           12: {'a': 35, 'b': 36, 'c': 40},
           13: {'a': 37, 'b': 37, 'c': 17},
           14: {'a': 37, 'b': 19, 'c': 37},
           15: {'a': 37, 'b': 37, 'c': 23},
           16: {'a': 37, 'b': 37, 'c': 25},
           17: {'a': 27, 'b': 26, 'c': 28},
           18: {'a': 37, 'b': 30, 'c': 37},
           19: {'a': 32, 'b': 33, 'c': 34},
           20: {'a': 37, 'b': 36, 'c': 37},
           21: {'a': 37, 'b': 37, 'c': 14},
           22: {'a': 37, 'b': 37, 'c': 17},
           23: {'a': 18, 'b': 19, 'c': 20},
           24: {'a': 37, 'b': 37, 'c': 23},
           25: {'a': 27, 'b': 37, 'c': 37},
           26: {'a': 32, 'b': 37, 'c': 37},
           27: {'a': 29, 'b': 30, 'c': 31},
           28: {'a': 35, 'b': 37, 'c': 37},
           29: {'a': 37, 'b': 13, 'c': 37},
           30: {'a': 15, 'b': 16, 'c': 17},
           31: {'a': 37, 'b': 19, 'c': 37},
           32: {'a': 21, 'b': 22, 'c': 23},
           33: {'a': 24, 'b': 37, 'c': 37},
           34: {'a': 27, 'b': 37, 'c': 37},
           35: {'a': 37, 'b': 30, 'c': 37},
           36: {'a': 32, 'b': 37, 'c': 37},
           37: {'a': 37, 'b': 37, 'c': 37},
           38: {'a': 37, 'b': 37, 'c': 37},
           39: {'a': 37, 'b': 37, 'c': 37},
           40: {'a': 37, 'b': 37, 'c': 37}
           }

    task = input("Do you want to use problem 1 or 2?\n1 for Problem 1, 2 for Problem 2, or q for quit\n")

    while task != 'q':
        if task == '1':
            size = int(input("Enter length for n: "))
            calculate(dfa, size)
            print('\n')

        elif task == '2':
            # Do problem 2
            print("2")

        else:
            print("Invalid option, exiting")
            sys.exit()
        task = input("Do you want to use problem 1 or 2?\n1 for Problem 1, 2 for Problem 2, or q for quit\n")


def calculate(dfa, size):
    #function to calculate problem 1
    _length = len(dfa);
    _next = []
    _prev = []

    for i in range(_length):
        if i != 37:
            _prev.append(1)
        else:
            _prev.append(0)

    for n in range(size):
        for j in range(_length):
            first = _prev[dfa[j]['a']]
            second = _prev[dfa[j]['b']]
            third = _prev[dfa[j]['c']]

            total = first + second + third
            _next.append(total)

        _prev = _next
        _next = []

    print(_prev[0])

main()