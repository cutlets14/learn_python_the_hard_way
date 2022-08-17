# What was that?
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Excape sequences and format strings
dope = 'dope'
print("This is \nkinda %s." % dope)

# %r - converts any Python object into a String using repr() -> print the way you'd like to write in your file
# %s - converst any Python object into a String using str() -> print the way you'd like to see it