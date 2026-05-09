line1 = input().split()
n = int(line1[0])
m = int(line1[1])

section_1 = [0]*m
section_2 = [0]*m

for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    section_1[a-1] += 1
    section_2[b-1] += 1

for i in range(m):
    print(section_2[i] - section_1[i])
