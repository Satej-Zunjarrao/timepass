
def bfs(visited, graph, node,goal):
    queue.append (node)
    visited.append(node)
    while queue:
        s = queue. pop (0)
        print (s, end = "\n")
        for neighbour in graph [s]:

          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
            if goal is visited:
                break
#PRANAV KUMAR
#PRN 1032200232

if __name__ == '__main__':
  
  graph = {
  '0': ['1', '2', '3'],
  '1': ['0', '4'],
  '2': ['4', '5'],
  '3': ['0', '5'],
  '4': ['1', '5'],
  '5': ['5']
  }

  visited = []
  queue = []
  goal = '5'
  bfs(visited,graph,'0',goal)