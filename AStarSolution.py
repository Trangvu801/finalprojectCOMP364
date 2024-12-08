import heapq
from createMaze import createMaze

class AStarSolution:
    def __init__(self, maze):
        """
        Initializes the AStarSolution class.

        Parameters:
        - maze: A 2D list representing the maze structure.
        """
        self.maze = maze
        self.start = (0, 0)
        self.goal = (len(maze) - 1, len(maze) - 1)

    def heuristic(self, a, b):
        """Calculate the Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def aStarSearch(self):
        """
        Performs the A* search algorithm.

        Returns:
        - path: The solution path from start to goal.
        - visited_nodes: The list of visited nodes in order.
        - total_length_visited_nodes: The total length of the visited nodes.
        - path_length: The total length of the solution path.
        - total_cost: The total cost of the solution path.
        """
        open_set = []
        heapq.heappush(open_set, (0, self.start))

        g_cost = {self.start: 0}  # Cost from start to a node
        parent = {self.start: None}  # To reconstruct the path
        visited_nodes = []  # Order of visited nodes

        while open_set:
            _, current = heapq.heappop(open_set)

            if current in visited_nodes:
                continue

            visited_nodes.append(current)  # Track visitation order

            if current == self.goal:
                path = self.reconstruct_path(parent)
                path_length = len(path)
                total_length_visited_nodes = self.calculate_visited_path_length(visited_nodes)
                total_cost = self.calculate_path_cost(path)
                return path, visited_nodes, total_length_visited_nodes, path_length, total_cost

            for neighbor in self.possibleSolution(current):
                tentative_g_cost = g_cost[current] + self.getCost(current, neighbor)

                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    parent[neighbor] = current

                    f_cost = tentative_g_cost + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_cost, neighbor))

        return "No path found", visited_nodes, 0, 0, 0

    def possibleSolution(self, cur):
        """
        Identify valid neighbors for the current cell.
        """
        pos_sol = []
        row, col = cur[0], cur[1]

        # Check all four directions
        if col - 1 >= 0 and self.maze[row][col - 1][0] != "#":  # Left
            pos_sol.append((row, col - 1))
        if col + 1 < len(self.maze) and self.maze[row][col + 1][0] != "#":  # Right
            pos_sol.append((row, col + 1))
        if row + 1 < len(self.maze) and self.maze[row + 1][col][0] != "#":  # Down
            pos_sol.append((row + 1, col))
        if row - 1 >= 0 and self.maze[row - 1][col][0] != "#":  # Up
            pos_sol.append((row - 1, col))

        # Include teleportation if present
        if len(self.maze[row][col]) > 1:
            pos_sol.append(self.maze[row][col][1])

        return pos_sol

    def getCost(self, current, neighbor):
        """
        Get the cost of moving to the neighbor.
        """
        row, col = neighbor
        if self.maze[row][col][0] == "#":
            return float('inf')
        if self.maze[row][col] == "G":
            return 0
        return self.maze[row][col][0]

    def reconstruct_path(self, parent):
        """
        Reconstruct the path from the goal to the start.
        """
        path = []
        current = self.goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

    def calculate_path_cost(self, path):
        """
        Calculate the total cost of the given path.
        """
        total_cost = 0
        for row, col in path:
            if isinstance(self.maze[row][col][0], int):  # Only add numeric costs
                total_cost += self.maze[row][col][0]
        return total_cost

    def calculate_visited_path_length(self, visited_nodes):
        """
        Calculate the total length of the path for all visited nodes.
        """
        total_length = 0
        for i in range(1, len(visited_nodes)):
            prev = visited_nodes[i - 1]
            curr = visited_nodes[i]
            total_length += abs(prev[0] - curr[0]) + abs(prev[1] - curr[1])
        return total_length


# Main Program
n = 5  # Fixed Maze size to 5x5
maze = createMaze(n)  # Generate a random maze of size 5x5
print("Generated Maze:")
for row in maze:
    print(row)

# Solve the maze using A*
astar = AStarSolution(maze)
solution_path, visited_nodes, total_length_visited_nodes, path_length, total_cost = astar.aStarSearch()

# Print the results
print("\nA* Solution Path:", solution_path)
print("Visited Nodes in Order:", visited_nodes)
print("Total Length of Visited Nodes:", total_length_visited_nodes)
print("Total Length of Solution Path:", path_length)
print("Total Cost of the Solution Path:", total_cost)
