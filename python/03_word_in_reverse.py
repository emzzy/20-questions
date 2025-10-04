user_input = input("Enter a word: ")

input_length = len((user_input))
reversed_word = user_input[input_length:: -1]

print(reversed_word)