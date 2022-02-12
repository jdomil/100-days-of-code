import pandas as pd

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Introduce a word: ")
phonetic_result = [phonetic_dict[letter] for letter in user_input.upper()]
print(phonetic_result)
