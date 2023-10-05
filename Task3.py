#Accepts a letter and returns the corresponding score

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
print(getLetterScore("A")) # Shows that for a chosen letter in this case "X", the function calculates the chosen letters score which is 16
print(getLetterScore("")) # If no letter is given the function returns 0 as the score
print(getLetterScore(2))  # The function errors and returns 0 for invalid inputs such as numbers or symbols
print(getLetterScore("!")) # The function returns 0 if there are any invalid inputs even if there are valid letters passed
print(getLetterScore("H1!")) # The function still returns 0 if there are any invalid inputs even if there are valid letters passed
