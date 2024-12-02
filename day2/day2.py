filename = "sample.txt"
# filename = "input.txt"

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



def check_single_row(row):
    final_res = False

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
            final_res = True
        else:
            print("FAIL up down counts")
            final_res = False
    else:
        print("FAIL for at least one and most 3")
        final_res = False
    print()
    return final_res

def part1():

    good_count = 0

    for row in tmp_data:

        res = check_single_row(row)
        if res:
            good_count += 1

    print(good_count)

def part2():
    pass

part1()