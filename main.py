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
    print("*********** Which are Multiples of: K ************")
    print("**************** Using Digits: D *****************")
    print("**************************************************")
    print('\n')
    
    while True:
        print("**************************************************")
        # Get values for n, m, d
        k = int(input("Enter value for K in the range (1 - 99,999): "))
        digitString = "1 2 3 4 5 6 7 8 9"
        #digitString = input("Enter digit list (D) separated by space (integers 1 - 9): ")
        m = int(input("Enter the size of the palindrome (M): "))
        digitSet = []

        #split digitString and store as a list
        for i in digitString.split():
            digitSet.append(int(i))
        #check n's size
        if k < 1 or k > 99999:
            print("k is out of range")
        else:
            time.sleep(0.1)
            print('\n')
            #palindromes = numPalindromes(n, digitSet, n, m)
            NumPalindromes(k, digitSet, k, m)

            #if palindromes is 0:
            #    print("No solution")
            #else:
                #print("The number of palindromes of size M: ", palindromes)


def M_Transition(initialState, inputSymbol, k):
    return (10 * initialState + inputSymbol) % k


# noinspection SpellCheckingInspection
def NumPalindromes(k, digitSet, startState, m):
    # function to solve problem 2
    # finds string of shortest length that is accepted by the DFA

    retVals = Generate_M(k, digitSet, startState, m)
    print(retVals)
    print("Answer: ")
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

def Generate_M(k, digitSet, startState, m):
    queue = []
    # visited is an array where each index represents a state, and visited[i] gives true or false
    # based on whether state i has been visited
    # initialize
    output  = ""

    visited = [startState]
    parent  = [-1] * (k + 1)
    label   = [-1] * (k + 1)

    queue.append(startState)
    nextState    = -1
    currentState = -1

    count = 1
    
    while len(queue) is not 0:
        currentState = queue.pop(0)
        count+=1
        
        for c in digitSet:
    
            nextState = M_Transition(currentState, c, k)

            if nextState is 0:  # accepting state reached
                visited.append(nextState)
                parent[nextState] = currentState
                label[nextState]  = c

                while nextState != startState:
                    output      += str(label[nextState])
                    nextState    = parent[nextState]
                
                print(output[::-1])
                nextState = int(output[::-1])
                queue.append(nextState)


                output = ""
               
            elif nextState not in visited:
                visited.append(nextState)
                parent[nextState] = currentState
                label[nextState]  = c
                queue.append(nextState)
                
    #return queue
    
def Generate_M_Prime(k, digitSet, startState, m):
    print("in progress")

main()
