import string

# s = """\
#     Hi $name.

#     $contents

#     Have a good day
# """

with open('template.txt', 'r') as f:
    t = string.Template(f.read())
contents = t.substitute(name='Jun', contents='My Blog')
print(contents)
