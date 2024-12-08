from createMaze import createMaze

class Solution:
    def __init__(self, maze):
        """
        Initializes the Solution class.

        Parameters:
        - maze: A 2D list representing the maze structure. Each cell can contain:
          - A cost value and optional teleport coordinates (e.g., [6, (1,1)]).
          - '#' indicating a wall.
          - 'G' indicating the goal position.

        Attributes:
        - self.maze: Stores the input maze.
        - self.start: The starting position (top-left corner, implicitly (0,0)).
        - self.goal: The goal position (bottom-right corner, implicitly (n-1,n-1)).
        """
        self.maze = maze
        self.start = maze[0][0]
        self.goal = maze[len(maze) - 1][len(maze) - 1]

    def BreadthFirstSearch(self):
        """
        Performs Breadth-First Search to find a path to the goal.

        Returns:
        - graph: A dictionary representing the graph of nodes and their possible moves.
        - visited_nodes: A list of nodes visited in the order they were explored.
        """
        visited_nodes = []
        graph = {}
        cur = (0, 0)
        queue = []

        if self.maze[cur[0]][cur[1]] == self.goal:
            return cur
        else:
            sols = self.possibleSolution(cur)
            queue += sols
            graph[cur] = sols
            visited_nodes.append(cur)
            
            while len(queue) > 0:
                cur = queue.pop(0)
                if self.maze[cur[0]][cur[1]] == self.goal:
                    break
                else:  
                    if cur not in visited_nodes:
                        queue += self.possibleSolution(cur)
                        visited_nodes.append(cur)
                        graph[cur] = self.possibleSolution(cur)
        
        return graph, visited_nodes

    def possibleSolution(self, cur):
        """
        Identifies all valid moves from the current cell.

        Parameters:
        - cur: The current cell being explored, represented as a tuple (row, column).

        Returns:
        - A list of valid neighboring cells or teleport locations that can be visited.
        """
        pos_sol = []
        row, col = cur[0], cur[1]

        if self.maze[row][col] == self.goal:
            return self.goal

        # Check each direction for valid moves (not blocked by walls)
        if col - 1 >= 0 and self.maze[row][col - 1][0] != "#":  # Left
            pos_sol.append((row, col - 1))
        if col + 1 < len(self.maze) and self.maze[row][col + 1][0] != "#":  # Right
            pos_sol.append((row, col + 1))
        if row + 1 < len(self.maze) and self.maze[row + 1][col][0] != "#":  # Down
            pos_sol.append((row + 1, col))
        if row - 1 >= 0 and self.maze[row - 1][col][0] != "#":  # Up
            pos_sol.append((row - 1, col))
        
        # Teleportation (if the current cell has teleport coordinates)
        if len(self.maze[row][col]) > 1:
            pos_sol.append(self.maze[row][col][1])

        return pos_sol

    def backtrackPath(self):
        """
        Backtracks from the goal to the start to reconstruct the solution path.

        Returns:
        - path: The path from start to goal.
        - visited_nodes: The list of visited nodes in the BFS search.
        - total_visited_nodes: The total number of visited nodes.
        - path_length: The total length of the solution path.
        """
        path = []
        graph, visited_nodes = self.BreadthFirstSearch()
        
        # Start at the goal position
        cur = (len(self.maze) - 1, len(self.maze) - 1)
        
        # Backtrack from goal to start
        while cur != (0, 0):
            path.append(cur)
            for node in graph:
                if cur in graph[node]:
                    cur = node
                    break
        
        # Add the start node and reverse the path
        path.append((0, 0))
        path.reverse()

        total_visited_nodes = len(visited_nodes)
        path_length = len(path)

        return path, visited_nodes, total_visited_nodes, path_length


# Main Program
n = 5  # Fixed Maze size to 5x5
maze = createMaze(n)  # Generate a random maze of size 5x5
print("Generated Maze:")
for row in maze:
    print(row)

# Solve the maze using BFS
solution = Solution(maze)
path, visited_nodes, total_visited_nodes, path_length = solution.backtrackPath()

# Print the results
print("\nBFS Solution Path:", path)
print("Visited Nodes in Order:", visited_nodes)
print("Total Number of Visited Nodes:", total_visited_nodes)
print("Total Length of Solution Path:", path_length)
