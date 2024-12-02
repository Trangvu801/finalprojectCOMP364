import tkinter as tk
import random
import createMaze
import BFSSolution
class MazeApp:
    def __init__(self, root, maze_size=5):
        self.root = root
        self.maze_size = maze_size
        self.maze = None
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()
        self.generate_button = tk.Button(root, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()
        self.generate_maze()

        # Add button for BreadthFirstSearch
        self.BFS_button = tk.Button(root, text="Breadth First Search", command=self.usingBFS)
        self.BFS_button.pack()
        #self.usingBFS()

    def generate_maze(self):
        self.maze = createMaze.createMaze(self.maze_size)
        self.display_maze()

    def display_maze(self):
        # Clear the current grid
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        # Display the maze
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
                    if row == 0 and col == 0:
                        color = "red"
                        text = "S"
                    else:  
                        color = "white"
                        text = str(value[0])
                elif len(value) > 1 and isinstance(value[1], tuple):
                    color = "yellow"
                    text = str(value[1])
                else:
                    color = "white"
                    text = ""
                label = tk.Label(self.grid_frame, text=text, font = ("Helvetica", 12), bg=color, width=15, height=5, borderwidth=2, relief="solid")
                label.grid(row=row, column=col)
    # Adding functions for Breadth First Search
    def usingBFS(self):
        s = BFSSolution.Solution(self.maze)
        self.path = s.backtrackPath()
        self.displayBFS()
    def displayBFS(self):
        # Clear the current grid
        #for widget in self.grid_frame.winfo_children():
        #    widget.destroy()
              
        for pos in range(len(self.path)):
            cell = self.path[pos]
            row, col = cell[0],cell[1]
            value = self.maze[row][col]
            color = "red"
            if value == "G":
                text = "Good Job!"
                
            elif len(value) == 1 and isinstance(value[0], int):
                text = str(value[0])
            elif len(value) > 1 and isinstance(value[1], tuple):
                if self.path[pos+1] == value[1]:
                    text = "Let's teleport to" + "\n" + str(value[1])
                else:    
                    text = "No teleport"

            label = tk.Label(self.grid_frame, text=text, font = ("Helvetica", 12), bg=color, width=15, height=5, borderwidth=2, relief="solid")
            label.grid(row=row, column=col)    

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Generator")
    app = MazeApp(root, maze_size=5)
    root.mainloop()
