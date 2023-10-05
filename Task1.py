# This program loads the content of the files into a variable in the respective data types (list, dict)

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
