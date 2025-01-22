from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    height_matrix = [[0 for _ in row] for row in isWater]
    
    # for i, row in enumerate(isWater):
        # for j, cell in enumerate(row):
            # if cell == 0:
                # height_matrix[i][j] += 1

    for i, row in enumerate(isWater):
        for j, cell in enumerate(row):
            if cell == 0:
                if i == 0:
                    if j == 0:
                        if isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                    elif j == len(isWater[i])-1:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                    else:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1
                elif i == len(isWater)-1:
                    if j == 0:
                        if isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1
                    elif j == len(isWater[i])-1:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1
                    else:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                        if isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                else:
                    if j == 0:
                        if isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                    elif j == len(isWater[i])-1:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                    else:
                        if isWater[i][j-1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i+1][j] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i][j+1] == 0:
                            height_matrix[i][j] += 1
                        elif isWater[i-1][j] == 0:
                            height_matrix[i][j] += 1


    return height_matrix

print(highestPeak([[0, 1],
                   [0, 0]]))

#input:  [[0, 1],
#         [0, 0]]
#output: [[1, 0],
#         [2, 1]]


# [[0, 1, 0],
#  [1, 1, 1],
#  [0, 1, 0]]