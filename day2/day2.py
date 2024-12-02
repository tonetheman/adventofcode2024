filename = "sample.txt"
filename = "input.txt"

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

    other notes 
        if the first boolean is all True you must check 2nd column
            if 2nd boolean all False or all True
                SUCCESS
            else
                FAIL
        if the first boolean is mixed you FAIL

    """

    good_count = 0

    for row in tmp_data:
        al3_counts = {}
        updown_counts = {False:0,True:0}
        print(len(row),row)
        for i in range(len(row)-1):
            res = atLeastOneMostThree(row[i],row[i+1])
            if res in al3_counts:
                al3_counts[res] += 1
            else:
                al3_counts[res] = 1
            res = row[i]<row[i+1]
            updown_counts[res] += 1

            print(row[i],row[i+1],atLeastOneMostThree(row[i],row[i+1]), row[i]<row[i+1])
        print("al3 counts",al3_counts)
        print("updown",updown_counts)
        if al3_counts[True] == len(row)-1:
            # they have enough trues to need second comparison
            if updown_counts[False]==len(row)-1 or updown_counts[True]==len(row)-1:
                print("SUCCESS")
                good_count += 1
            else:
                print("FAIL up down counts")


        else:
            print("FAIL for at least one and most 3")
        print()
    
    print(good_count)

part1()