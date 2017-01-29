def is_palindrome(s):
    '''
    Returns True if s is a palindrome, else returns False. Ignores punctuation
    and whitespace.

    TODO: Fix me!
    '''
    return True


def test_is_palindrome(function):
    tests = [("a", True),
             ("a.", True),
             ("Aa", True),
             ("1234321", True),
             ("911", False),
             ("race a car", False),
             ("A man, a plan, a canal: Panama", True)]

    for s, desired_result in tests:
        actual_result = function(s)
        try:
            assert actual_result == desired_result
            print s, "... OK!"
        except AssertionError:
            print "{0}(\"{1}\") = {2}. Should be {3}!".format(
                function.func_name, s, str(actual_result), str(desired_result))
            raise


def mikes_solution(s):
    s_ = ''.join([l.lower() for l in s if l.isalnum()])
    return (s_ == s_[::-1])


def efficient_solution(s):
    i, j = 0, len(s) - 1
    s = s.lower()

    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
