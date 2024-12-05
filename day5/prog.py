
import re

class DataHolder:
    def __init__(self):
        self.rules = []
        self.orders = []
    def __repr__(self):
        return f"DataHolder(rules={self.rules}, orders={self.orders})"

def get_data():
    lines = open("sample.txt").readlines()

    res = DataHolder()

    # fuck lazy ass python maps
    lines = list(map(lambda x: x.strip(), lines))
    P1 = re.compile(r"(\d+)\|(\d+)")

    index = 0
    while True:
        try:
            line = lines[index]
        except IndexError:
            print("end of lines",index)
            break
        
        m = P1.match(line)
        if m:
            num1 = int(m.group(1))
            num2 = int(m.group(2))

            res.rules.append((num1,num2))
            index += 1
            continue

        if line=="":
            index += 1
            continue

        tmp = line.split(",")
        # TODO save updates here
        res.orders.append(tmp)    
        index += 1
    return res


d = get_data()
print(d)