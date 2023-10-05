#Accepts a word and returns a total score of that word if the entire word is a valid input

# This will be defined in Task 1 by the scores.txt file
Scores = {
  'A': 1,
  'B': 3,
  'C': 5,
  'D': 3,
  'E': 1,
  'F': 5,
  'G': 4,
  'H': 3,
  'I': 1,
  'J': 10,
  'K': 8,
  'L': 3,
  'M': 5,
  'N': 3,
  'O': 2,
  'P': 5,
  'Q': 20,
  'R': 3,
  'S': 3,
  'T': 2,
  'U': 1,
  'V': 10,
  'W': 12,
  'X': 16,
  'Y': 8,
  'Z': 20
}

# This function is taken from Task 2
def onlyEnglishLetters(word): #Takes a string input (word) and returns a boolean value based on if the string contains only letters or not
  if type(word) != str: # Handles incorrect types
    return False #Returns false if not a string
  if word.isalpha(): # Checks if word contains only letters (A-Z)
    return True #Returns True if the word contains only english letters
  return False #Otherwise returns False

# This function is taken from Task 3
def getLetterScore(letter):
  try:
    assert type(letter) == str, "Input must be a letter" 
    # check if letter is string - assert or return 0 if not a string
    letter = letter.capitalize() # Ensures inputs correspond to Scores dictionary (Capital letters)
    if letter in Scores:
      return Scores[letter] # If letter is in Scores, return the corresponding score, else give no score.
    else:
      return 0
      
  except AssertionError: # Handles errors catched by assertions
    print("Error: Letter not a string")
    return 0

def getWordScore(word): # Takes a string arguement as an input
  WordScore = 0 # Keeps track of total letter score
  if onlyEnglishLetters(word):
    for letter in word:
     WordScore += int(getLetterScore(letter))
  return WordScore # Returns the total score of each letter in the word added together

#Test Cases:
print(getWordScore("HelLO")) # Inputs containing a mixture of lower and uppercase letters are valid. Returns 12
print(getWordScore("123")) # Function returns 0 for invalid inputs
print(getWordScore("xyz")) # Checks for words that are not in the dictionary. Returns 44
