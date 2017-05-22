# ^ matches the beginning of a string.
# $ matches the end of a string.
# \b matches a word boundary.
# \d matches any numeric digit.
# \D matches any non-numeric character.
# (x|y|z) matches exactly one of x, y or z.
# (x) in general is a remembered group. We can get the value of what matched by using the groups() method of the object returned by re.search.
# x? matches an optional x character (in other words, it matches an x zero or one times).
# x* matches x zero or more times.
# x+ matches x one or more times.
# x{m,n} matches an x character at least m times, but not more than n times.
# ?: matches an expression but do not capture it. Non capturing group.

import re
#re.sub
str1 = "regular expression"
op = re.sub('ula','l',str1)
print ("replaced sring",op[0])
print("count", op[1])