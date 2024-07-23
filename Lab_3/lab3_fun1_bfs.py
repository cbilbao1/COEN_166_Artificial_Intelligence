# paste your code:
def breadthFirstSearch(problem):
    #import time
    
    """
    Search the shallowest nodes in the search tree first.
    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
    #Parameter 'problem' gives you all the information of the simulation,
    #taken from searchAgents.py as PositionSearchProblem
    #Queue taken from util.py
    
    #Defines all directions
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST
    
    #Setup, take information from parameter 'problem'
    #Node(state, parent, action, path_cost)
    #S = problem.getStartState()
    S = Node(problem.getStartState(), None, None, 0)
    n_curr = S #Initialize the current node to Start node
    #A1 = Node("A", S, "Up", 4)
    #B1 = Node("B", S, "Down", 3)
    #B2 = Node("B", A1, "Left", 6)
    #B1 == B2
    #Create a Queue
    from util import Queue
    queue = Queue()
    #Create an set of visited nodes
    visitedNodes = set()
    
    #Create an array of moves, which makes up the solution
    solution = []
    
    #NOTE: MAKE SURE TO PUSH STARTING NODE INTO QUEUE
    queue.push(S)
    
    #We have visited the starting node, so mark it as visited
    #visitedNodes.append(S)
    
    #Boolean to store if we visited this current node, initialized to false
    #isVisted = False
    
    #print ('Start State', n_curr)
    print ('Start State', n_curr.state)
    #print ('Start Actions', problem.getActions(n_curr))
    print ('Start Actions', problem.getActions(n_curr.state))
    print ('Queue Start', queue.list)
    
    #Search the shallowest nodes in the search tree first
    #We will run the simulation until the queue is fully emptied out (means we visited all)
    while (queue.isEmpty() == False):
        #time.sleep(0.05)
        print ('Top Queue', queue.list)
        print ('Top Visited Nodes', visitedNodes)
        
        isVisited = False
        #TODO
        #Set the current node to the item first in line in the queue
        print ('Size of queue', len(queue.list))
        n_curr = queue.list.__getitem__(len(queue.list) - 1)
        #print('Current', n_curr)
        print('Current', n_curr.state)
 
        #Check if the current location has been visited using the visitedNodes array
        for x in visitedNodes:
            if (x == n_curr):
                isVisited = True
                queue.pop()
                #print('We have visited', n_curr)
                print('We have visited', n_curr.state)
 
        #Not visited, this means we expand the node
        #n_curr.state
        if (isVisited == False):
            visitedNodes.add(n_curr)
 
            #Mark the current node as visited by removing it from the queue
            queue.pop()
 
            #Expand the node
            #Run goal_test, if goal node, return solution
            #if (problem.goalTest(n_curr) == True):
            if (problem.goalTest(n_curr.state) == True):
                sol = []
 
                print ('Success')
                #TO DO
                #After finding the solution, reconstruct the path
                #Do this until we reach back to the starting state
                while (n_curr != S):
                    sol.append(n_curr.state)
 
                    #Add the current node to the solution set
                    solution.append(n_curr)
                    #Backtrack, go to the parent node
                    print ('Parent', n_curr.state)
                    n_curr = n_curr.parent
                    print ('Solution', solution)
                    print ('Sol', sol)
                    print ('Queue length', len(sol))
                #Reverse the order of the array
                #solution = solution.reverse()
                solution.reverse()
                #sol = sol.reverse()
                #Add the starting element, for the backtracking calculations
                print ('S start state', S.state)
                sol.append(S.state)
                sol.reverse()
                num = len(sol)
                print ('Reverse Sol', sol)
                
                print ('VISITED NODES LENGTH: ', len(visitedNodes))
 
                #[s, s, w, s, w, w, s, w]
                #This array actually holds the actions for the simulation to work
                finalSolution = []
 
                #Find the action set based on the information
                for i in range(0, num - 1):
                    #The vector will tell us the direction the agent moved
                    #temp = sol[i + 1] - sol[i]
                    temp = tuple(map(lambda i, j: i - j, sol[i + 1], sol[i]))
                    print ('Temp calculation', temp)
                    if (temp == (0, 1)):
                        finalSolution.append(n)
                    elif (temp == (1, 0)):
                        finalSolution.append(e)
                    elif (temp == (0, -1)):
                        finalSolution.append(s)
                    elif (temp == (-1, 0)):
                        finalSolution.append(w)
                print('Final Solution', finalSolution)
                return finalSolution
 
            #Generate the node's successors (the adjacent ones), put into Frontier Queue
 
            #Get the list of actions
            #print ('Actions', problem.getActions(n_curr))
            #print ('Actions', problem.getActions(n_curr.state))
            #actions = problem.getActions(n_curr)
            actions = problem.getActions(n_curr.state)
            print ('Queue', queue.list)
            print ('Visited Nodes', visitedNodes)
 
            #For every action, we create a new node, add to Frontier Queue
            #TO DO
            for act in actions:
                #Create new node information
                #TO DO ------- n_new = (n_curr.getResult(STATE, ACTION), n_curr, act, getCost(STATE, ACTION))
                #n_new = problem.getResult(n_curr, act)
                n_new = Node(problem.getResult(n_curr.state, act), n_curr, act, problem.getCost(n_curr.state, act))
                print ('Act', act)
                print ('n_new', n_new)
                #n_new = Node(n_curr.getResult(n_curr, act), n_curr, act, n_curr.getCost(n_curr, act))
                #queue.push(act)
                #ONLY ADD IF IT IS NOT CURRENTLY IN THE QUEUE
                #TODO CURRENTLY RUNNING INTO AN INFINITE LOOP, WEED OUT WHAT YOU WANT TO ADD
                #SUGGESTION: FLIP THE LOGIC HERE..?
                inQueue = False
                print('Queue list', queue.list)
                for x in queue.list:
                    print ('Item', x)
                    if (n_new == x):
                        inQueue = True
                if (inQueue == False):
                    queue.push(n_new)
            print('')
 
 
 
util.raiseNotDefined()