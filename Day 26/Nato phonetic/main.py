import pandas

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
word = input("Enter a word: ")

#TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet = {row["letter"].lower(): row["code"] for (index, row) in data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
letter_word = [letter.lower() for letter in word]
# result = [val for (key, val) in nato_phonetic_alphabet.items() if key in letter_word ]
result = [nato_phonetic_alphabet[letter] for letter in letter_word]
print(result)
