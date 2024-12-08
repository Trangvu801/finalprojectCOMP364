import heapq
from createMaze import createMaze

class AStarSolution:
    def __init__(self, maze):
        self.maze = maze
        self.start = (0, 0)
        self.goal = (len(maze) - 1, len(maze) - 1)

    def heuristic(self, a, b):
        """Calculate the Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def aStarSearch(self):
        """Performs the A* search algorithm."""
        open_set = []
        heapq.heappush(open_set, (0, self.start))

        g_cost = {self.start: 0}  # Cost from start to a node
        parent = {self.start: None}  # To reconstruct the path
        visited = []  # Order of visited nodes

        while open_set:
            _, current = heapq.heappop(open_set)

            if current in visited:
                continue

            visited.append(current)  # Track visitation order

            if current == self.goal:
                path = self.reconstruct_path(parent)
                total_cost = self.calculate_path_cost(path)
                return path, visited, total_cost

            for neighbor in self.possibleSolution(current):
                tentative_g_cost = g_cost[current] + self.getCost(current, neighbor)

                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    parent[neighbor] = current

                    f_cost = tentative_g_cost + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_cost, neighbor))

        return "No path found", visited, 0

    def possibleSolution(self, cur):
        """Identify valid neighbors for the current cell."""
        posSol = []
        row, col = cur[0], cur[1]

        # Check all four directions
        if col - 1 >= 0 and self.maze[row][col - 1][0] != "#":
            posSol.append((row, col - 1))
        if col + 1 < len(self.maze) and self.maze[row][col + 1][0] != "#":
            posSol.append((row, col + 1))
        if row + 1 < len(self.maze) and self.maze[row + 1][col][0] != "#":
            posSol.append((row + 1, col))
        if row - 1 >= 0 and self.maze[row - 1][col][0] != "#":
            posSol.append((row - 1, col))

        # Include teleportation if present
        if len(self.maze[row][col]) > 1:
            posSol.append(self.maze[row][col][1])

        return posSol

    def getCost(self, current, neighbor):
        """Get the cost of moving to the neighbor."""
        row, col = neighbor
        # If the cell is a wall, return a very high cost (inaccessible)
        if self.maze[row][col][0] == "#":
            return float('inf')
        
        # If the cell is the goal, return a cost of 0
        if self.maze[row][col] == "G":
            return 0
        
        # Otherwise, return the cost value from the cell
        return self.maze[row][col][0]

    def reconstruct_path(self, parent):
        """Reconstruct the path from the goal to the start."""
        path = []
        current = self.goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

    def calculate_path_cost(self, path):
        """Calculate the total cost of the given path."""
        total_cost = 0
        for row, col in path:
            if isinstance(self.maze[row][col][0], int):  # Only add numeric costs
                total_cost += self.maze[row][col][0]
        return total_cost


# Example Usage
'''n = 5  # Fixed Maze size to 5x5
maze = createMaze(n)  # Generate a random maze of size 5x5
print("Generated Maze:")
for row in maze:
    print(row)'''

maze = [[[0], ['#'], ['#'], ['#'], ['#']],

[[4], [3], [2], [10], [4]],

[[4], [4], [4], ['#'], [4, (3, 4)]],

[['#'], [4], [4, (2, 1)], ['#'], [4]],

[[4, (1, 0)], [4], [3], [4], 'G']]
# BFS: [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
# AS: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
print("\nA* Solution Path:")
astar = AStarSolution(maze)
solution_path, visited_nodes, total_cost = astar.aStarSearch()

print("Solution Path:", solution_path)
print("Visited Nodes in Order:", visited_nodes)
print("Total Cost of the Solution Path:", total_cost)