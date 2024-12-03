

def part1():
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

def part2():
    
    filename = "input.txt"
    data = open(filename,"r").read()

    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    # print(data)

    import re
    P = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    # P1 = re.compile(r"do\(\)")
    # P2 = re.compile(r"don't\(\)")
    
    # matches = P.findall(data)
    matches = P.findall(data)
    print(matches)

    _do = True
    total = 0
    PP = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    for m in matches:
        if m[0] == "m":
            if _do:
                print(m,PP.match(m).groups())
                (a,b) = PP.match(m).groups()
                a=int(a)
                b=int(b)
                print(a*b)
                total += a*b
        elif m[0] == "d" and m[1]=="o" and m[2]=="(":
            # do command
            _do = True
        else:
            # dont
            _do = False
    print(total)

part2()