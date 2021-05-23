eat_num, meat_or_veg = map(str, input().split())  # 2
eat_num = int(eat_num)
lst_meat_or_veg = list(meat_or_veg)  # 3
lst_num = len(lst_meat_or_veg)

nCr = {}


def cmb(lst_num, eat_num):
    if eat_num == 0 or eat_num == lst_num:
        return 1
    if eat_num == 1:
        return lst_num
    if (lst_num, eat_num) in nCr:
        return nCr[(lst_num, eat_num)]
    nCr[(lst_num, eat_num)] = cmb(
        lst_num-1, eat_num) + cmb(lst_num-1, eat_num-1)
    return nCr[(lst_num, eat_num)]


result = cmb(lst_num, eat_num)
print(result)
