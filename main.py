#Generate the number of palindromes of size n that are divisible by number k
def SmallestMultiple(k, n):
    state = (-1, "")
    queue = []
    parent = {}
    visited = {}
    #list of adjacent nodes
    adjList = map(lambda x: ((int(0) * 10 + int(x)) % int(k), x), n)
    state, queue, parent, visited, adjList = BuildAdjList(state, queue, parent, visited, adjList)
    return MinString(state, queue, parent, visited, n, k)

#build base adjacency list
def BuildAdjList(state, queue, parent, visited, adjList):
    for adj in adjList:
        if adj[0] not in visited:
            queue.insert(0, adj)
            parent[adj[0]]  = state
            visited[adj[0]] = 1
    return state, queue, parent, visited, adjList

def MinString(state, queue, parent, visited, n, k):
    #initialize empty string
    out = ""
    #Begin BFS
    #go through queue of adjacent possible moves.
    while True:
        if len(queue) <= 0:
            break
        searchNext = queue.pop()
        state      = searchNext[0]
    
        if state != 0:
            adjList = map(lambda x: ((int(state) * 10 + int(x)) % int(k), x), n)
            state, queue, parent, visited, adjList = BuildAdjList(searchNext, queue, parent, visited, adjList)
        else:
            #reached an accepting state append the queue to output string until you reach -1
            while searchNext[0] != -1:
                out += str(searchNext[1])
                searchNext = parent[searchNext[0]]
            #reverse the string and return 
            return out[::-1] 
    
    return "No solution exists"

def main():
    print('\n')
    while True:
        #Generate the number of palindromes of size n that are divisible by number k
        print("Find the number of Palindromes ")
        userKInput = int( input("Enter the number (k) to find shortest multiple of: ") )
        userNInput = int( input("Length of palindrome? (n): ") )
        out = SmallestMultiple(userKInput, userNInput)
        print("Output: " + out + '\n')
    print('\n' + "Closing the Program...")
main()