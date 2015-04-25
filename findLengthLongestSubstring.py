# NOT DONE!  Have to fix: start unique char each time


def findLengthLongestSubstring(myString):
    uniqueString = ''.join(set(myString))
    maxSubstring = ""
    for char in uniqueString:
        currSubstring = ""
        newCharString = myString[myString.find(char):]
        for letter in newCharString:
            if letter in currSubstring:
                currSubstring = letter
            else:
                currSubstring += letter
                print currSubstring
                if len(currSubstring) > len(maxSubstring):
                    maxSubstring = currSubstring
    print(maxSubstring)
    return(len(maxSubstring))
