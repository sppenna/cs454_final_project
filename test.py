def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

def isNotIn(d, k):
    for i in str(k):
            if int(i) not in d:
                return False

    return True

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
        k = int( input("enter a number k: ") )
        m = int( input("enter length of palindrome m: ") )
        dString = input("Enter digit list separated by space (integers 1 - 9): ")
        out = []

        #split digitString and store as a list
        d = []
        for i in dString.split():
            d.append(int(i))

        print("finding palindrome of size: " + str(m) + ", that is a multiple of: " + str(k) )
        print("using only digits in language: ", d, '\n')
        print("Generating DFA. This may take a couple minutes...")
        count = 0

        while True:
            
            if isPalindrome( str(k*count) ) and len(str(k*count)) == m and isNotIn(d, k*count):             
                out.append(k*count)

            elif len( str(k*count) ) > m:
                break
            
            count += 1
        
        #output
        print('\n')
        print("Number of palindromes of size " + str(m) + ": ",  len(out) )
        if input("print the list of palindromes? (y/n) ") == "y":
            print(out)
        print('\n')

main()