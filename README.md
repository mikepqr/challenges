# Palindromes

"A man, a plan, a canal: Panama" is a palindrome, while "race a car" is not a palindrome.

Write code that returns True if a string is a palindrome, and False if not. You should ignore whitespace and punctuation.

For the purposes of this exercise, "a" is a palindrome and "a." is a palindrome.

# Test harness

Here's a simple test harness. Your job is to fix the function is_palindrome. You can check it by calling the function test_is_palindrome().

```
def is_palindrome(s):
    '''
    Returns True if s is a palindrome, else returns False.
    TODO: Fix me!
    '''
    return True


def test_is_palindrome():
    tests = [("a", True),
             ("a.", True),
             ("Aa", True),
             ("A man, a plan, a canal: Panama", True),
             ("race a car", False)]

    for s, desired_result in tests:
        print s,
        assert isPalindrome(s) == desired_result
        print "...OK!"
```

# Help!

If this is tough and you're not sure where to start, here's one way to do it step-by-step:

1. Write a function that removes all whitespace from a string
2. Write a function that removes all punctuation from a string
3. Write a function that reverses a string

If you followed steps 1, 2 and 3, you have all the pieces you need to solve this problem.

# Bonus

## Speed/memory

Imagine running your code on a very long string, perhaps millions of characters long (I'll send one of these after lunch!). Is there a way to avoid making copies of the string? Are there situations in which you can avoid checking the entire string?


## Software engineering

Did you find the algorithm easy? OK, now do this "properly". These things are probably overkill for this project, but great habits to get into:
 - Check everything into git with commit messages that are meaningful to other people
 - ...and upload it to github
 - Run your code through https://github.com/google/yapf to see what changes are needed to make it PEP8 compliant
 - Change my simple test harness to be a 'real' nosetest, pytest or unittest:
	 - https://nose.readthedocs.org/en/latest/
	 - http://pytest.org/latest/
	 - https://docs.python.org/2/library/unittest.html
 - Make your code a class as you see fit
 - Make your code an installable Python module, e.g.
	 - http://www.scotttorborg.com/python-packaging/index.html
	 - https://python-packaging-user-guide.readthedocs.org/en/latest/
