# Strings and text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# String inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

# String inside a string
print("I said: %r." % x)
# String inside a string
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# String inside a string
# This is a fun example of string formatting where the format is set elsewhere and the values are subbed in when printing.
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)