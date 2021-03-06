'''
CS 454: Final Project

This program will the number of palindromes of size M
that are multiples of number K.
'''
import sys
import time 
import numpy as np

def main():
    print( '\n' )
    print( "**************************************************" )
    print( "***** Find Number of Palindromes of size: M ******" )
    print( "*********** Which are Multiples of: K ************" )
    print( "**************************************************" )
    print( '\n' )
    
    while True:
        print( "**************************************************" )
        # Get values for n, m, d
        k = int( input( "Enter value for K in the range (1 - 99,999): " ) )
        digitString = "0 1 2 3 4 5 6 7 8 9"
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
    dfa, palindromes = Generate_M( k, digitSet, startState, m )
        
    print( "Number of Palindromes: ", len( np.unique(palindromes) ) )
    print('\n')
        
    yn = input( "Display Palindromes? (y/n): ")
    if yn is 'Y' or 'y':
        print( np.unique(palindromes) )
        print('\n')

    yn = input( "Display the DFA? (y/n): " )
    if yn is 'Y' or 'y':
        print("DFA M:\n")

        for i in range(1, len(dfa)):
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
    # Generate DFA M. |d| transitions for each state
    dfa = {}
    _next = []
    _prev = []

    i = 1
    solutionList = []

    if m % 2 is 0:
        x = m//2
    else:
        x = m//2 + 1
    
    while len(str(i)) <= x:
    
        dfa[i] = {}
        for c in digitSet:
            dfa[i][c] = M_Transition(i, c, k)
            if len(str(i)) is x:
            #   if M_Transition(i, c, k) is 0:
                #if i is not 0:
                solutionList.append( str(i) )
                #elif c is not 0:
                #    solutionList.append(str(c))
    
        i += 1
    
    final = []
    for i in solutionList:
        if m % 2 is 0:
            i += i[::-1]
            if int(i) % k is 0:
                final.append(i)
        else:
            i += i[0:-1]
            if int(i) % k is 0:
                final.append(i)

    #print( len( np.unique(final) ) )
    #print(solutionList)
    # Find the the amount of m sized numbers that are accepting in
    # DFA M
    '''
    solution = []
    for n in range(m):
        var = []
        for j in range(len(dfa)):
            for c in digitSet:
                if dfa[j][c] is 0:
                    print("test")
    '''                

        #prev  = _next
        #_next = []
    
    #print(len(solution))
    #for i in solution:
    #    print(i)
    #print(_prev[0])
    
    return dfa, final
    
    
 
def M_Prime_Transition(k, digitSet, state, m, dfa):
    print("in progress(M_Prime_Transition)...")
    for i in range(k):
        for c in digitSet:
            if dfa[1][c] == state:
                return 1


def Generate_M_Prime(k, digitSet, startState, m):
    print("in progress(Generate_M_Prime)...")


main()
