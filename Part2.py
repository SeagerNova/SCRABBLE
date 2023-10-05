import os

def setupList(fileName): # Function that takes a fileName and returns a formatted list of the contents of the file.
  try:
    assert fileName != "", "Error: Filename not valid."
    assert os.path.splitext(fileName)[1] == ".txt", "Error: File extension not .txt"
    file = open(fileName, "r") # Opens the file specified in the parameters in read mode
    outputList = file.read().splitlines() # Defines the variable outputList as the list of the contents of the file split at the line breaks.
    file.close() # Closes the file
    return outputList # Returning the list
  except FileNotFoundError: # Handles errors caused by the file not existing  
    print("Error: The file could not be found.")
    return []
  except AssertionError as error: # Handles errors caused by assertions
    print(error)
    return []
  except:
    print("Error: An unexpected error occurred.")
    return []

# Test Cases:
print(setupList("epic.txt")) # The file doesn't exist
# Output: [] -> Error: The file could not be found.
print(setupList("")) # Invalid file name (empty string)
# Output: [] -> Error: Filename not valid.
print(setupList("epic.json")) # Wrong file extension
# Output: [] -> Error: File extension not .txt
print(setupList(3664)) # Invalid file name (integer)
# Output: [] -> Error: An unexpected error occurred.
print(setupList("tiles.txt")) # Valid filename
# Output: ['B', 'A', 'N', ..., 'E', 'N']

def setupDict(fileName): # Function that takes a fileName and returns a formatted dict of the contents of the file.
  try:
    assert fileName != "", "Error: Filename not valid."
    assert os.path.splitext(fileName)[1] == ".txt", "Error: File extension not .txt"
    outputDict = {} # Defines a new dictionary, outputList
    file = open(fileName, "r") # Opens the file specified in the parameters in read mode
    for line in file: # Looping through all the lines of the file
      formatted_line = line.strip().split(" ") # Creates a list formed of the content of the line, with the letter and the corresponding score
      outputDict[formatted_line[0]] = formatted_line[1] # Adds the letter to the dictionary, outputDict, with the letter being the key, and the score being the value
    file.close() # Closes the file
    return outputDict # Returning the dictionary
  except FileNotFoundError: # Handles errors caused by the file not existing  
    print("Error: The file could not be found.")
    return {}
  except AssertionError as error: # Handles errors catched by assertions
    print(error)
    return []
  except:
    print("Error: An unexpected error occurred.")
    return {}

# Test Cases:
print(setupDict("epic.txt")) # The file doesn't exist
# Output: [] -> Error: The file could not be found.
print(setupDict("")) # Invalid file name (empty string)
# Output: [] -> Error: Filename not valid.
print(setupDict("epic.json")) # Wrong file extension
# Output: [] -> Error: File extension not .txt
print(setupDict(3664)) # Invalid file name (integer)
# Output: [] -> Error: An unexpected error occurred.
print(setupDict("scores.txt")) # Valid filename
# Output: {'A': '1', 'B': '3', 'C': '5', ..., 'Y': '8', 'Z': '20'}

Tiles = setupList("tiles.txt") # Defines the list, Tiles, with the contents of the file tiles.txt
Dictionary = setupList("dictionary.txt") # Defines the list, Dictionary, with the contents of the file dictionary.txt
Scores = setupDict("scores.txt") # Defines the dictionary, Scores, with the contents of the file scores.txt


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
    
# Test Cases:
print(getLetterScore("X")) # Shows that for a chosen letter in this case "X", the function calculates the chosen letters score which is 16
print(getLetterScore("")) # If no letter is given the function returns 0 as the score
print(getLetterScore(2))  # The function errors and returns 0 for invalid inputs such as numbers or symbols
print(getLetterScore("!")) # The function returns 0 if there are any invalid inputs even if there are valid letters passed
print(getLetterScore("H1!")) # The function still returns 0 if there are any invalid inputs even if there are valid letters passed

    
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
  

import random # Imports the random package
def generateTiles(): # Defines the new function generateTiles, that returns a randomly generated list of 7 letter tiles. 
  copiedTiles = Tiles.copy() # Copies the tiles array, so when elements are removed it doesn't effect the main Tiles list
  myTiles = [] # Defines the new empty list, myTiles
  for i in range(7): # Iterates through 7 times, for each tile to be generated
    try:
      randomLetter = random.choice(copiedTiles) # Picks a random letter from the list copiedTiles and defines it as the variable randomLetter
      copiedTiles.remove(randomLetter) # Removes the random letter from the list copiedTiles, so that letter can't be picked again
      myTiles.append(randomLetter) # Adds the random letter to the list of tiles
    except IndexError: # Handles errors caused by index errors
      return "Error: Tiles list is empty"
  return myTiles # Returns the list of tiles

print("Generating Random Tiles...")
myTiles = generateTiles() # Defines the variable, myTiles as a list of 7 random letters, calculated with the generateTiles function
if isinstance(myTiles, str): # Checks if an error code was returned
  print(myTiles) # Prints the error
  exit() # Quits the program
print("Tiles: " + " ".join(myTiles))
print("Scores: ", end = "")
for tile in myTiles: # Iterates through each tile in the myTile list, calculates the score of the corresponding tile, and prints it
  print(getLetterScore(tile) + " ", end="")
print("\n")

while True:
  wordinput = input("Enter a word: ") # Asks the user to input a word as defines it as the variable wordinput
  if wordinput != "&&&": # If the response isn't &&& then the program should continue
    validBool, stringResponse = isValid(wordinput, myTiles, Dictionary) # Checks if the word input is valid, can be made with all the tiles, and is part of the dictionary. The boolean response to these checks are defined as the variable validBool, and the string description that will be displayed to the user is defined as the variable stringResponse
    if validBool: # If the checks are valid
      print(stringResponse)
      print("Score for this word is " + str(getWordScore(wordinput))) # Prints the score of the user inputted word, which is calculated with the getWordScore function
      BestWord, BestScore = findHighestScore(myTiles, Dictionary) # Calls the function findHighestScore which finds the best possible word with the tiles provided. Defines the best word to the variable BestWord, and the corresponding score of the top word to BestScore
      print("The best potential word is " + BestWord + " with a score of " + str(BestScore))
      break # Stops the program as the user has found a valid word
    print(stringResponse + "\n") # Outputs the reason why the users inputted word is invalid
  else: # The user has inputted &&&, so the program stops
    print("Thanks for using this application, better luck next time!!!")
    break
