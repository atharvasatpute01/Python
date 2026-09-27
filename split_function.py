# The split() Function

# Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)

print(x)




# Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)

print(x)