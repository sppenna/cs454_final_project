'''
CS 454: Final Project

This program will the number of palindromes of size M
that are multiples of number N using as designated
language of digits D.
'''
import sys
import time 

def main():

    print('\n')
    print("**************************************************")
    print("***** Find Number of Palindromes of size: M ******")
    print("*********** Which are Multiples of: N ************")
    print("**************** Using Digits: D *****************")
    print("**************************************************")
    print('\n')
    
    while True:
        # Get values for n, m, d
        n = int(input("Enter value for N in the range (1 - 99,999): "))
        digitString = "1 2 3 4 5 6 7 8 9"
        #digitString = input("Enter digit list (D) separated by space (integers 1 - 9): ")
        m = int(input("Enter the size of the palindrome (M): "))
        digitSet = []

        #split digitString and store as a list
        for i in digitString.split():
            digitSet.append(int(i))
        #check n's size
        if n < 1 or n > 99999:
            print("k is out of range")
        else:
            time.sleep(0.1)
            print('\n')
            palindromes = shortestAcceptedString(n, digitSet, n, m)
            print("The number of palindromes of size M: ", palindromes)
            print('\n')

def dfaDelta(initialState, inputSymbol, k):
    return (10 * initialState + inputSymbol) % k


# noinspection SpellCheckingInspection
def shortestAcceptedString(k, digitSet, startState, m):
    # function to solve problem 2
    # finds string of shortest length that is accepted by the DFA

    retVals = bfs(k, digitSet, startState)

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


def bfs(k, digitSet, startState):
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
        for c in digitSet:
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
