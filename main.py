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
    print("**************************************************")
    print( "***** Find Number of Palindromes of size: M ******" )
    print( "*********** Which are Multiples of: K ************" )
    print( "**************** Using Digits: D *****************" )
    print( "**************************************************" )
    print( '\n' )
    
    while True:
        print( "**************************************************" )
        # Get values for n, m, d
        k = int( input( "Enter value for K in the range (1 - 99,999): ") )
        digitString = "1 2 3 4 5 6 7 8 9"
        #digitString = input("Enter digit list (D) separated by space (integers 1 - 9): ")
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
            #palindromes = numPalindromes(n, digitSet, n, m)
            NumPalindromes( k, digitSet, k, m )


def M_Transition(initialState, inputSymbol, k):
    return ( 10 * initialState + inputSymbol ) % k


def NumPalindromes(k, digitSet, startState, m):
    # finds a list of viable palindromes of size m
    # calls Generate_M to do this evaluation
    Generate_M( k, digitSet, startState, m )

    print("Answer: ")


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
    output  = ""

    visited = [startState]
    parent  = [-1] * ( k + 1 )
    label   = [-1] * ( k + 1 )

    queue.append( startState )
    nextState    = -1
    currentState = -1

    count = 1
    
    while len(queue) is not 0:
        
        currentState = queue.pop(0)
        count += 1

        for c in digitSet:
            # generate a M transition for each digit in your digitList
            nextState = M_Transition( currentState, c, k )

            if nextState is 0:  # accepting state reached

                parent[nextState] = currentState
                label[nextState]  = c

                while nextState != startState:
                    output      += str( label[nextState] )
                    nextState    = parent[nextState]

                print(output[::-1])
                nextState = int( output[::-1] )
                #print("visited: ", visited)
                #print("nextState: ", nextState)
                #print("queue: ", queue)
                output = ""

            # If state has not been visited
            # add the state to the move queue
            elif nextState not in visited: 
                # Adjacent saves the nextState to the queue and saves its parent
                visited, parent, label, queue = Adjacent( visited, parent, label, queue,
                                                          c, currentState, nextState )

    print( queue )


def M_Prime_Transition(k, digitSet, startState, m):
    print("in progress(M_Prime_Transition)...")


def Generate_M_Prime(k, digitSet, startState, m):
    print("in progress(Generate_M_Prime)...")


main()
