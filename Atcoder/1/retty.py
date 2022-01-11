def solution(A):
    mother_collection = [i for i in range(1, 100001)]

    for num in A:
        if num > 0 and mother_collection[num - 1] == i:
            mother_collection.remove(num)

    result = min(mother_collection)
    return result
