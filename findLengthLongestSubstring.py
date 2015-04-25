def findLengthLongestSubstring(mystring):
    currSubstring = ""
    maxSubstring = ""
    for letter in myString:
        if letter in currSubstring:
            currSubstring = ""
        else:
            currSubstring += letter
            if len(currSubstring) > len(maxSubstring):
                maxSubstring = currSubstring
    return(len(maxSubstring))
