from createMaze import createMaze

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
        - self.visited_sequence: A list to store the order of visited nodes.
        """
        self.maze = maze
        self.start = (0, 0)
        self.goal = (len(maze) - 1, len(maze) - 1)
        self.path = []  # To store the path to the goal
        self.visited = set()  # To keep track of visited nodes
        self.visited_sequence = []  # To store the sequence of visited nodes
        self.total_cost = 0  # To store the total cost of the solution path

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
        self.visited_sequence.append(cur)
        self.path.append(cur)

        # Add cost if the cell has a numeric value
        cell_value = self.maze[cur[0]][cur[1]]
        if isinstance(cell_value[0], int):
            self.total_cost += cell_value[0]

        # Base case: If the goal is reached, return True
        if cur == self.goal:
            return True

        # Explore all possible moves from the current cell
        for next_move in self.possibleSolution(cur):
            if next_move not in self.visited:  # Check if the move is unvisited
                # Recursively call DFS on the next move
                if self.DepthFirstSearch(next_move):
                    return True

        # If all moves fail, backtrack by removing the current node from the path and adjusting cost
        self.path.pop()
        if isinstance(cell_value[0], int):
            self.total_cost -= cell_value[0]
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
        - A tuple containing:
          - The path from start to goal if a solution exists.
          - "No path found" if no solution exists.
          - Nodes visited in sequence.
          - Total cost of the solution path.
        """
        if self.DepthFirstSearch():
            return self.path, self.visited_sequence, self.total_cost
        else:
            return "No path found", self.visited_sequence, self.total_cost


n = 5  # Fixed Maze size to 5x5
maze = createMaze(n)  # Generate a random maze of size 5x5
print("Generated Maze:")
for row in maze:
    print(row)

dfs = DFSSolution(maze)
solution, visited_nodes, total_cost = dfs.getPath()

print("\nDFS Solution Path:", solution)
print("Visited Nodes in Order:", visited_nodes)
print("Total Cost of Solution Path:", total_cost)
