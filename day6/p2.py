
"""

4716 is too low

"""
def load_grid():
    filename = "input.txt"
    lines = open(filename,"r").readlines()

    lines = list(map(lambda s : s.strip(),lines))

    grid = []
    dup_grid = []

    for line in lines:
        tmp = []
        tmp2 = []
        for c in line:
            tmp.append(c)
            tmp2.append(0)
        grid.append(tmp)
        dup_grid.append(tmp2)

    return (grid,dup_grid)

def part1():
    pr = 0 # where is the player now row
    pc = 0 # where is the player now col

    def find_player_once():
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='^' or grid[i][j]=='>' or grid[i][j]=='<' or grid[i][j]=='v':
                    return (i,j)
    def next_pos():
        player = grid[pr][pc]
        if player=='^':
            direction = (pr+-1,pc+0)
        elif player=='v':
            direction = (pr+1,pc+0)
        elif player=='<':
            direction = (pr+0,pc+-1)
        elif player=='>':
            direction = (pr+0,pc+1)
        else:
            print("ERR NOT A PLAYER")
        
        return direction
    def turn_player_right():
        print("turning player")
        p = grid[pr][pc]
        if p=='^':
            grid[pr][pc] = '>'
        elif p=='>':
            grid[pr][pc] = 'v'
        elif p=='v':
            grid[pr][pc] = '<'
        elif p =='<':
            grid[pr][pc] = '^'
        else:
            print("ERR TURN")

    def pg(msg,grid):
        print(msg)
        for g in grid:
            print(g)

    (grid,dup_grid) = load_grid()
    pr,pc = find_player_once()
    pg("grid",grid)
    print(pr,pc,grid[pr][pc])
    count = 0
    while True:
        # remember orientation
        cc = grid[pr][pc]
        # save a trail
        dup_grid[pr][pc] = 1
        # figure out next step
        nr,nc = next_pos()
        if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]):
            print("END")
            break
        if grid[nr][nc] == '#':
            # turn right
            turn_player_right()
        else:
            grid[pr][pc] = '.'
            grid[nr][nc] = cc
            pr,pc = nr,nc
            # move

        # pg("grid"+str(count),grid)
        count += 1
    total = 0
    for i in range(len(dup_grid)):
        for j in range(len(dup_grid[i])):
            if dup_grid[i][j]==1:
                total += 1
    print("total",total)


part1()

