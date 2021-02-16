# C問題　占い

username = input()
user_num = int(input())
dict = {}

for i in range(user_num):
    name_blood = input().split()
    dict[name_blood[0]] = name_blood[1]
# print(dict)

blood_num = int(input())
dict2 = {}

for i in range(blood_num):
    blood_luck = input().split()
    dict2[blood_luck[0]] = blood_luck[1]
# print(dict2)

for k, v in dict.items():
    if username == k:
        tmp = v

        print(dict2[tmp])
