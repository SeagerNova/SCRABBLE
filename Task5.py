# Returns a boolean that if a given word can be made with the tiles available

# This function is taken from Task 2
def onlyEnglishLetters(word): #Takes a string input (word) and returns a boolean value based on if the string contains only letters or not
  if type(word) != str: # Handles incorrect types
    return False #Returns false if not a string
  if word.isalpha(): # Checks if word contains only letters (A-Z)
    return True #Returns True if the word contains only english letters
  return False #Otherwise returns False

def canBeMade(word, myTiles):  #Defines the function canBeMade which takes as input a word and the list, myTiles
  if onlyEnglishLetters(word) == False or type(myTiles) != list: # Checks input types are correct
    return False #Returns False if either of the inputs are the incorrect object types
  copiedTiles = myTiles.copy()
  for letter in word:
    letterLow = letter.lower()
    letterUp = letter.upper()
    if letterLow in copiedTiles:
      # Removes any lowercase instance of the letter that appears in myTiles to check for duplicates
      copiedTiles.remove(letter)
    elif letterUp in copiedTiles:
      #Does the same but for uppercase instances of the letter
      copiedTiles.remove(letterUp)
    else:
      return False # If letter is not in myTiles the word is impossible so it returns False
  return True # If it passes all checks True is returned

#Test Cases:
print(canBeMade("WORD", ["W", "O", "R", "D", "A"])) #All chars in word exist in myTiles
#Output: True
print(canBeMade("WERD", ["W", "O", "R", "D", "A"])) #Word contains a letter not in myTiles
#Output: False
print(canBeMade("WorD", ["W", "O", "R", "D", "A"])) #Word contains letters from myTiles and a mix of cases
#Output: True
print(canBeMade(["W", "O", "R", "D", "A"], 24)) #Incorrect Types
#Output: False
print(canBeMade("WorD", ["W", "&", "R", "D", "A"])) #Word contains letters from myTiles and a mix of cases. "&" Symbol causes invalid input
#Output: False
print(canBeMade("W&rD", ["W", "&", "R", "D", "A"])) # Word contains invalid character
# Output: False
print(canBeMade("word", ['W', 'O', 'R', 'D', '&'])) # Word can be made out of the tiles
# Output: True
