import math

def AND(p1, p2):
    i, j = 0, 0
    result = []

    skip1 = int(math.sqrt(len(p1)))
    skip2 = int(math.sqrt(len(p2)))

    while i < len(p1) and j < len(p2):

        if p1[i] == p2[j]:
            result.append(p1[i])
            i += 1
            j += 1

        elif p1[i] < p2[j]:
            # try skipping in p1
            if i + skip1 < len(p1) and p1[i + skip1] <= p2[j]:
                i += skip1
            else:
                i += 1

        else:
            # try skipping in p2
            if j + skip2 < len(p2) and p2[j + skip2] <= p1[i]:
                j += skip2
            else:
                j += 1

    return result


def OR(p1, p2):
    return sorted(list(set(p1) | set(p2)))


def NOT(p, total_docs):
    all_docs = set(range(1, total_docs + 1))
    return sorted(list(all_docs - set(p)))