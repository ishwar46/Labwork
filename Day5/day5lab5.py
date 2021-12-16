#Write a Python program that accepts a word from the user and reverse it.

word = input("Input a word: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

