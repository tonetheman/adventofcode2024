


def make_grid(filename):
    grid = []
    data = open(filename).readlines()
    for d in data:
        d = d.strip()
        print(d)
        tmp = []
        for c in d:
            if c == '#':
                tmp.append('#')
            elif c == 'O':
                tmp.append('O')
            elif c == '.':
                tmp.append('.')
            elif c == '@':
                tmp.append('@')
            else:
                print("ERRR")
        grid.append(tmp)
    return grid

def find_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                return i, j
def part1():
    px = 0
    py = 0
    
    moves = "<^^>>>vv<v>>v<<"

    def move_up(grid):
        pass
    def move_down(grid):
        pass
    def move_left(grid):
        if grid[px-1][py] == '#':
            print("cannt move")
            return
    def move_right(grid):
        pass

    grid = make_grid("sample.txt")
    print(grid)
    (px,py) = find_player(grid)
    print(px,py)
    move_left(grid)

part1()    


