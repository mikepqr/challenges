def cleaner(mystring):
    #This function cleans the string i.e. gets it into the format we want
    
    #first strip spaces and convert all to lowercase
    mystring = mystring.strip().lower()

    #remove unwanted chars
    cleanstring = ""
    unwantedChars = """ `~!@#$%^&*()-_=+'"[]{}\|;:,<>./?"""
    for char in mystring:
        if char not in unwantedChars:
            cleanstring += char
    return cleanstring

def is_palindrome(mystring):
    #This function tests if a string is a palindrome, ignoring whitespace and punctuation
    
    #first clean your string
    cleanstring = cleaner(mystring)
    
    #set your string length and default to True
    stringLength = len(cleanstring)
    isapalindrome = True
    
    #move in from left and right one by one and set to false if you find a nonmatch
    fromLeft = 0
    fromRight = stringLength - 1
    while fromLeft < (stringLength/2):
        if cleanstring[fromLeft] != cleanstring[fromRight]:
            print mystring + "isn't  a palindrome"
            print "Here's why: " + cleanstring[fromLeft] + "!= " + cleanstring[fromRight]
            isapalindrome = False
            break
        else:
            fromLeft += 1
            fromRight -= 1           
    
    return isapalindrome
