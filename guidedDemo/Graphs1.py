##### BFT Uses a queue to organize what nodes get visited
def bft(start_node):
  # make a queue to store the nodes we will visit
  q = Queue()
  # make a set of unique values of all nodes we have already visited
  visited = set()
  # enqueue the start node that begins the while loop
  q.enqueue(start_node)
  # while this queue isn't empty:
  while q.length():
  ## dequeue whatever is at the front, and this is our current node
  ## mark this node as having been visited by adding node to set 
    current_node = q.dequeue()
    if current_node not in visited:
      visited.add(current_node)
      print(current_node)
  ## get all of the nodes that the current node knows about
    neighbors = getNeighbors()
  ## for each of those friends:
    for neighbor in neighbors:
  ## put them in the queue to be visited
      q.enqueue(neighbor)

##### DFT Uses a stack to organize what nodes get visited
def dft(start_node):
  # make a stack, for nodes we are about to visit
  stack = []
  # make a list of for visited nodes
  visited = set()
  # put the start node on the stack
  stack.push(start_node)
  # while this stack isn't empty
  # pop off whatever is on top of the stack, this is the current_node
  while len(stack):
    current_node = stack.pop()
  ## if current_node has not yet been visited:
    if current_node not in visited:
  ## mark the current_node as visited by putting it in our visited list
      visited.add(current_node)
  ## get all of the current_node's friends / neighbors
      neighbors = getNeighbors()
  ## for each of those friends:
      for neighbor in neighbors:
  ##   put them into our stack to be visited
        stack.append(neighbor)


