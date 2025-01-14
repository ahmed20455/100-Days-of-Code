import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for(index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato():
  h_word = str(input("Enter a word: ")).upper()
  try:
    ans = [nato_dict[letter]  for letter in h_word]
  except KeyError:
    print("Sorry, only letters are in the alphabet")
  else:
    print(ans)
nato()
