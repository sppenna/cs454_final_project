import sys
import time 

def main():

   # task = input("\n")
    print("*************************************************")
    print("***** Find Number of Palindromes of size N ******")
    print("*********** Which are Multiples of K ************")
    print("*************************************************")
    while True:
        # Do problem 2
        k = int(input("Enter value for k in the range [1, 99999]: "))
        alphaString = input("Enter alphabet symbols separated by space (integers 1 - 9): ")
        alphabet = []
        for i in alphaString.split():
            alphabet.append(int(i))
        if k < 1 or k > 99999:
            print("k is out of range")
        else:
            #print("Performing BFS on the DFA... (this may take a while, please be patient)")
            time.sleep(0.1)
            solution = shortestAcceptedString(k, alphabet, k)
            print(solution)

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
