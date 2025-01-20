"""Lerato Moholo
22 September 2024
Rightalign.py
Program where a user can enter a list of strings press DONE then the output is a list of strings right aligned with the longest string
"""

def Enter_strings(): 
    stringList = []                        #Empty list
    print("Enter strings (end with DONE):")
    while True:
        currentString = input()
        if currentString == "DONE":
            break
        stringList.append(currentString)         #if currentString is not 'DONE' add currentString to list
    return stringList

def longest_str(stringList):
    # Find the length of the longest string
    longest = len(max(stringList, key=len))  
    
    # Right-align strings
    for string in stringList:
        emptySpace = longest - len(string)  # Calculate spaces needed to right-align
        print(' ' * emptySpace + string)  # Right-align the string

def main():
    names = Enter_strings()
    print('\nRight-aligned list:')
    if names:
        longest_str(names)

main()