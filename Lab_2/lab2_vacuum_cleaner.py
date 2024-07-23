# -*- coding: utf-8 -*-
#import unittest
"""
class Testlab2(unittest.TestCase):
 def test_lab2(self):
 self.assertEqual(xxx)
"""
"""
Created on Mon Apr 4 14:51:35 2022
@author: gabby
"""
"""
Function for testing whether the state we are in is the desired state
"""
def goal_test(state):
    """
    As long as both spots are clean, it doesn't matter where we are
    """
    if state[0] == 'Clean' and state[1] == 'Clean':
        return True
    else: #One of the spots aren't clean
        return False
 
"""
Function for determining the next action, returns list of possible actions
"""
def Actions(state):
    #Brute force implementation, 8 states needed
    if (state[state[2]] == 'Dirty'): #If the slot we are in is dirty, suck
        return 'Suck'
    elif state[2] == 0: #If we are in the left slot and it is clean, go to the right slot
        #Go right
        return 'Right'
    else: #We are in the right slot, and it is clean
        #Go Left
        return 'Left'
 
"""
Function that updates state information the next action, returns state information
"""
def Transition(state, action):
    """
    Brute force implementation, 8 states needed
    """
    if action == 'Left': #If the action is left, only change the location
        state[2] = 0
    elif action == 'Right': #If the action is right, only change the location
        state[2] = 1
    else: #In this case, we are going to suck, make slot clean
        state[state[2]] = 'Clean'

def simulate(init_state, sol):
    currState = [' ',' ', 0]
    for i in range(3):
        currState[i] = init_state[i]
    print ("Initial state:", currState)
    #currState = ['Dirty', 'Clean', 1]
    solution = sol
    #cost = 0
    
    #possActions = Actions(currState) #A list of possible actions in the current state
    action = [' '] #The current action
    #print (Actions(currState))
    #print (possActions)
    #print (possActions[1])
    
    #print (goal_test(currState))
    
    #possActionsIndex = 0
    """
    Handles the simulation, ends when the current state is the goal state
    """
    while goal_test(currState) != True:
        action = Actions(currState) #Determine the next course of action
        solution.append(action) #Add this action to the solution set
        #temp = Transition(currState, action) #Update the current state to the next state
        #for i in range(3):
            #currState[i] = temp[i] #Go to new state
        Transition(currState, action)
    
    print('Final Solution:', solution, ', Cost:', len(solution))
"""
Main function, executes code
""" 
if __name__=='__main__':
 #unittest.main()
 
    print ("Test 1 :")
    simulate(['Dirty', 'Dirty', 0], []) #Left dirty, Right dirty, Location left
    print ("")
    
    print ("Test 2 :")
    simulate(['Dirty', 'Dirty', 1], []) #Left dirty, Right dirty, Location left
    print ("")
    
    print ("Test 3 :")
    simulate(['Clean', 'Dirty', 0], []) #Left clean, Right dirty, Location left
    print ("")
    
    print ("Test 4 :")
    simulate(['Dirty', 'Clean', 1], []) #Left dirty, Right clean, Location right
    print ("")
    
    print ("Test 5 :")
    simulate(['Dirty', 'Clean', 0], []) #Left dirty, Right clean, Location left
    print ("")
    
    print ("Test 6 :")
    simulate(['Clean', 'Dirty', 1], []) #Left dirty, Right clean, Location right
    print ("")
    
    print ("Test 7 :")
    simulate(['Clean', 'Clean', 0], []) #Left clean, Right clean, Location left
    print ("")
    
    print ("Test 8 :")
    simulate(['Clean', 'Clean', 1], []) #Left clean, Right clean, Location right
    print ("")