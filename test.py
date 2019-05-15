def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

def main():
    print('\n')
    print("**************************************************")
    print("***** Find Number of Palindromes of size: M ******")
    print("*********** Which are Multiples of: K ************")
    print("**************************************************")
    print('\n')
    while True:
        print("**************************************************")
        k = int( input("enter a number k: ") )
        m = int( input("enter length of palindrome m: ") )
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        out = []

        print("finding palindrome of size: " + str(m) + ", that is a multiple of: " + str(k) )
        count = 0

        while True:
            
            if isPalindrome( str(k*count) ) and len(str(k*count)) == m:
                
                out.append(k*count)

            elif len( str(k*count) ) > m:
                break
            
            count += 1

        print( len(out) )
        if input("print list? (y/n) ") == "y":
            print(out)
        print('\n')

main()