def pairs_sum_to_target(list1, list2, target):
    pairs = []
    for index1, i in enumerate(list1):
        for index2, j in enumerate(list2):
            if i + j == target:
                pairs.append([index1, index2])

    return pairs

list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

print(pairs_sum_to_target(list1, list2, target))