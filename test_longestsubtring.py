def test_longest_substring(f):
    tests = [('a', 1),
             ('aa', 1),
             ('abcabcda', 4),
             ('dvdx', 3),
             ('anviaj', 5),
             (open('longstring.txt').read(), 95)]

    for s, desired_result in tests:
        if len(s) > 60:
            s_ = s[0:60] + "... (truncated)"
        else:
            s_ = s

        actual_result = f(s)

        try:
            assert actual_result == desired_result
            print s_, "... OK!"
        except AssertionError:
            print "{0}(\"{1}\") = {2}. Should be {3}!".format(
                f.func_name, s_, str(actual_result), str(desired_result))
            raise
