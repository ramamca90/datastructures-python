def LCS(i, s1, j, s2):
    if (i, j) in memory:
        return memory[(i, j)]

    if i == len(s1) or j == len(s2):
        output = 0

    elif s1[i] == s2[j]:
        output = 1 + LCS(i + 1, s1, j + 1, s2)

    else:
        output = max(LCS(i + 1, s1, j, s2), LCS(i, s1, j + 1, s2))

    memory[(i, j)] = output

    return output


def DP_LCS(s1, s2):
    table = [[0 for i in range(len(s1)) for j in range(len(s2))]]
    print(table)


s1 = "stone"
s2 = "longest"
memory = {}
print(DP_LCS(s1, s2))
