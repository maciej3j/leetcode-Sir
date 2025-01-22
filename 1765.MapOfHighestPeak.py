from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    height = []
    height_matrix = [[0 for _ in row] for row in isWater]
    
    for i, row in enumerate(isWater):
        for j, cell in enumerate(row):
            height_matrix = []
            if cell == 0:



#input:  [[0, 1], [0,0]]
#output: [[1, 0], [2,1]]
