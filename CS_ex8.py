letter = str(input("Please input a character: "))
letter = letter.upper()
if len(letter) > 1:
    print("This is not a single character")
    exit(0)
elif len(letter) == 0:
    print("You haven't input a character")
    exit(0)
vowels = ['A', 'E', 'I', 'O', 'U']
consonants = []
abc = list(map(chr, range(65, 90)))
for i in abc:
    if i not in vowels:
        consonants.extend(i)
if letter in consonants:
    print("Input letter is consonant")
elif letter in vowels:
    print("Input letter is vowel")
else:
    print("Input is not letter")