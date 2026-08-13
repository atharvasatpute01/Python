# Strings cannot be changer after they are created.

# Incorrect

# text = "Python"
# text[0] = "J"

# Output : TypeError: 'str' object does not support item assignment


# Correct

text = "Python"
text = "Jython"

print(text)