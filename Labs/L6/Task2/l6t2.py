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



print(given_length("The white cat and the red fox.", 3))
print(given_length("This is a test string that will return a list of two a's.", 1))
print(longest_word("Hello CS2613! Python is fun."))
print(longest_word("Hello CS2613 - Python is fun."))
print(most_common("My name is..."))
print(most_common("This is!"))
