import heapq

class AStarSolution:
    def __init__(self, maze):
        """
        Initializes the A* solution class.

        Parameters:
        - maze: A 2D list representing the maze structure. Each cell can contain:
          - A cost value and optional teleport coordinates (e.g., [6, (1,1)]).
          - '#' indicating a wall.
          - 'G' indicating the goal position.

        Attributes:
        - self.maze: Stores the maze.
        - self.start: The starting position (implicitly (0,0)).
        - self.goal: The goal position (implicitly (n-1,n-1)).
        """
        self.maze = maze
        self.start = (0, 0)
        self.goal = (len(maze) - 1, len(maze) - 1)

    def heuristic(self, a, b):
        """
        Calculates the Manhattan distance between two points.

        Parameters:
        - a, b: Tuples representing coordinates (row, column).

        Returns:
        - The Manhattan distance between a and b.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def aStarSearch(self):
        """
        Performs A* search to find the shortest path from start to goal.

        Returns:
        - The shortest path as a list of coordinates if a solution exists.
        - "No path found" if the maze is unsolvable.
        """
        # Priority queue to store nodes along with their f-cost (g + h)
        open_set = []
        heapq.heappush(open_set, (0, self.start))  # (f-cost, node)

        # Dictionaries to store the g-cost and parent of each node
        g_cost = {self.start: 0}
        parent = {self.start: None}

        # Visited set to avoid revisiting nodes
        visited = set()

        while open_set:
            # Get the node with the lowest f-cost
            _, current = heapq.heappop(open_set)

            # If the goal is reached, reconstruct and return the path
            if current == self.goal:
                return self.reconstruct_path(parent)

            visited.add(current)

            # Explore neighbors
            for neighbor in self.possibleSolution(current):
                if neighbor in visited:
                    continue

                # Calculate tentative g-cost
                tentative_g_cost = g_cost[current] + self.getCost(current, neighbor)

                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    # Update g-cost and parent
                    g_cost[neighbor] = tentative_g_cost
                    parent[neighbor] = current

                    # Calculate f-cost and add to the priority queue
                    f_cost = tentative_g_cost + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_cost, neighbor))

        return "No path found"  # No solution exists

    def possibleSolution(self, cur):
        """
        Identifies all valid moves from the current cell.

        Parameters:
        - cur: The current cell being explored, represented as a tuple (row, column).

        Returns:
        - A list of valid neighboring cells or teleport locations.
        """
        posSol = []
        row, col = cur[0], cur[1]

        # Check all possible directions
        if col - 1 >= 0 and self.maze[row][col - 1][0] != "#":  # left
            posSol.append((row, col - 1))
        if col + 1 < len(self.maze) and self.maze[row][col + 1][0] != "#":  # right
            posSol.append((row, col + 1))
        if row + 1 < len(self.maze) and self.maze[row + 1][col][0] != "#":  # down
            posSol.append((row + 1, col))
        if row - 1 >= 0 and self.maze[row - 1][col][0] != "#":  # up
            posSol.append((row - 1, col))

        # Teleportation
        if len(self.maze[row][col]) > 1:
            posSol.append(self.maze[row][col][1])

        return posSol

    def getCost(self, current, neighbor):
        """
        Retrieves the movement cost between the current cell and its neighbor.

        Parameters:
        - current, neighbor: Tuples representing cell coordinates.

        Returns:
        - The cost value of moving to the neighbor.
        """
        row, col = neighbor
        return self.maze[row][col][0] if self.maze[row][col][0] != "#" else float('inf')

    def reconstruct_path(self, parent):
        """
        Reconstructs the path from start to goal using the parent dictionary.

        Parameters:
        - parent: A dictionary mapping each node to its parent.

        Returns:
        - A list of coordinates representing the path from start to goal.
        """
        path = []
        current = self.goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path


# Example Usage
n = 3  # Maze size
maze = createMaze(n)  # Generate a random maze
print("Generated Maze:")
for row in maze:
    print(row)

print("\nA* Solution Path:")
astar = AStarSolution(maze)
solution_path = astar.aStarSearch()
print(solution_path)
