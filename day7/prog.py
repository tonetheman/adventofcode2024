



def part1():
    lines = open("sample.txt","r").readlines()
    lines = [line.strip() for line in lines]

    for line in lines:
        print(line)
        tmp = line.split(":")
        answer = int(tmp[0])
        parts = list(map(int,filter(lambda x : x!="", tmp[1].split(" "))))
        print("answer: ", answer)
        print("parts: ", parts)
        needed = len(parts)-1 # num operations
        print("needed: ", needed)

        for i in range(needed):
            for j in range(needed):
                pass

        break

part1()