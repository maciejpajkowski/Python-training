# https://www.practicepython.org/exercise/2014/03/12/06-word-lists.html

word = input("Please enter a word: ").lower()
length = len(word)
if (word[0:length] == word[::-1]):
    print(word, "is a palindrome!")
else:
    print(word, "is not a palindrome :(")

input("Press enter to quit...")