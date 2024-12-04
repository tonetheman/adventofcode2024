


def get_data():
    filename = "sample.txt"
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

data = get_data()
new_data = add_padding(data)
print(new_data)