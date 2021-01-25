# C問題

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
first = input()
last = input()
tmp = input()

result = 'false'

is_first_coming = False
for alphabet in alphabets:
    if first == alphabet:
        is_first_coming = True

    if is_first_coming and tmp == alphabet:
        result = 'true'

    if last == alphabet:
        break

print(result)
