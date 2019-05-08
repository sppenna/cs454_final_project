# Tyler Kaim, Warren Goodson
# Project 01
# CS 454 Spring 2019
# Dr. Ravikumar

import sys
import time


def main():
    dfa = {0: {'a': 1, 'b': 2, 'c': 3},
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
            alphaString = input("Enter alphabet symbols separated by space (integers 1 - 9): ")
            alphabet = []
            for i in alphaString.split():
                alphabet.append(int(i))
            k = int(input("Enter value for k in the range [1, 99999]: "))
            if k < 1 or k > 99999:
                print("k is out of range")
            else:
                print("Performing BFS on the DFA... (this may take a while, please be patient)")
                time.sleep(0.1)
                solution = shortestAcceptedString(k, alphabet, k)
                print(solution)

        else:
            print("Invalid option, exiting")
            sys.exit()
        task = input("Do you want to use problem 1 or 2?\n1 for Problem 1, 2 for Problem 2, or q for quit\n")


def calculate(dfa, size):
    # function to calculate problem 1
    _length = len(dfa)
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


def dfaDelta(initialState, inputSymbol, k):
    return (10 * initialState + inputSymbol) % k


# noinspection SpellCheckingInspection
def shortestAcceptedString(k, alphabet, startState):
    # function to solve problem 2
    # finds string of shortest length that is accepted by the DFA

    retVals = bfs(k, alphabet, startState)

    print("Answer: ")

    if not retVals:
        return "No solution"

    currentstate = retVals[0]
    nextstate = retVals[1]
    parent = retVals[2]
    label = retVals[3]
    output = ""
    while nextstate != startState:
        output += str(label[nextstate])
        nextstate = parent[nextstate]
    return output[::-1]


def bfs(k, alphabet, startState):
    queue = []
    # visited is an array where each index represents a state, and visited[i] gives true or false
    # based on whether state i has been visited
    # initialize
    visited = [startState]
    parent = [-1] * (k + 1)
    label = [-1] * (k + 1)

    queue.append(startState)
    nextstate = -1
    currentstate = -1

    while queue:
        currentstate = queue.pop(0)
        for c in alphabet:
            nextstate = dfaDelta(currentstate, c, k)
            if nextstate == 0:  # accepting state reached
                parent[nextstate] = currentstate
                label[nextstate] = c
                returnVals = [currentstate, nextstate, parent, label]
                return returnVals
            if nextstate not in visited:
                visited.append(nextstate)
                parent[nextstate] = currentstate
                label[nextstate] = c
                queue.append(nextstate)
    if nextstate != 0:
        return False


main()
