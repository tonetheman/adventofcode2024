



def load_grid():
    filename = "sample.txt"
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

def find_player(g):
    for i in range(len(g)): # these are rows
        for j in range(len(g[i])): # these are cols
            if g[i][j]=='^' or g[i][j]=='>' or g[i][j]=='<' or g[i][j]=='v':
                return (i,j)
def next_pos(g):
    (pr,pc) = find_player(g)
    player = g[pr][pc]
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

def mark_current_pos(g,gd):
    (pr,pc) = find_player(g)
    gd[pr][pc] = 1

def turn_player_right(g):
    print("turning player")
    (pr,pc) = find_player(g)
    p = g[pr][pc]
    if p=='^':
        g[pr][pc] = '>'
    elif p=='>':
        g[pr][pc] = 'v'
    elif p=='v':
        g[pr][pc] = '<'
    elif p =='<':
        g[pr][pc] = '^'
    else:
        print("ERR TURN")

def pg(msg,g):
    print(msg)
    for line in g:
        print(line)

def part1():
    (g,gd) = load_grid()
    pg("start",g)

    while True:
        # mark on the output where we are
        # does not matter if we over write
        mark_current_pos(g,gd)

        # decide next position
        (nextr,nextc) = next_pos(g)
        print(nextr,nextc)
        try:
            if g[nextr][nextc] == '#':
                # cannot move this direction turn right
                turn_player_right(g)    
            else:
                # can move
                # get current position
                (cr,cc) = find_player(g)
                # do the move
                g[nextr][nextc] = g[cr][cc]
                # reset the position we moved from
                g[cr][cc] = '.'

            # pg("after move",g)
        except IndexError:
            pg("final",gd)
            break
    
    count = 0
    for ll in gd:
        for l in ll:
            count += l
    print(count)

part1()