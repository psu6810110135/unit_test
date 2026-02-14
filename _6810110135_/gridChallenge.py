
def gridChallenge(grid):
    if not grid:
        return 'YES'
    sorted_rows = [sorted(row) for row in grid]
    for i in range(len(sorted_rows[0])):
        for j in range(1, len(sorted_rows)):
            if sorted_rows[j][i] < sorted_rows[j-1][i]:
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

