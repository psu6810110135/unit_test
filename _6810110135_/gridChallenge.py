
def gridChallenge(grid):

    sort_grid = [sorted(g) for g in grid]
    for i in range(len(sort_grid)):
        for j in range(len(sort_grid[i]) - 1):
            if sort_grid[i][j] > sort_grid[i][j + 1]:
                return 'NO'
    return 'YES'
# if __name__ == '__main__':

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         grid = []

#         for _ in range(n):
#             grid_item = input()
#             grid.append(grid_item)

#         result = gridChallenge(grid)
#         print(result)

