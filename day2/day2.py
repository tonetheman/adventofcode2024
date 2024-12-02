#!/usr/bin/env python3


# filename = "sample.txt"
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



def check_single_row(row):
    final_res = False
    al3_counts = {True:0,False:0}
    updown_counts = {False:0,True:0}
    # print(len(row),row)
    for i in range(len(row)-1):
        res = atLeastOneMostThree(row[i],row[i+1])
        if res in al3_counts:
            al3_counts[res] += 1
        else:
            al3_counts[res] = 1
        res = row[i]<row[i+1]
        updown_counts[res] += 1

        # print(row[i],row[i+1],atLeastOneMostThree(row[i],row[i+1]), row[i]<row[i+1])
    # print("al3 counts",al3_counts)
    # print("updown",updown_counts)
    # THIS LINE BELOW IS A PROBLEM?
    if al3_counts[True] == len(row)-1:
        # they have enough trues to need second comparison
        if updown_counts[False]==len(row)-1 or updown_counts[True]==len(row)-1:
            # print("SUCCESS")
            final_res = True
        else:
            # print("FAIL up down counts")
            final_res = False
    else:
        # print("FAIL for at least one and most 3")
        final_res = False
    return final_res

def part1():

    good_count = 0

    for row in tmp_data:

        res = check_single_row(row)
        if res:
            good_count += 1

    print(good_count)


def make_new_skip_index(row,index):
    tmp = []
    for i in range(len(row)):
        if i==index:
            pass
        else:
            tmp.append(row[i])
    return tmp

def recheck(row):
    """
    the row as it came failed
    now remove single items and recheck each of them
    """
    count = 0
    for i in range(len(row)):
        # make a new row skipping the index i
        new_row = make_new_skip_index(row,i)
        print("new_row",new_row)
        new_res = check_single_row(new_row)
        print("new res",new_res)    
        if new_res: count += 1
    
    if count>0:
        print("WOULD BE GOOD WITH DAMP")
        return True
    else:
        print("FAILED DAMP")
        return False



def test_recheck():
    # will not be good if we remove at least 1
    row = [1,2,7,8,9]
    res = check_single_row(row)
    print("check single row", res)
    if res==False:
        recheck(row)
    
    # will be good if we remove at least 1
    row = [1,3,2,4,5]
    res = check_single_row(row)
    print("check single row", res)
    if res==False:
        recheck(row)
        

def test_recheck_specific():
    row = [77, 74, 77, 82, 86]
    res = check_single_row(row)
    print("res",res)
    if res==False:
        new_res = recheck(row)
        print(new_res)


def part2():
    good_count = 0
    for row in tmp_data:
        res = check_single_row(row)
        if res:
            good_count += 1
        else:
            # now we need to remove things and retest!
            print("row to recheck",row)
            res = recheck(row)
            if res:
                good_count += 1
            print("WOULD REMOVE AND RETEST")
            print()
    print(good_count)

# part1()
part2()
# test_recheck()
# test_recheck_specific()
