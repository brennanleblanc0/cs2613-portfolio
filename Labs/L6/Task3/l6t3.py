def given_length(msg : str, wordLen : int):
    tokens = msg.split()
    correctLen : list = []
    for e in tokens:
        if (len(e) == wordLen):
            correctLen.append(e)
    return correctLen

def longest_word(msg : str):
    tokens = msg.split()
    longest : list = []
    longest.append(tokens[0])
    for e in tokens:
        if (len(e) > len(longest[0])):
            longest.clear()
            longest.append(e)
        elif (len(e) == len(longest[0])):
            longest.append(e)
    return longest

def most_common(msg : str):
    msg = msg.lower()
    charCount : list = [0] * 26
    for e in msg:
        if (ord(e) >= 97 and ord(e) <= 122):
            charCount[ord(e) - 97] += 1
    largeIndex : list = []
    largeIndex.append(0)
    i = 0
    while i < 26:
        if (charCount[i] > charCount[largeIndex[0]]):
            largeIndex.clear()
            largeIndex.append(i)
        elif (charCount[i] == charCount[largeIndex[0]]):
            largeIndex.append(i)
        i += 1
    for e in range(len(largeIndex)):
        largeIndex[e] = chr(largeIndex[e] + 97)  
    return largeIndex

f = open("L6_T3_Text.txt", 'r')
fileContent : str = ""
for x in f:
    fileContent += x

print("Number of words of length 5: ", len(given_length(fileContent, 5)))
print("Most common letters: ", most_common(fileContent))
print("Longest words: ", longest_word(fileContent))