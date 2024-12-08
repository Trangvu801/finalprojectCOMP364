# create BFS (Breadth first search)
import createMaze
import timeit
class Solution():
  def __init__(self, maze):
    self.maze = maze
    self.start = maze[0][0]
    self.goal = maze[len(maze)-1][len(maze)-1]
  def BreadthFirstSearch(self):
    visitedNode = []
    graph = {}
    cur = (0,0)
    queue =  []
    if self.maze[cur[0]][cur[1]] == self.goal:
      return cur
    else:
      sols = self.possibleSolution(cur)
      queue += sols
      graph[cur] = sols
      visitedNode.append(cur)
      while len(queue) > 0:
        cur = queue.pop(0)
        if self.maze[cur[0]][cur[1]] == self.goal:
          break
        else:  
          if cur not in visitedNode:
            queue += self.possibleSolution(cur)
            visitedNode.append(cur)
            graph[cur] = self.possibleSolution(cur)
    return graph, visitedNode
  def possibleSolution(self,cur):
    posSol = []
    row, col = cur[0], cur[1]
    if self.maze[row][col] == self.goal:
      return self.goal
    # left
    if col-1 >= 0 and self.maze[row][col-1][0] != "#":
      posSol.append((row,col-1))
    # right
    if col+1 < len(self.maze) and self.maze[row][col+1][0] != "#":
      posSol.append((row,col+1))
    # down
    if row+1 < len(self.maze) and self.maze[row+1][col][0] != "#":
      posSol.append((row+1,col))
    # up
    if row-1 >= 0 and self.maze[row-1][col][0] != "#":
      posSol.append((row-1,col))
    # teleport
    if len(self.maze[row][col]) > 1:
      posSol.append(self.maze[row][col][1])
    return posSol
  def backtrackPath(self):
    path = []
    graph, visitedNode = self.BreadthFirstSearch()
    # it will always be the first parent
    cur = (len(self.maze)-1,len(self.maze)-1)
    while cur != (0,0):
      path.append(cur)
      for node in graph:
        if cur in graph[node]:
          cur = node
          break
    path.append((0,0))
    path.reverse()
    return path, visitedNode


'''n = 1
while n < 10:
  print("Trial: " + str(n) + "\n")
  maze = createMaze.createMaze(n)
  print("\n" + "Solution: " + "\n")
  s = Solution(maze)
  print(s.backtrackPath())
  #runtime = timeit.timeit("s.BreadthFirstSearch()", globals=globals(), number=1)  # Run function once
  #print(f"Function runtime: {runtime:.6f} seconds")
  n += 1   
  
  #EX: [(0, 0), (0, 1), (1, 2), (2, 2), (2, 3), (3, 3)]'''