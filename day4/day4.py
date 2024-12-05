


def get_data():
    filename = "input.txt"
    data = open(filename,"r").readlines()
    data = [line.strip() for line in data]
    return data

def add_padding(data):
    # adding padding to make my life easier
    d=[]

    # if you call list() on a string you get an array of chars!
    d.append(list("."*(2+len(data[0]))))

    for line in data:
        new_line = "." + line + "."
        d.append(list(new_line))
    
    d.append(list("."*(2+len(data[0]))))
    
    return d

def pp(data):
    for line in data:
        print(line)

def xmas_search(data,r,c):
    count = 0
    # to the right
    if data[r][c] == 'X' and data[r][c+1]=='M' and data[r][c+2]=='A' and data[r][c+3]=='S':
        count += 1
    # to the left
    if data[r][c] == 'X' and data[r][c-1]=='M' and data[r][c-2]=='A' and data[r][c-3]=='S':
        count += 1
    # up
    if data[r][c] == 'X' and data[r-1][c]=='M' and data[r-2][c]=='A' and data[r-3][c]=='S':
        count += 1
    # down
    if data[r][c] == 'X' and data[r+1][c]=='M' and data[r+2][c]=='A' and data[r+3][c]=='S':
        count += 1
    # diag right up
    if data[r][c] == 'X' and data[r-1][c+1]=='M' and data[r-2][c+2]=='A' and data[r-3][c+3]=='S':
        count += 1
    # diag right down
    if data[r][c] == 'X' and data[r+1][c+1]=='M' and data[r+2][c+2]=='A' and data[r+3][c+3]=='S':
        count += 1
    # diag left up
    if data[r][c]=='X' and data[r-1][c-1]=='M' and data[r-2][c-2]=='A' and data[r-3][c-3]=='S':
        count += 1
    # diag left down
    if data[r][c]=='X' and data[r+1][c-1]=='M' and data[r+2][c-2]=='A' and data[r+3][c-3]=='S':
        count += 1

    return count
        
def xmas_search2(data,r,c):
    count = 0
    if data[r][c]!='A':
        return 0
    
    """
    print("r,c",r,c)
    print("value of r,c", data[r][c])
    print("MAS",data[r-1][c-1]=='M' and data[r][c]=='A' and data[r+1][c+1]=='S')
    print("row",data[r])
    print("SAM",data[r-1][c-1]=='S' and data[r][c]=='A' and data[r+1][c+1]=='M')
    print("part2")
    print("MAS",data[r-1][c+1]=='M' and data[r][c]=='A' and data[r+1][c-1]=='S')
    print("SAM",data[r-1][c+1]=='S' and data[r][c]=='A' and data[r+1][c-1]=='M')
    print()
    """
    
    """
    easier to search both ways at the same time on each diag
    """
    if (data[r-1][c-1]=='M' and data[r][c]=='A' and data[r+1][c+1]=='S') or (data[r-1][c-1]=='S' and data[r][c]=='A' and data[r+1][c+1]=='M'):
        if (data[r-1][c+1]=='M' and data[r][c]=='A' and data[r+1][c-1]=='S') or (data[r-1][c+1]=='S' and data[r][c]=='A' and data[r+1][c-1]=='M'):
            count += 1
    return count        

def find_xmas(data):
    # pp(data)
    total_found = 0
    for ridx in range(len(data)):
        crow = data[ridx]
        # print(crow)
        for cidx in range(len(crow)):
            cc = crow[cidx]
            if cc=='A':
                # print(ridx,cidx,cc)
                # part1
                # res = xmas_search(data,ridx,cidx)
                # part2
                res = xmas_search2(data,ridx,cidx)
                total_found += res
    print("total_found",total_found)

data = get_data()
new_data = add_padding(data)
find_xmas(new_data)

def test():
    # res = xmas_search2(new_data,2,3)
    # print(res)
    res = xmas_search2(new_data,4,5)
    print(res)
