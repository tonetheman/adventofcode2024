
# filename = "sample.txt"
filename = "input.txt"
data = open(filename,"r").read()

print(data)

import re
P = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
matches = P.findall(data)

total = 0
PP = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
for m in matches:
    print(m,PP.match(m).groups())
    (a,b) = PP.match(m).groups()
    a=int(a)
    b=int(b)
    print(a*b)
    total += a*b
print(total)