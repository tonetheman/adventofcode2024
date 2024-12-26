
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
            # print("end of lines",index)
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
        res.orders.append(list(map(int,tmp)))    
        index += 1
    return res

def get_rules_for_order(d:DataHolder,c_order):
    # this really should be a map
    # do not need duplicate rules
    # in this list I think
    res = []
    for val in c_order:
        for rule in d.rules:
            if rule[0]==val or rule[1]==val:
                res.append(rule)
    return res
        

d = get_data()
c_order = d.orders[0]
print("current order",c_order)
rules_to_check = get_rules_for_order(d,c_order)
print("rules to check",rules_to_check)