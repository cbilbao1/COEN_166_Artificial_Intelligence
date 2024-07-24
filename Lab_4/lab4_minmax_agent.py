class MinimaxAgent(MultiAgentSearchAgent):
    #Function 1
    def getAction(self, gameState):
        minAgent = gameState.getNumAgents() - 1 #pacman is not a min agent
        best_action = self.maxValue_fun(gameState, 1, minAgent)#pass agent index =1 as first ghost
        return best_action
    
    #Function 2
    def maxValue_fun(self, gameState, depth, minAgent):
        if gameState.isWin() or gameState.isLose():#terminal test
            return self.evaluationFunction(gameState)
        
        v = float("-inf")
        
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)#generate successor for each action
        
        v2 = self.minValue_fun(successor, depth, 1, minAgent)#recurse
        if v2 > v:#iterate among all succesors to find the maxval and aquire the best action that correspons to max val
            v = v2
            if depth == 1:
                best_action = action

        if depth ==1:#root node action
            return best_action
        return v#non root node action(pacman for depth 2,3,4)
    
    #Function 3
    def minValue_fun(self, gameState, depth, playerIndex, minAgent):
        if gameState.isWin() or gameState.isLose(): #terminal test
            return self.evaluationFunction(gameState)
        
        v = float("inf")
        
        actions = gameState.getLegalActions(playerIndex)
        successors = [gameState.generateSuccessor(playerIndex, action) for action in actions]#don't have to worry abt returning action
        
        if playerIndex == minAgent:#3 two things can happen here either the next thing is pacman or a leaf
            if depth < self.depth:
                for successor in successors: 
                    v = min(v, self.maxValue_fun(successor, depth + 1, minAgent))#next agent is pacman(maximizer)
            else:#depth = 4 reached as we are on the 3rd ghost but the depth is the same
                for successor in successors:
                    v = min(v, self.evaluationFunction(successor))#leaf
        
        else:#0,1,2 repeat
            playerIndex+=1
            for successor in successors:
                v = min(v, self.minValue_fun(successor, depth, playerIndex, minAgent))
        return v