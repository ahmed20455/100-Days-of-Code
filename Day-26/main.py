import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for(index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
h_word = str(input("Enter a word: ")).upper()
ans = [nato_dict[letter]  for letter in h_word]
print(ans)
