import random

guess = input("Guess a word?\n").lower()
word_list = ["Hiu", "Lion", "Harimau", "Anaconda"]
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"
print(display)

print(f"animal name is {chosen_word}", f"and length of the name is {len(str(chosen_word))}")


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)  