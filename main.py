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
            palindromes = numPalindromes(n, digitSet, n, m)
            
            if palindromes is 0:
                print("No solution")
            else:
                print("The number of palindromes of size M: ", palindromes)
            print('\n')

def dfaDelta(initialState, inputSymbol, k):
    return (10 * initialState + inputSymbol) % k


# noinspection SpellCheckingInspection
def numPalindromes(k, digitSet, startState, m):
    # function to solve problem 2
    # finds string of shortest length that is accepted by the DFA

    retVals = generateM(k, digitSet, startState, m)
    print(retVals)
    print("Answer: ")
    if not retVals:
        return "No solution"
    return retVals
    '''
    currentState = retVals[0]
    nextState = retVals[1]
    parent = retVals[2]
    label = retVals[3]
    output = ""
    while nextState != startState:
        output += str(label[nextState])
        nextState = parent[nextState]
    return output[::-1]
    '''


def generateM(k, digitSet, startState, m):
    queue = []
    # visited is an array where each index represents a state, and visited[i] gives true or false
    # based on whether state i has been visited
    # initialize
    visited = [startState]
    parent = [-1] * (k + 1)
    label = [-1] * (k + 1)

    queue.append(startState)
    nextState = -1
    currentState = -1

    count = 0
    
    while count < m:
        currentState = queue.pop(0)
        for c in digitSet:
            nextState = dfaDelta(currentState, c, k)
            
            if nextState is 0:  # accepting state reached
                parent[nextState] = currentState
                label[nextState] = c
                returnVals = [currentState, nextState, parent, label]
                return returnVals
            
            if nextState not in visited:
                visited.append(nextState)
                parent[nextState] = currentState
                label[nextState] = c
                queue.append(nextState)
                count+=1
                
    #if nextState != 0:
    #    return False
    return queue
    
def generateM_Prime(k, digitSet, startState, m):


main()
