import random

class Maze:
    solid = "@ "
    empty = "  "

    def __init__(self, width, height, origin=(0, 0)):
        self.width = width
        self.height = height
        self.visited = {origin} # the origin is our starting point, so it has already been "visited"
        self.edge = self.getNeighbors(origin) # start branching adjacent to the origin
        self.path = set() # there's no path yet since we haven't generated anything

        while self.edge: self.branch() # while there's somewhere to go, continue on

    # create a new "branch" or passage through the maze
    def branch(self):
        cell = random.choice(list(self.edge)) # pick a random cell adjacent to one that has already been visited (along the edge)
        neighbors = self.getNeighbors(cell)   # get all the cell's adjacent neighbors
        previous = random.choice(list(self.visited & neighbors)) # pick a visited cell to connect to
        neighbors = neighbors - self.visited  # we only want the new, unvisited neighbors from here on

        self.edge |= neighbors # add the new neighbors to the edge
        self.join(previous, cell) # connect the new and visited cells
        self.edge.discard(cell) # remove the current cell from the edge
        self.visited.add(cell) # mark the current cell as having been visited

        while neighbors and random.random() > 0.05: # end the branch if there's nowhere to go or by random chance
            previous, cell = cell, random.choice(list(neighbors)) # advance forward in a random (open) direction
            self.edge |= neighbors # add the new neighbors to the edge
            self.join(previous, cell) # connect the two cells
            self.edge.discard(cell) # remove the current cell from the edge
            self.visited.add(cell) # mark the current cell as having been visited
            neighbors = self.getNeighbors(cell) - self.visited # search for adjacent neighbors who haven't yet been visited

    # connect the two cells, adding their intersection to the maze path
    def join(self, cellA, cellB):
        self.path.add((cellA[0]+cellB[0], cellA[1]+cellB[1])) # (x1, y1) and (x2, y2) intersection is (x1+x2, y1+y2)

    def getNeighbors(self, cell):
        neighbors = set()
        if cell[0] > 0:               neighbors.add((cell[0] - 1, cell[1])) # don't go off the grid
        if cell[0] < self.width - 1:  neighbors.add((cell[0] + 1, cell[1])) #
        if cell[1] > 0:               neighbors.add((cell[0], cell[1] - 1)) #
        if cell[1] < self.height - 1: neighbors.add((cell[0], cell[1] + 1)) #
        return neighbors

    def __str__(self):
        maze = edge = self.solid*(self.width*2+1)
        for y in range(self.height*2-1):
            maze += "\n" + self.solid
            for x in range(self.width*2):
                if x%2 == y%2 == 0 or (x, y) in self.path:
                    maze += self.empty
                else:
                    maze += self.solid
        maze += "\n" + edge
        return maze

if __name__ == "__main__":
    print(Maze(12, 12))
