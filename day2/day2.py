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

print(tmp_data)