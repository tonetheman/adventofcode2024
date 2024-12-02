filename = "sample.txt"

data = open(filename,"r").readlines()

tmp_data = []

for d in data:
    # map int over the array
    tmp = map(lambda a : int(a), d.split(" "))

    # wtf has happened to python seriously
    # what twat ass idea is it to be lazy by default
    # so I have to force this to a list
    # sigh
    res = list(tmp)
    # print(res)
    tmp_data.append(res)

def atLeastOneMostThree(a,b):
    # check that from a to b there
    # at least 1 and at most 3 difference
    # ha my brain is much
    if a==b: return False
    if b>(a+3): return False # b is too big
    if b<(a-3): return False # b is too small
    return True

def test1():
    for i in range(10):
        for j in range(10):
            print(i,j,atLeastOneMostThree(i,j))
    assert(atLeastOneMostThree(1,3)==True)
    assert(atLeastOneMostThree(1,4)==True)
    assert(atLeastOneMostThree(1,5)==False)
    assert(atLeastOneMostThree(7,3)==False)

def part1():
    # TODO
    # partial working
    # sample case #4 does not work
    """
    they are good on the first rule of atLeastOneMostThree
    TODO: But it fails because some are increasing some are decreasing
    need to check for that also
[1, 3, 2, 4, 5]
1 3 True
3 2 True
2 4 True
4 5 True
    """
    for row in tmp_data:
        print(row)
        for i in range(len(row)-1):
            print(row[i],row[i+1],atLeastOneMostThree(row[i],row[i+1]))
        print()


part1()