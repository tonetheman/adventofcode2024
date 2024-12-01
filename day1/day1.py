
filename = "input.txt"
# filename = "sample.txt"

data = open(filename,"r").readlines()

l1 = []
l2 = []
s2 = {}

for d in data:
    tmp = d.split()
    l1.append(int(tmp[0]))
    l2.append(int(tmp[1]))  

    # needed for part two
    if int(tmp[1]) not in s2:
        s2[int(tmp[1])] = 1
    else:
        s2[int(tmp[1])] += 1

l1.sort()
l2.sort()

# part one
total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])

print(total)

# part two
total = 0
for i in range(len(l1)):
    num1 = int(l1[i])
    num2 = int(l2[i])
    if num1 in s2:
        total += (num1*s2[num1])
print(total)