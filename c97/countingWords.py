introString = input('Enter your name\n')
wordCount = 1
characterCount = 0
for i in introString:
    characterCount+=1
    if(i == ' '):
        wordCount+=1
print(characterCount)
print(wordCount)
