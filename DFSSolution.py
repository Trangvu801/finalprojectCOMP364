class DFSSolution:
    def __init__(self, maze):
        """
        Initializes the DFSSolution class.

        Parameters:
        - maze: A 2D list representing the maze structure. Each cell can contain:
          - A cost value and optional teleport coordinates (e.g., [6, (1,1)]).
          - '#' indicating a wall.
          - 'G' indicating the goal position.

        Attributes:
        - self.maze: Stores the input maze.
        - self.start: The starting position (top-left corner, implicitly (0,0)).
        - self.goal: The goal position (bottom-right corner, implicitly (n-1,n-1)).
        - self.path: A list used to store the current path from start to goal.
        - self.visited: A set to keep track of visited nodes, avoiding revisiting nodes and loops.
        """
        self.maze = maze
        self.start = maze[0][0]
        self.goal = maze[len(maze) - 1][len(maze) - 1]
        self.path = []  # To store the path to the goal
        self.visited = set()  # To keep track of visited nodes

    def DepthFirstSearch(self, cur=(0, 0)):
        """
        Performs Depth-First Search recursively to find a path to the goal.

        Parameters:
        - cur: The current cell being explored, represented as a tuple (row, column).

        Returns:
        - True if a path to the goal is found; False otherwise.
        """
        # Mark the current node as visited and add it to the path
        self.visited.add(cur)
        self.path.append(cur)

        # Base case: If the goal is reached, return True
        if cur == (len(self.maze) - 1, len(self.maze) - 1):
            return True

        # Explore all possible moves from the current cell
        for next_move in self.possibleSolution(cur):
            if next_move not in self.visited:  # Check if the move is unvisited
                # Recursively call DFS on the next move
                if self.DepthFirstSearch(next_move):
                    return True

        # If all moves fail, backtrack by removing the current node from the path
        self.path.pop()
        return False

    def possibleSolution(self, cur):
        """
        Identifies all valid moves from the current cell.

        Parameters:
        - cur: The current cell being explored, represented as a tuple (row, column).

        Returns:
        - A list of valid neighboring cells or teleport locations that can be visited.
        """
        posSol = []  # List to store possible solutions
        row, col = cur[0], cur[1]

        # Check each direction for valid moves (not blocked by walls):
        # Left (col - 1)
        if col - 1 >= 0 and self.maze[row][col - 1][0] != "#":
            posSol.append((row, col - 1))

        # Right (col + 1)
        if col + 1 < len(self.maze) and self.maze[row][col + 1][0] != "#":
            posSol.append((row, col + 1))

        # Down (row + 1)
        if row + 1 < len(self.maze) and self.maze[row + 1][col][0] != "#":
            posSol.append((row + 1, col))

        # Up (row - 1)
        if row - 1 >= 0 and self.maze[row - 1][col][0] != "#":
            posSol.append((row - 1, col))

        # Teleportation (if the current cell has teleport coordinates)
        if len(self.maze[row][col]) > 1:
            posSol.append(self.maze[row][col][1])

        return posSol

    def getPath(self):
        """
        Initiates the Depth-First Search and retrieves the path from start to goal.

        Returns:
        - A list of coordinates representing the path from start to goal if a solution exists.
        - "No path found" if no solution exists.
        """
        if self.DepthFirstSearch():
            return self.path
        else:
            return "No path found"


# Example Usage
n = 3  # Maze size
maze = createMaze(n)  # Generate a random maze
print("Generated Maze:")
for row in maze:
    print(row)

print("\nDFS Solution Path:")
dfs = DFSSolution(maze)
print(dfs.getPath())
