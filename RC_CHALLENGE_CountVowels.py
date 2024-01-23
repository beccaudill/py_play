'''
COUNT THE NO. OF VOWELS IN A STRING
DO NOT INCLUDE 'Y'
1/12/2024, Rebecca Caudill
'''

# List of vowels
vList = ["a","e","i","o","u"]

# Pass in the entered word
# Count the number of vowels using the list count method
# Return the count value
def countVowels(x):
    i = 0
    vCnt = 0
    while i < len(x):
        vCnt += vList.count(x[i])
        i += 1
    rCnt = "The vowel count is {0} in \'{1}\'."
    print(rCnt.format(vCnt, strInput))

# Ask user for input
# Confirm input is a word before calling function for vowel count
# If not a word, ask user to input again
print("Enter a word:")
strInput = input()
strLower = strInput.lower()
j = 0
while j < 1:
    if strInput.isalpha():
        j = 1
        countVowels(strLower)
    else:
        print("Input is not a string; please try again.")
        strInput = input()
        strLower = strInput.lower()
    
