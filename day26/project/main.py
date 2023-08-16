# day 25 project - nato phonetic alphabet

import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

npa_dict = {row.letter:row.code for (index, row) in df.iterrows()}

word = input('enter a word: ').upper()

code_word_list = [npa_dict[letter] for letter in word]

print(code_word_list)

