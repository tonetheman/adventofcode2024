#!/usr/bin/env python3

"""
https://www.reddit.com/r/adventofcode/comments/1h4ncyr/comment/m02fv18/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import itertools

with open('src/day02/input.txt', 'r') as file:
    items = [[int(x) for x in line.split()] for line in file]

def isSafe(levels):
    steps = [a - b for a, b in itertools.pairwise(levels)]
    return all(x > 0 and x < 4 for x in steps) or all(x < 0 and x > -4 for x in steps)

def isAnySubsetSafe(levels):
    subsets = [levels[:i] + levels[i+1:] for i in range(len(levels))]
    return any(isSafe(subset) for subset in subsets)


part1 = sum(1 for levels in items if isSafe(levels))
part2 = sum(1 for levels in items if isAnySubsetSafe(levels))

print(part1)
print(part2)

"""


import itertools

filename = "sample.txt"
# filename = "input.txt"

data = open(filename,"r").readlines()

# for line in data makes a list
# the first bit splits it out and makes ints
# I do not think like this at all
stuff = [ [int(v) for v in line.split() ] for line in data]


for levels in stuff:

    # do a subtract on the pairwise things in levels
    # this will get you a difference basically
    # and is used in the next step
    steps = [ a-b for a,b in itertools.pairwise(levels) ]
    
    # see if all of the steps meet pos requirement
    # or negative
    pos_res = all(x>0 and x<4 for x in steps)
    neg_res =  all(x<0 and x>-4 for x in steps)

    # need to or them pos and neg to get final result
    final_res = pos_res or neg_res
    if final_res:
        print("YES",levels,steps,pos_res,neg_res, pos_res or neg_res)
    else:
        print("NO0",levels,steps,pos_res,neg_res, pos_res or neg_res)

a = [7,6,4,2,1]
print("orig",a)
b = [a[:i] + a[i+1:] for i in range(len(a))]
print(b)