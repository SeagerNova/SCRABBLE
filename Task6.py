# Accepts three parameters (word, myTiles, dictionary) and returns true if the word meets all three rules listed in the program specification

# This function is taken from Task 2
def onlyEnglishLetters(word): #Takes a string input (word) and returns a boolean value based on if the string contains only letters or not
  if type(word) != str: # Handles incorrect types
    return False #Returns false if not a string
  if word.isalpha(): # Checks if word contains only letters (A-Z)
    return True #Returns True if the word contains only english letters
  return False #Otherwise returns False

# This function is taken from Task 5
def canBeMade(word, myTiles):  #Defines the function canBeMade which takes as input a word and the list, myTiles
  if onlyEnglishLetters(word) == False or type(myTiles) != list: # Checks input types are correct
    return False #Returns False if either of the inputs are the incorrect object types
  copiedTiles = myTiles.copy()
  for letter in word:
    letter = letter.upper()
    if letter in copiedTiles:
      # Removes any letter that appears in myTiles to check for duplicates
      copiedTiles.remove(letter)
    else:
      return False # If letter is not in myTiles the word is impossible so it returns False
  return True # If it passes all checks True is returned

def isValid(word, myTiles, dictionary): # Defines the function isValid that takes as parameters the word, myTiles and the dictionary and returns a True/False bool response that corresponds to if the word is valid and also returns a string reason to be displayed to the user
  try:
    assert isinstance(myTiles, list) == True, "Error: myTiles must be a list"
    assert isinstance(dictionary, list) == True, "Error: dictionary must be a list"
    if onlyEnglishLetters(word): # Checks if the word is the user word input is valid
      if canBeMade(word, myTiles): # Checks if the user inputted word can be made with the tiles
        if word.upper() in dictionary: # Checks if the user inputted word is in the dictionary
          return True, "You got it right, this is a valid word!" # Returns that the word is valid
        return False, "There is no such word in the dictionary." # Returns that the word is invalid as its not in the dictionary
      return False, "Your word cannot be made with the tiles avaliable." # Returns that the word is invalid as it cannot be made with the tiles
    return False, "Only use English letters..." # Returns that the word is invalid as it is not made with english letters
  except AssertionError as error: # Handles errors catched by assertions
    return False, str(error)

# Test Cases:
print(isValid("hello", ["H", "E", "L", "L", "O"], ["HELLO", "WORLD"])) # Valid word, as word can be made from the tiles and is in the dictionary
# Output: (True, 'You got it right, this is a valid word!')
print(isValid("/s", [], ["HELLO", "WORLD"])) # Not valid as / is not an english letter
# Output: (False, 'Only use English letters...')
print(isValid("", [], ["HELLO", "WORLD"])) # Not valid due to empty string
# Output: (False, 'Only use English letters...')
print(isValid("hello", {}, ["HELLO", "WORLD"])) # Not valid as myTiles is wrong datatype (not list)
# Output: (False, 'Error: myTiles must be a list')
print(isValid("hello", ["H", "E", "L", "L", "O"], {})) # Not valid as dictionary is wrong datatype (not list)
# Output: (False, 'Error: dictionary must be a list')
print(isValid("hello", ["H", "E", "L", "O"], ["HELLO", "WORLD"])) # Not valid as word cannot be made with the tiles
# Output: (False, 'Your word cannot be made with the tiles avaliable.')
print(isValid("helo", ["H", "E", "L", "O"], ["HELLO", "WORLD"])) # Not valid as word not in the dictionary
# Output: (False, 'There is no such word in the dictionary.')
