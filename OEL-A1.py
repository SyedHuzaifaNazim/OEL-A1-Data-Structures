"""""
Open-Ended Lab Task 2:
Objective:
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest Palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Submission Requirements:
Submit the program code along with comments explaining key sections of your implementation.
Optional: Submit screenshots of sample outputs or visualizations if implemented.

Examples:
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""""

def long_paldme(a:str) -> int:
    num = {}
    #It will count each character in the string
    for char in a:
        if char in num:
            num[char] +=1
        else:
            num[char] = 1
    #The length of the longest palindrome is stored in the variable of len
    len=0
    odd_fnd = False
    #Iterating through the character counts
    for count in num.values():
        #If the count is even, it can fully contribute to the palindrome
        if count % 2 == 0:
            len +=count
        #If the count is odd, one less than the count can contribute to the palindrome
        else:
            len += count - 1
            odd_fnd = True
    #If any odd count was found, we can add one to the length for the center character
    if odd_fnd:
        len += 1
    return len

#Given explaination usage of the given example
if __name__ == "__main__":
    a1 = "abccccdd"
    print(f"Input: {a1}\nOutput: {long_paldme(a1)}")
    a2 = "a"
    print(f"Input: {a2}\nOutput: {long_paldme(a2)}") 
    #User input for checking the program dynamically:
    a3 = input("Enter a string to find the longest palindrome length: ")
    print ("You entered the string: ", a3)
    print("The length of the longest palindrome that can be built is: ", long_paldme(a3))