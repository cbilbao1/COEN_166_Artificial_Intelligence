#Function 1
def getQValue(self, state, action):
    """
        Returns Q(state,action)
        Should return 0.0 if we have never seen a state
        or the Q node value otherwise
    """
    "*** YOUR CODE HERE ***"
    if not self.q_values[(state,action)]:
        return 0.0
    else:
        return self.q_values[(state, action)]

#Function 2
def computeValueFromQValues(self, state):
    """
        Returns max_action Q(state,action)
        where the max is over legal actions. Note that if
        there are no legal actions, which is the case at the
        terminal state, you should return a value of 0.0.
    """
    "*** YOUR CODE HERE ***"
    legalActions = self.getLegalActions(state)
    if len(legalActions) == 0:
        return 0.0
    temp = util.Counter()
    for action in legalActions:
        temp[action] = self.getQValue(state, action)
    return temp[temp.argMax()]

#Function 3
def computeActionFromQValues(self, state):
    """
        Compute the best action to take in a state. Note that if there
        are no legal actions, which is the case at the terminal state,
        you should return None.
    """
    "*** YOUR CODE HERE ***"
    maxqval = self.getValue(state)
    best_action = []
    for action in self.getLegalActions(state):
        if self.getQValue(state, action) == maxqval:
            best_action.append(action)
    if len(best_action)==0:
        return None
    else:
        return random.choice(best_action)

#Function 4
def getAction(self, state):
    """
        Compute the action to take in the current state. With
        probability self.epsilon, we should take a random action and
        take the best policy action otherwise. Note that if there are
        no legal actions, which is the case at the terminal state, you
        should choose None as the action.
        HINT: You might want to use util.flipCoin(prob)
        HINT: To pick randomly from a list, use random.choice(list)
    """
    # Pick Action
    "*** YOUR CODE HERE ***"
    legalActions = self.getLegalActions(state)
    exploration = util.flipCoin(self.epsilon)
    if exploration:
        return random.choice(legalActions)
    else:
        return self.getPolicy(state)
    
#Function 5
def update(self, state, action, nextState, reward):
    """
        The parent class calls this to observe a
        state = action => nextState and reward transition
        You should do your Q-Value update here
        NOTE: You should never call this function,
        it will be called on your behalf
    """
    "*** YOUR CODE HERE ***"
    oldQvalue = self.getQValue(state, action)
    old_func = (1 - self.alpha) * oldQvalue
    reward_func = self.alpha * reward
    if not nextState:
        self.q_values[(state, action)] = old_func + reward_func
    else:
        nextState_func = self.alpha * self.discount * self.getValue(nextState)
        self.q_values[(state, action)] = old_func + reward_func + nextState_func

#Function 6
def getPolicy(self, state):
    return self.computeActionFromQValues(state)

#Function 7
def getValue(self, state):
    return self.computeValueFromQValues(state)