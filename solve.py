
def solve(grid):
    #create a copy for grabbing total coins later
    default_matrix = [row[:] for row in grid]

    #for an n by n grid
    n = len(grid)

    #run it twice because some values are dropped
    solve_grid(grid,n)
    solve_grid(grid,n)

    #get the number of coints
    coins = 0
    for o in range(n):
        for i in range(n):
            coins += grid[o][i] - default_matrix[o][i]
    return coins


def solve_grid (grid, n):
    for row in range(n):
        max_ = grid[row][0]
        index = 0
        i = 1

        for i in range(n):
            if grid[row][i] >= max_:
                max_ = grid[row][i]
                index = i
        indr = index

        #from the back
        temp = grid[row][n-1]
        for col in range(n-1,indr,-1):
            temp = max(temp,grid[row][col])
            grid[row][col] = temp

        #from the front
        temp = grid[row][0]
        for col in range(1,indr):
            temp = max(temp,grid[row][col])
            grid[row][col] = temp

    for col in range (n):
        #assume max is first
        max_ = grid[0][col]
        index = 0
        i = 1

        for i in range(n):
            if grid[i][col] >= max_:
                max_ = grid[i][col]
                index = i
            indc = index

        #back to ind
        temp = grid[n-1][col]
        for row in range(n-1,indc,-1):
            temp = max(temp,grid[row][col])
            grid[row][col] = temp

        #front to ind
        temp = grid[0][col]
        for row in range(1,indc):
            temp = max(temp,grid[row][col])
            grid[row][col] = temp












def main():
    grid = [
        [1,2,5,3,3],
        [2,4,1,5,1],
        [2,1,1,5,2],
        [1,1,5,1,3],
        [4,3,1,5,1]
    ]
    x = solve(grid)
    for col in grid:
        print(*col)
    print("Coins: " , x)


if __name__ == '__main__':
    main()
