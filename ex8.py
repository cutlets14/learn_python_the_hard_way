# Printing, printing
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# The output from the last print statement looks like this:
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
# There is a mixture of single and double quotes used because in the third element, a single quote is used as an apostrophe.
# Therefore, Python uses double-quotes to avoid having to escape the single-quotes and so on.