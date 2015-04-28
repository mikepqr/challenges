def length_of_longest_substring(s):
    '''
    Find length of longest substring of s with no repeating characters.

    Uses pointers i and j to search string. Initially i = 0, j = 1.

    1. j is then incremented until the character s[j] occurs in the substring
    s[i:j] -- i.e. we find the end of the non-repeating substring -- or until j
    == len(s). E.g. if s = "anviaj" then j is increased until i = 0, j = 4,
    s[i:j] = "anvi", s[j] = "a".

    2. i is then incremented to be at the position after the character in
    s[i:j] responsible for the collision with s[j], e.g. if s = "anviaj", then
    after step 1, and i = 0, j = 4, then the character s[j] = "a" is
    responsible for the collision, and "a" first occurs at position 0.
    '''

    longest = 0
    i = 0
    j = 1

    while i < len(s) - longest:
        while j < len(s) and s[j] not in s[i:j]:
            j += 1

        longest = max(longest, len(s[i:j]))

        if j < len(s):
            i = s[i:].find(s[j]) + i + 1

    return longest


def length_of_longest_substring_slow(s):
    '''
    Find length of longest substring of s with no repeating characters (SLOW!)

    Uses pointers i and j to search string, and an (ordered) dict to keep track
    of which letters have been seen.

    Initially i = j = 0.

    For each i, increase j until you find a repeat or reach the end of the
    string. Make a note of the length of this substring if it is longer than
    the previously seen longest substring. Then increment i until it is within
    the length of the longest candidate substring of the end of s.
    '''
    longest = 0
    i = 0

    while i < len(s) - longest:
        j = i

        while j < len(s) and s[j] not in s[i:j]:
            j += 1

        longest = max(longest, len(s[i:j]))
        i += 1

    return longest
