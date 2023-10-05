# Takes the tiles and dictionary then returns the word with the highest score

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

# This function is taken from Task 4
def getWordScore(word): # Takes a string arguement as an input
  WordScore = 0 # Keeps track of total letter score
  if onlyEnglishLetters(word):
    for letter in word:
     WordScore += int(getLetterScore(letter))
  return WordScore # Returns the total score of each letter in the word added together

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

def findHighestScore(myTiles, dictionary): # Defines the function findHighestScore that takes as parameters the myTiles and a dictionary. The function returns the highest scoring word that could be made from the tiles and is valid in the dictionary and the corresponding words score.
  try:
    assert isinstance(myTiles, list) == True, "Error: myTiles must be a list"
    assert isinstance(dictionary, list) == True, "Error: dictionary must be a list"
  
    topWord = "" # Defines the variable topWord as an empty string
    topScore = 0 # Defines the variable topScore as the int 0
    
    for word in dictionary: # Loops through every word in the dictionary. This method is more efficent then testing against every combination of tiles
      if canBeMade(word, myTiles): # Checks if the word can be made with the tiles. This is more efficent than running isValid() as all words will already be of a valid data type and are inside the dictionary
        wordScore = getWordScore(word) # Defines the variable wordScore as the words score, calculated with the function getWordScore
        if topScore <= wordScore: # Checks if the current word has a higher score than highest recorded word found so far
          topWord = word # Sets the value of the variable topWord to the new top scoring word
          topScore = wordScore # Sets the value of the variable topScore to the new score of the new top scoring word
    return topWord, topScore # Returns the topWord and the topScore
    
  except AssertionError as error: # Handles errors catched by assertions
    print(error)
    return "", 0

# Test Cases:
print(findHighestScore(["H", "E", "L", "L", "O"], ["HELLO", "WORLD", "LOL"])) # Valid inputs
# Output: ('HELLO', 12)
print(findHighestScore([], ["HELLO", "WORLD"])) # No tiles so no word can be made
# Output: ('', 0)
print(findHighestScore({}, ["HELLO", "WORLD"])) # Tiles wrong data type, must be a list
# Output: ('', 0) -> Error: myTiles must be a list
print(findHighestScore([], [])) # No tiles and no words in the dictionary so no word can be made
# Output: ('', 0)
print(findHighestScore(["H", "E", "L", "L", "O"], {})) # Dictionary wrong data type, must be a list
# Output: ('', 0) -> Error: dictionary must be a list
print(findHighestScore(["H", "E", "L", "O"], ["HELLO", "WORLD"])) # No words can be made from the tiles that is in the dictionary
# Output: ('', 0)
