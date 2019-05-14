import sys

word = sys.stdin.read()
word.lower()
letter = {}
for i in range(97, 123):
    letter[chr(i)] = word.count(chr(i))
letter = sorted(letter.items())
print(letter)
print(len(word))
