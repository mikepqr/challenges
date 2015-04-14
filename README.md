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
>>> test_longestsubstring(myfile.myfunc)
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

The final string in the test harness, which is truncated for output in the
harness, is over 30,000 characters long. I wrote two functions with very
different performance characteristics!

```
In [4]: s = open('longstring.txt').read()

In [5]: %timeit longestsubstring.length_of_longest_substring(s)
10 loops, best of 3: 79.8 ms per loop

In [6]: %timeit longestsubstring.length_of_longest_substring_slow(s)
1 loops, best of 3: 4.25 s per loop
```

How does your solution do?! If you struggle to get millisecond speed, take a
look at the docstring (the comments at the start) of the faster function,
without looking at the code below. This describes the algorithm. 
