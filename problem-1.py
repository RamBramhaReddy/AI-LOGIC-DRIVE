def merge(inter):

    for i in range(len(inter)):
        for j in range(i + 1, len(inter)):
            if inter[i][1] >= inter[j][0]:
                inter[i][1] = max(inter[i][1], inter[j][1])
                inter.pop(j)
                return merge(inter)

    return inter
n = int(input())
inter = []
for i in range(n):
    start, end = map(int, input().split())
    inter.append([start, end])
result = merge(inter)
for interval in result:
    print(interval[0], interval[1])
