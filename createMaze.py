# create maze
import random
import time
import tkinter as tk
def createMaze(n):
  maze = [[[0] for i in range(n)] for j in range(n)]
  # fixed starting location
  start = maze[0][0]
  wall_path_list = ["#",random.randint(0,10)]
  teleportList = ["NT","T"]
  teleVisited = []
  for row in range(n):
    for col in range(n):
      # random walls
      if row != 0 or col != 0:
        if row!=n-1 or col != n-1:
          maze[row][col] = [random.choice(wall_path_list)]
          if maze[row][col][0] != "#":
            if len(maze[row][col]) < 2: # means there is no teleport or not teleport assigned yet
              teleport = random.choice(teleportList)
              if teleport == "T":
                rowT = random.randint(0,n-1)
                colT = random.randint(0,n-1)
                while maze[rowT][colT][0] == "#" or (rowT,colT) in teleVisited:
                  rowT = random.randint(0,n-1)
                  colT = random.randint(0,n-1)
                maze[row][col].append((rowT,colT))
                teleVisited.append((rowT,colT))
          else:
            if (row,col) in teleVisited:
              maze[row][col] = [random.randint(0,10)]
            if row-1 >= 0 and col+1 < n:
              if maze[row-1][col+1][0] == "#":
                maze[row][col] = [random.randint(0,10)]

  # goal location
  maze[n-1][n-1] = "G"
  #print output of maze
  for row in range(n):
    print(str(maze[row]) + '\n')
  return maze

  '''Example output: of a grid 3x3
  [[0], [6], [6, (1, 1)]]

  [[6, (2, 0)], [6, (0, 1)], ['#']]

  [[6], [8], 'G']

  start at maze[0][0], and the cost of the path is put inside the list such as the cost is 0 will be [0]
  if the list is [6, (1,1)] means the cost path is 6 and the teleport location is (1,1) which is [6, (0, 1)].
  For the teleport, when we change from the current location to another location, but it doesnt mean we can get back to the old location.
  Example: we choose [6,(1,1)] and teleport, we move to place having [6,(0,1)], which means cost path of this new location is 6 and we cannot get back the
  old location, but if we choose to teleport then the next location will be at (0,1) or [6]. Generally, we just teleport to the new location,
  if that new is [6] then we will start at that location and the cost path is 6, no return back.
  '''

'''n = 1
while n < 10:
  print("Trial: " + str(n) + "\n")
  createMaze(n)
  n += 1'''

def displayMaze(maze):
    n = len(maze)
    root = tk.Tk()
    root.title("Maze GUI")

    for row in range(n):
        for col in range(n):
            if row == 0 and col == 0:
              color = "red"
              text = "S"
            value = maze[row][col]
            if value == "G":
                color = "green"
                text = "G"
            elif value[0] == "#":
                color = "gray"
                text = "#"
                text_color = "white"
            elif isinstance(value[0], int):
                if row == 0 and col == 0:
                  color = "red"
                  text = "S"
                else:  
                  color = "white"
                  text = str(value[0])
            elif len(value) > 1 and isinstance(value[1], tuple):
                color = "blue"
                text = "T"
            else:
                color = "white"
                text = ""

            label = tk.Label(root, text=text, bg=color, width=4, height=2, borderwidth=2, relief="solid")
            label.grid(row=row, column=col)

    root.mainloop()


# Example Usage
#maze_size = 5
#maze = createMaze(maze_size)
#displayMaze(maze)
