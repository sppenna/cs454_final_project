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
    k = int( input("enter a number k: ") )
    m = int( input("enter length of palindrome m: ") )

    print("finding palindrome of size: ", m, ", that is a multiple of: ", k)
    count = 0

    while True:
        
        if isPalindrome( str(k*count) ) and len(str(k*count)) == m:
            
            print(k*count)

        elif len( str(k*count) ) > m:
            break
        
        count += 1
main()