# Returns if a given word is a valid data input

def onlyEnglishLetters(word): #Takes a string input (word) and returns a boolean value based on if the string contains only letters or not
  if type(word) != str: # Handles incorrect types
    return False #Returns false if not a string
  if word.isalpha(): # Checks if word contains only letters (A-Z)
    return True #Returns True if the word contains only english letters
  return False #Otherwise returns False
 
# An alternate shorter version of the above function
def onlyEnglishLettersM2(word):
  return ((type(word) == str) and word.isalpha()) #The value of this statement will only be True if the word is both a string and only English letters, otherwise it will return False

#Test Cases:
print(onlyEnglishLetters('HELLO')) #Word made of only english letters
#Output: True
print(onlyEnglishLetters('HeLLo')) #Word made of only english letters with mixed cases
#Output: True
print(onlyEnglishLetters('HE LLO')) #Word containing a space
#Output: False
print(onlyEnglishLetters('HE3LLO')) #Word containing a letter
#Output: False
print(onlyEnglishLetters('WOO!!')) #Word containing special characters
#Output: False
print(onlyEnglishLetters(234)) #Incorrect data type
#Output: False
