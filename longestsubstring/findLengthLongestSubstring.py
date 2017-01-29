def findLengthLongestSubstring(myString):
    maxSubstring = ""
    currSubstring = ""
    rightIndex = 0
    leftIndex = 0
    #crawl out to the right until you find a repeat
    while rightIndex < len(myString):
        if myString[rightIndex] not in currSubstring:
            currSubstring += myString[rightIndex]
            rightIndex += 1
            if len(currSubstring) > len(maxSubstring):
                maxSubstring = currSubstring
        #when you find a repeat crawl in from left until you find the char that caused the repeat
        else:
            repeat = myString[rightIndex]
            repeatFound = 0
            while not repeatFound: 
                if myString[leftIndex] == repeat:
                    repeatFound = 1
                    currSubstring = myString[leftIndex + 1 : rightIndex]
                leftIndex += 1             

    print(maxSubstring)
    return(len(maxSubstring))
