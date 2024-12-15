import tkinter as tk
import random
import createMaze
import BFSSolution
from DFSSolution import DFSSolution
from AStarSolution import AStarSolution
from EuclideanAStarSolution import EuclideanAStarSolution
import time

class MazeApp:
    def __init__(self, root, maze_size):
        self.root = root
        self.maze_size = maze_size
        self.maze = None
        self.path = []  # Initialize the path attribute
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        # Frame for buttons to arrange them horizontally
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # "Generate Maze" button, made larger and placed above other buttons
        self.generate_button = tk.Button(self.button_frame, text="Generate Maze", command=self.generate_maze, height=2, width=20)
        self.generate_button.pack(pady=5)  # Adding some space above for separation

        # Frame to hold BFS, DFS, and A* buttons horizontally
        self.solve_buttons_frame = tk.Frame(root)
        self.solve_buttons_frame.pack()

        # Buttons for solving the maze
        self.BFS_button = tk.Button(self.solve_buttons_frame, text="Breadth First Search", command=self.usingBFS, width=20)
        self.BFS_button.pack(side=tk.LEFT, padx=5)

        self.DFS_button = tk.Button(self.solve_buttons_frame, text="Depth First Search", command=self.usingDFS, width=20)
        self.DFS_button.pack(side=tk.LEFT, padx=5)

        self.AStar_button = tk.Button(self.solve_buttons_frame, text="A* Search", command=self.usingAStar, width=20)
        self.AStar_button.pack(side=tk.LEFT, padx=5)

        self.EuclideanAStar_button = tk.Button(self.solve_buttons_frame, text="Euclidean A* Search", command=self.usingEuclideanAStar, width=20)
        self.EuclideanAStar_button.pack(side=tk.LEFT, padx=5)

        # Label for displaying results (visited nodes and total cost)
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), anchor="w", justify="left")
        self.result_label.pack(pady=10)

        #self.generate_maze()
        self.maze = maze = [[[0], ['#'], ['#'], ['#'], ['#']],

                            [[4], [3], [2], [10], [4]],

                            [[4], [4], [4], ['#'], [4, (3, 4)]],

                            [['#'], [4], [4, (2, 1)], ['#'], [4]],

                            [[4, (1, 0)], [4], [3], [4], 'G']]
        self.display_maze()                    

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields,height=2, width=20)
        self.reset_button.pack(pady=5)
    def reset_fields(self):
        # Clear any result labels
        self.result_label.config(text="")
        # Reset the path to empty
        self.path = []
        self.display_maze()#.delete(0, tk.END)

    def generate_maze(self):
        self.result_label.config(text="")
        self.maze = createMaze.createMaze(self.maze_size)
        self.display_maze()

    def display_maze(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                value = self.maze[row][col]
                if value == "G":
                    color = "green"
                    text = "G"
                elif value[0] == "#":
                    color = "gray"
                    text = "#"
                elif len(value) == 1 and isinstance(value[0], int):
                    color = "red" if row == 0 and col == 0 else "white"
                    text = "S" if row == 0 and col == 0 else str(value[0])
                    
                elif len(value) > 1 and isinstance(value[1], tuple):
                    color = "yellow"
                    text = str(value[1])+"\n"+str(value[0])
                else:
                    color = "white"
                    text = ""
                label = tk.Label(self.grid_frame, text=text, font=("Helvetica", 12), bg=color, width=15, height=5, borderwidth=2, relief="solid")
                label.grid(row=row, column=col)
        
    def usingBFS(self):
        start_time = time.time()
        solver = BFSSolution.Solution(self.maze)
        self.path, visited_nodes = solver.backtrackPath()  # Update the path
        end_time = time.time()

        self.displayPath("BFS")
        #self.result_label.config(text="BFS Path: Not applicable to BFS")  # You can adjust this message as needed.
        # Update the result_label with the visited nodes and total cost
        #runtime = timeit.timeit("solver.BreadthFirstSearch()", globals=globals(), number=1)  # Run function once
        visited_nodes_count = len(visited_nodes)
        solution_path_count = len(self.path)
        result_text = f"Visited Nodes: {visited_nodes}\nTotal Length of Visited Nodes: {visited_nodes_count}\nTotal Length of Solution Path: {solution_path_count}\nFunction runtime: {end_time - start_time:.10f} seconds"
        self.result_label.config(text=result_text)

    def usingDFS(self):
        start_time = time.time()
        solver = DFSSolution(self.maze)
        solution_path, visited_nodes, total_cost = solver.getPath()  # Get the result from DFS
        end_time = time.time()
        self.path = solution_path  # Update path
        self.displayPath("DFS")
        # Update the result_label with the visited nodes and total cost
        visited_nodes_count = len(visited_nodes)
        solution_path_count = len(self.path)
        result_text = f"Visited Nodes: {visited_nodes}\nTotal Length of Visited Nodes: {visited_nodes_count}\nTotal Length of Solution Path: {solution_path_count}\nFunction runtime: {end_time - start_time:.10f} seconds"
        self.result_label.config(text=result_text)

    def usingAStar(self):
        start_time = time.time()
        solver = AStarSolution(self.maze)
        solution_path, visited_nodes, total_cost = solver.aStarSearch()  # Get the result from A*
        end_time = time.time()
        if solution_path == "No path found":
            print("A* Search: No path found.")
            self.path = []  # Ensure path is empty if no solution
        else:
            self.path = solution_path  # Update path
            self.displayPath("A* Search")
            # Update the result_label with the visited nodes and total cost
            visited_nodes_count = len(visited_nodes)
            solution_path_count = len(self.path)
            result_text = f"Visited Nodes: {visited_nodes}\nTotal Cost: {total_cost}\nTotal Length of Visited Nodes: {visited_nodes_count}\nTotal Length of Solution Path: {solution_path_count}\nFunction runtime: {end_time - start_time:.10f} seconds"
            
            self.result_label.config(text=result_text)
    
    def usingEuclideanAStar(self):
        start_time = time.time()
        solver = EuclideanAStarSolution(self.maze)
        solution_path, visited_nodes, total_cost = solver.aStarSearch()  # Get the result from Euclidean A*
        end_time = time.time()
        if solution_path == "No path found":
            print("Euclidean A* Search: No path found.")
            self.path = []  # Ensure path is empty if no solution
        else:
            self.path = solution_path  # Update path
            self.displayPath("Euclidean A* Search")
            # Update the result_label with the visited nodes and total cost
            visited_nodes_count = len(visited_nodes)
            solution_path_count = len(self.path)
            result_text = f"Visited Nodes: {visited_nodes}\nTotal Cost: {total_cost}\nTotal Length of Visited Nodes: {visited_nodes_count}\nTotal Length of Solution Path: {solution_path_count}\nFunction runtime: {end_time - start_time:.10f} seconds"
            
            self.result_label.config(text=result_text)

    def displayPath(self, algo_name):
        # Check if path is not empty
        if not self.path:  # If path is empty, handle the case
            print(f"No path found for {algo_name}")
            self.result_label.config(text=f"No path found for {algo_name}")
            return
        
        for pos in range(len(self.path)):
            cell = self.path[pos]
            row, col = cell[0], cell[1]
            value = self.maze[row][col]

            color = "red"
            if value == "G":
                text = f"Goal ({algo_name})"
            elif len(value) == 1 and isinstance(value[0], int):
                text = str(value[0])
            elif len(value) > 1 and isinstance(value[1], tuple):
                if pos + 1 < len(self.path) and self.path[pos + 1] == value[1]:
                    text = f"Teleport to\n{value[1]}\n{value[0]}"
                else:
                    text = f"No teleport\n{value[0]}"
        
            label = tk.Label(self.grid_frame, text=text, font=("Helvetica", 12), bg=color, width=15, height=5, borderwidth=2, relief="solid")
            label.grid(row=row, column=col)
            self.root.update()  # Update the GUI to reflect changes
            time.sleep(0.5) 
            

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Solver")
    app = MazeApp(root, maze_size=5)
    root.mainloop()
