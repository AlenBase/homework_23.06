def merge(ls1, ls2):
    list = []
    i = 0
    j = 0

    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            list.append(ls1[i])
            i += 1
        else:
            list.append(ls2[j])
            j += 1

    while i < len(ls1):
        list.append(ls1[i])
        i += 1

    while j < len(ls2):
        list.append(ls2[j])
        j += 1

    return list

ls1 = [1, 3, 5, 7, 9, 16, 24]
ls2 = [2, 4, 6, 8, 10, 19, 28]
merged = merge(ls1, ls2)

for k in merged:
    print(k, end=" ")
print()
