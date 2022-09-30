import random

called_guess = input("guess a letter:\n").lower()

word_list = ["fish", "lion", "tiger"]

choosen = random.choice(word_list)
print(choosen)
print("="*100)
for i in choosen:
    if i == called_guess:
        print("Right")
    else:
        print("False")
