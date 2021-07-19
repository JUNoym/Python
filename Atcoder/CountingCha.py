cnt = [0]*26

while True:
    try:
        s = input().lower()

        for i in range(len(s)):
            num = ord(s[i]) - ord('a')
            if num >= 0 and num <= 25:
                cnt[num] += 1
    except:
        break

for i in range(26):
    print('{0} : {1}'.format(chr(i+ord('a')), cnt[i]))
