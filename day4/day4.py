
filename = "sample.txt"
data = open(filename,"r").readlines()
data = [line.strip() for line in data]

print(data)