count = [0] * 26

while True:
    try:
        strings = input().lower()
        for i in range(len(strings)):
            num = ord(strings[i]) - ord('a')
            if num >= 0 and num <= 25:
                count[num] += 1
    except:
        break

for i in range(26):
    print('{0}:{1}'.format(chr(i+ord('a')), count[i]))
