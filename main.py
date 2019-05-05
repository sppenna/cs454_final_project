#Finds a multiple of k with a list n of permitted digits.
def SmallestMultiple(k, inputList):
    state = (-1, "")
    queue = []
    parent = {}
    visited = {}
    #list of adjacent nodes
    adjList = map(lambda x: ((int(x)) % int(k), x), inputList)
    state, queue, parent, visited, adjList = BuildAdjList(state, queue, parent, visited, adjList)
    return MinString(state, queue, parent, visited, inputList, k)

#build base adjacency list
def BuildAdjList(state, queue, parent, visited, adjList):
    for adj in adjList:
        if adj[0] not in visited:
            queue.insert(0, adj)
            parent[adj[0]] = state
            visited[adj[0]] = 1
    return state, queue, parent, visited, adjList

#BFS of the adjacent nodes
def MinString(state, queue, parent, visited, inputList, k):
    #initialize empty string
    out = ""
    #Begin BFS
    #go through queue of adjacent possible moves.
    while True:
        if len(queue) <= 0:
            break
        print("queue: ", queue)
        searchNext = queue.pop()
        state = searchNext[0]
        #print("searchNext[0]: ", searchNext[0], " searchNext[1]: ", searchNext[1])
        if state is 0:
            
            #reached an accepting state append the queue to output string until you reach -1
            while searchNext[0] != -1:
                out += str(searchNext[1])
                searchNext = parent[searchNext[0]]
            #reverse the string and return
            return out[::-1]

        else:
            adjList = map(lambda x: ((int(state) * 10 + int(x)) % int(k), x), inputList)
            state, queue, parent, visited, adjList = BuildAdjList(searchNext, queue, parent, visited, adjList)
        
    return "No solution exists"

 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False

def main():
    while True:
        print("************************************")
        print("*** Find The Shortest Palindrome ***")
        print("************************************")
        userKInput = int(input("Enter the number 'k' to find shortest multiple of: "))
        userNInput = input("Enter Numbers Permitted (separated by spaces): ")
        inputList = []
        inputList = userNInput.split(' ')
        out = SmallestMultiple(userKInput, inputList)
        print("Output: " + out + '\n')
    print('\n' + "Closing the Program...")
main()