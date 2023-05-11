# THIS CODE IS TO COUNT THE NUMBER OF VOWELS IN A WORD

word = input("Type in the word: ")
vowels = 0

for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels = vowels + 1

print("The number of vowels in", word, "are", vowels)