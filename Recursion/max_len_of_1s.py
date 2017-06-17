#Finding the length of connected cells of 1s (regions) in an matrix of Os and 1s

#returns maximum length of connected cells of 1s
def get_max_one(mylist, rowMax, colMax):
    maxSize=0
    size=0
    #create a list to keep track of visited elements
    cntarr = [[0 for x in range(0, rowMax)] for y in range(0, colMax)]
    for i in range(0,rowMax):
        for j in range(0, colMax):
            if mylist[i][j] == 1:
                maxSize = find_max_block(mylist, i, j, rowMax, colMax, 0, cntarr, maxSize)
    return maxSize

def find_max_block(mylist, r, c, R, C, size, cntarr, maxSize):
    if (r >= R) or (c >= C):
        return
    cntarr[r][c] = True
    size = size+1
    new_max = maxSize
    if size > maxSize:
        new_max = size
    #create a list to check neighboring 1s in 8 directions
    direction = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
    for i in range(0,8):
        new_i = r + direction[i][0]
        new_j = c + direction[i][1]
        val = get_val(mylist, new_i, new_j, R, C)
        if (val > 0) and (cntarr[new_i][new_j] == False):
            new_max = find_max_block(mylist, new_i, new_j, R, C, size, cntarr, new_max)
    cntarr[r][c] = False
    return new_max

#get value at particular index within the list
def get_val(mylist, i, j, R, C):
    if (i < 0) or (i >= R) or (j < 0) or (j >= C):
        return 0
    else:
        return mylist[i][j]

mylist = [
            [1,1,0,0,0],
            [0,1,1,0,0],
            [0,0,1,0,1],
            [1,0,0,0,1],
            [0,1,0,1,1]
        ]

print(get_max_one(mylist, 5, 5))
