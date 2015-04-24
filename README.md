# Make change

Write code to make change for a purchase. 

Your code should accept two parameters: the amount of money offered in
cents, and the cost of the item in cents. So you should be able to do
`make_change(100, 66)` to calculate the change required if someone buys
something that costs 66 cents using a dollar bill.

Your code should not simply return the total change: it should return
the _coins_ required! So `make_change(100, 66)` should not just return
`34`! It should return a quarter, a dime and four pennies!

## Design decisions

The main design decision you'll face is what data structure to use to
represent a collection of coins! One possibility is a dictionary, e.g.

```
>>> make_change(100, 66)
{25: 1, 5: 1, 1: 4}
```

But there is probably a better option that more naturally represents the
data, and makes it easier to do some of the calculations you're likely
to need! [Here's a
clue](https://docs.python.org/2/library/collections.html)!

## Test harness

Come up with some test cases! Think about edge cases (e.g. when the
change is zero, when the change is 100) and errors (e.g. when the change
is negative).

Look at the test harness for longest-substring for an example of how to
implement a quick test harness.
