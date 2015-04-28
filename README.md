# Longest substrings

Write a function that returns the length of the longest substring with
no repeating characters in a string.

E.g. the longest non-repeating substring in `'abcabcda'` is `'abcd'`,
which has length 4.

**Don't look at `longestsubstring.py`, which contains two solutions!!!**

## Test harness

There is a simple test harness in `test_longestsubstring.py`. It contains a
function that takes one argument: your function that solves the problem, e.g.
if you have a function `myfunc` in the file `myfile` then you can test it by
doing:

```
>>> import test_longestsubstring
>>> import myfile
>>> test_longestsubstring.test_longestsubstring(myfile.myfunc)
```

If it's correct, you should get:

```
a ... OK!
aa ... OK!
abcabcda ... OK!
dvdx ... OK!
anviaj ... OK!
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456... (truncated) ... OK!
```

## Speed/memory bonus

The final strings in the test harness, which are truncated for output in
the harness, are over 30,000 characters long. One is ordered and drawn
from a large alphabet, and is a worst-case input for most approaches to
this problem. The other is a random sequence of letters.

I wrote two functions, `length_of_longest_substring_slow` and
`length_of_longest_substring`, with very different performance
characteristics!

``` 
In [1]: s_random = open('random_longstring.txt').read()

In [2]: s_ordered = open('ordered_longstring.txt').read()

In [3]: %timeit longestsubstring.length_of_longest_substring_slow(s_random)
10 loops, best of 3: 90.2 ms per loop

In [4]: %timeit longestsubstring.length_of_longest_substring_slow(s_ordered)
1 loops, best of 3: 801 ms per loop

In [5]: %timeit longestsubstring.length_of_longest_substring(s_random)
100 loops, best of 3: 16.7 ms per loop

In [6]: %timeit longestsubstring.length_of_longest_substring(s_ordered)
10 loops, best of 3: 66.4 ms per loop
```

How does your solution do?! If you struggle to get millisecond speed, take a
look at the docstring (the comments at the start) of the faster function,
without looking at the code below. This describes the algorithm. 
