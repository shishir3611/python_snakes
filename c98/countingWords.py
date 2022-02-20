'''def greet(name):
    print("Hello, "+name+". How are you?")
    
greet('Shishir')'''

def countWords():
    fileName = input('enter file name:\n')
    files = open(fileName, 'r')

    wordNum=0
    for line in files:
        words = line.split()
        wordNum = wordNum + len(words)
        
    print("Number of words: "+str(wordNum))
countWords()