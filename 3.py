def johnson_trotter(elements):
    elements.sort()
    permutation = list(elements)
    directions = [-1] * len(permutation)
    result = [permutation.copy()]
    mobile_index = find_mobile(permutation, directions)
    while mobile_index != -1:
        mobile_element = permutation[mobile_index]
        next_index = mobile_index + directions[mobile_index]
        swap(permutation, directions, mobile_index, next_index)
        result.append(permutation.copy())
        for i in range(len(permutation)):
            if permutation[i] > mobile_element:
                directions[i] = -directions[i]
        mobile_index = find_mobile(permutation, directions)
    return result

def find_mobile(perm, dir):
    mobile_index = -1
    for i in range(len(perm)):
        if (i + dir[i] >= 0 and i + dir[i] < len(perm)):
            if perm[i] > perm[i + dir[i]]:
                if mobile_index == -1 or perm[i] > perm[mobile_index]:
                    mobile_index = i
    return mobile_index

def swap(perm, dir, i, j):
    perm[i], perm[j] = perm[j], perm[i]
    dir[i], dir[j] = dir[j], dir[i]

n = ['математика', 'русский', 'информатика']
for i in range(3):
    l = n.copy()
    el = l.pop(i)
    for j in johnson_trotter(l):
        print(el, ' '.join(j))
