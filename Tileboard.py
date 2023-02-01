import random

# class Tileboard:
#     def __init__(self, cols = 10, rows = 10):
#         self.cols = cols
#         self.rows = rows
#         self.createBoard()
        
#     def createBoard(self):
#         self.grid = []
#         for i in range(self.rows):
#             row = []
#             for j in range(self.cols):
#                 # Assign different colors to tiles
#                 tile = Tile()
#                 row.append(tile)
#             self.grid.append(row)





class Tile:
    def __init__(self):
        self.options = ["up", "down", "left", "right"]
        
    def randomCollapse(self):
        pick = random.choice(self.options)
        newOptions = [pick]
        self.options = newOptions
        return pick

    def displayOptions(self):
        return self.options



def createBoard(cols = 5, rows = 5 ):
    cols = cols
    rows = rows

    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Assign different colors to tiles
            tile = Tile()
            row.append(tile)
        grid.append(row)
    return grid

