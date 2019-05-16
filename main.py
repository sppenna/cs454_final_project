'''
CS 454: Final Project

This program will the number of palindromes of size M
that are multiples of number K using as designated
language of digits D.
'''
import sys
import time 

def main():
    print('\n')
    print( "**************************************************" )
    print( "***** Find Number of Palindromes of size: M ******" )
    print( "*********** Which are Multiples of: K ************" )
    print( "**************** Using Digits: D *****************" )
    print( "**************************************************" )
    print( '\n' )
    
    while True:
        print( "**************************************************" )
        # Get values for n, m, d
        k = int( input( "Enter value for K in the range (1 - 99,999): ") )
        #digitString = "1 2 3 4 5 6 7 8 9"
        digitString = input("Enter digit list (D) separated by space (integers 1 - 9): ")
        m = int( input("Enter the size of the palindrome (M): ") )
        digitSet = []

        #split digitString and store as a list
        for i in digitString.split():
            digitSet.append( int(i) )
        #check n's size
        if k < 1 or k > 99999:
            print( "k is out of range" )
        else:
            time.sleep( 0.1 )
            print( '\n' )
            NumPalindromes( k, digitSet, k, m )


def M_Transition(initialState, inputSymbol, k):
    return ( 10 * initialState + inputSymbol ) % k


def NumPalindromes(k, digitSet, startState, m):
    # finds a list of viable palindromes of size m
    # calls Generate_M to do this evaluation
    dfa = Generate_M( k, digitSet, startState, m )
    
    print("DFA M:\n")
    for i in range(len(dfa)):
        print(i, ":" , dfa[i])
    print('\n')


def Adjacent(visited, parent, label, queue, c, currentState, nextState):
    # Helper function saves the nextState to the move queue and
    # saves its parent as currentState
    visited.append( nextState )
    parent[nextState] = currentState
    label[nextState]  = c
    queue.append( nextState )

    return visited, parent, label, queue


def Generate_M(k, digitSet, startState, m):
    # Generates a list of numbers that are a multiple of k.
    # this will be used to transition to M_Prime
    queue = []
    # visited is an array where each index represents a state, and visited[i] gives true or false
    # based on whether state i has been visited
    # initialize
    output = ""

    visited = [startState]
    parent = [-1] * (k + 1)
    label = [-1] * (k + 1)

    queue.append(startState)
    nextState = -1
    currentState = -1

    count = 1
    dfa = {}
    _next = []
    _prev = []
    #Generate DFA M. |d| transitions for each state
    for i in range(m):
        dfa[i] = {}
        for c in digitSet:
            dfa[i][c] = M_Transition(i, c, k)

    '''
    for n in range(k):
        for j in range(len(dfa)):
            first = _prev[dfa[j]['1']]
            second = _prev[dfa[j]['2']]
            third = _prev[dfa[j]['3']]

            total = first + second + third
            _next.append(total)

        _prev = _next
        _next = []

    print(_prev[0])
    '''
    return dfa
    
    
 
def M_Prime_Transition(k, digitSet, state, m, dfa):
    print("in progress(M_Prime_Transition)...")
    for i in range(k):
        for c in digitSet:
            if dfa[1][c] == state:
                return 1


def Generate_M_Prime(k, digitSet, startState, m):
    print("in progress(Generate_M_Prime)...")


main()
