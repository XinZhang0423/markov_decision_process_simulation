from antlr4 import *
from gramLexer import gramLexer
from gramListener import gramListener
from gramParser import gramParser
import sys
import argparse
import math
from math import log
import numpy as np

import matplotlib.pyplot as plt
import random
from itertools import accumulate
from time import sleep
from math import sqrt
import scipy
import copy

class gramModelListener(gramListener):
    
    def __init__(self,mode='mc'):
        self.states=[]
        self.actions=[]
        self.mode=mode
               
    def enterStaterew(self, ctx):
        if self.mode=='mc':
            self.states = [state_mc(str(x),i) for i,x in enumerate(ctx.ID())]
        else:
            self.states = [state_mdp(str(x),i) for i,x in enumerate(ctx.ID())]
            
        rewards=[int(str(x)) for x in ctx.INT()]
        for i,s in enumerate(self.states):
            s.reward=rewards[i]  
     
    def enterStatenorew(self,ctx):
        if self.mode=='mc':
            self.states = [state_mc(str(x),i) for i,x in enumerate(ctx.ID())]
        else:
            self.states = [state_mdp(str(x),i) for i,x in enumerate(ctx.ID())]
            
        
    def enterDefactions(self, ctx):
        self.actions = [str(x) for x in ctx.ID()]  
          
    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)  
        weights = [int(str(x)) for x in ctx.INT()]
        targets = ids
        
        total_weights=sum(weights)
        flag=False
        for state in self.states:
            if state.name==dep:
                current_state = state
                flag=True
                break
        if not flag : print(f"{dep} is not defined in States")  
        
        to_states=dict()
        
        for i,target in enumerate(targets):
            proba=weights[i]/total_weights
            flag_target=False 
            for state in self.states:
                if state.name==target:
                    current_target = state
                    current_target.parents.append(current_state)
                    if self.mode == 'mc':
                        current_state.to_states[current_target] = proba
                    else: 
                        to_states[current_target] = proba
                    flag_target=True
                    break
            if not flag_target: print(f"{target} is not defined in States")
        if self.mode == 'mdp':
            print (f"add a new action {self.actions[0]} in the transitions for {current_state} ")
            current_state.actions.append(self.actions[0])
            current_state.transitions[self.actions[0]]=to_states
            print(current_state.transitions)
    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        
        weights = [int(str(x)) for x in ctx.INT()]
        targets = ids
        
        total_weights=sum(weights)
        flag=False
        for state in self.states:
            if state.name==dep:
                current_state = state
                flag=True
                break
        if not flag : print(f"{dep} is not defined in States")  
        
        to_states =dict()
        
        for i,target in enumerate(targets):
            proba=weights[i]/total_weights
            flag_target=False 
            for state in self.states:
                if state.name==target:
                    current_target = state
                    to_states[current_target]=proba
                    flag_target=True
                    break
            if not flag_target: print(f"{target} is not defined in States")
        current_state.actions.append(act)   
        current_state.transitions[act]=to_states
        print(current_state.transitions)
    def get_mc(self):
        return MarkovChain(self.states)

    def get_mdp(self):
        return MarkovDecisionProcess(self.states,self.actions)

class state():  
    
    def __init__(self,name,id,reward=0,parents=None):
        self.name = name
        self.id = id 
        self.reward=reward
        self.parents = list() if parents is None else parents
    
    def __str__(self):
        return self.name
    
    def __copy__(self):
        return state(self.name,self.id,self.reward)
    
class state_mc(state):
    
    def __init__(self,name,id,reward=0,to_states=None,parents=None):
        super().__init__(name,id,reward,parents)
        self.to_states = dict() if to_states is None else to_states
        
    def __copy__(self):
        return state_mc(self.name,self.id,self.reward,self.to_states,self.parents)
                   
class state_mdp(state):
    
    def __init__(self,name,id,reward=0,actions=None,transitions=None,parents=None):
        super().__init__(name,id,reward,parents)
        self.actions = list()  if actions is None else actions
        self.transitions=dict() if transitions is None else transitions 
    
    def __copy__(self):
        return state_mdp(self.name,self.id,self.reward,self.actions,self.transitions,self.parents)
        
# 下边是一个失败的例子，🙅🏻‍♀️，有机会再看吧
# class transition_mdp():
#     def __init__(self,from_state,action,to_states_dict,to_states_list):
#         self.from_state = from_state
#         self.action = action
#         self.to_states_dict=dict()
#         self.to_states_list=list()
#         self.probas=list()

#     def add_to_state(self,state,proba):
#         pass
    
class MarkovModel():
    
    def __init__(self,states):
        self.states = states
    
    def __str__(self):
        st = ', '.join([s.name for s in self.states]) 
        return st        

class MarkovChain(MarkovModel):
    
    def __init__(self,states):
        super().__init__(states)
    
    def __str__(self):
        st=super().__str__()
        st+= '\n'
        for s in self.states:
            st += s.name + ' -> '
            for k,v in s.to_states.items():
                st +=  str(k) +' : '+ str(v) + ';'
            st+= '\n'
        return st
    
    def simulate(self,steps,init=None,reward_mode=False):
        init=self.states[0] if not init else init
        current=init
        history = list()
        reward_final=0
        history.append(current.name)
        for i in range(steps):
            p=random.uniform(0,1)   
            pc=0
            for key,ps in current.to_states.items():
                pc+=ps
                if p<pc:
                    current=key
                    break
            if reward_mode and i!=steps-1:
                reward_final+=current.reward
            history.append(current.name)

        if reward_mode:
            return history,reward_final
        else:
            return history
          
    def check_access(self,target,steps=None):
        s0=list()
        s1=list()
        s2=list()
    
        #使用dfs找到s1和s2
        for state in self.states:
            if state.to_states.get(state,0) == 1:
                if state.name!=target:  
                    s0.append(state)
                    # print(state.name)
                    #创建堆进行dfs查找
                    dfs_list=list()
                    current_state=state
                    dfs_list.append(state)
                    while dfs_list:
                        current_state=dfs_list.pop()
                        for parent in current_state.parents:
                            if parent.to_states[current_state]==1 and parent!=state:
                                s0.append(parent)
                                # print(parent.name)
                                dfs_list.append(parent)
                                      
                else:
                    s1.append(state) 
                    # print(state.name)                 
                    dfs_list=list()
                    current_state=state
                    dfs_list.append(state)
                    while dfs_list:
                        current_state=dfs_list.pop()
                        for parent in current_state.parents:
                            if parent.to_states[current_state]==1 and parent!=state:
                                s1.append(parent)
                                # print(parent.name)
                                dfs_list.append(parent)
        #根据s0，s1构造s2 
        print('s0:')
        for s in s0:
            print(s.name+' ',end='')
            
        print('\ns1:')
        
        for s in s1:   
            print(s.name,end=' ')

        for state in self.states:
            if (state not in s0) and (state not in s1):
                s2.append(state)
          
        nb_nodes=len(s2)      
        A=np.zeros((nb_nodes,nb_nodes))
        b=np.zeros((nb_nodes,1))
        
        for i in range(nb_nodes):
            for j in range(nb_nodes):
                A[i,j]=s2[i].to_states.get(s2[j],0)
                
        for i in range(nb_nodes):
            for st in s1:
                b[i,0]+=s2[i].to_states.get(st,0)
            
        if steps:
            for i in range(steps):
                y=np.dot(A,y)+b
            res=y
        else:
            id=np.eye(nb_nodes)
            res=np.linalg.solve((id-A),b)

        results=dict()
        for i,s in enumerate(s2):
            results[s.name]=res[i]
          
        return results
     
    def reward_expected(self,target):
        s0=list()
        s1=list()
        s2=list()
    
        #使用dfs找到s1和s2
        for state in self.states:
            if state.to_states[state.name] == 1:
                if state.name!=target:
                    s0.append(state)
                    #创建堆进行dfs查找
                    dfs_list=list()
                    current_state=state
                    dfs_list.append(state)
                    while not dfs_list:
                        current_state=dfs_list.pop()
                        for parent in current_state.parents:
                            if parent.to_states[current_state.name]==1:
                                s0.append(parent)
                                dfs_list.append(parent)
                                      
                else:
                    s1.append(state)                    
                    dfs_list=list()
                    current_state=state
                    dfs_list.append(state)
                    while not dfs_list:
                        current_state=dfs_list.pop()
                        for parent in current_state.parents:
                            if parent.to_states[current_state.name]==1:
                                s0.append(parent)
                                dfs_list.append(parent)
        #根据s0，s1构造s2    
        for state in self.states:
            if (state not in s0) and (state not in s1):
                s2.append(state)
          
        nb_nodes=len(s2)      
        A=np.zeros((nb_nodes,nb_nodes))
        b=np.zeros((nb_nodes,1))
        
        for i in range(nb_nodes):
            for j in range(nb_nodes):
                A[i,j]=s2[i].to_states.get(s2[j].name,0)
                
        for i in range(nb_nodes):
            b[i,1]=s2[i].reward
            
        id=np.eye(nb_nodes)
        res=np.linalg.solve((id-A),b)
        
        results=dict()
        for i,s in enumerate(s2):
            results[s.name]=res[i]
             
        return results      
     
    def modify_model(self,target):
        states=list()
        for s in self.states:
            s0=copy.copy(s)
            if s0.name==target:
                s0.to_states={s0:1}
            states.append(s0)
        new_model=MarkovChain(states)
        return new_model
               
    def SMC_quantitatif_mc(self,steps,target,precision,error):
        new_model=self.modify_model(target)
        times=math.ceil((math.log(2)-math.log(error))/(2*precision)**2)
        res_times=0
        for i in range(times):
            res=new_model.simulate(steps)
            if res[-1]==target:
                res_times+=1
        res_proba=res_times/times
        return res_proba
    
    def SMC_qualitatif_sprt(self,steps,target,theta,epislon,alpha,beta):
        """
            H0 : γ ≥ γ0 VS H1 : γ < γ1
        """
        new_model=self.modify_model(target)
        
        gamma1=theta-epislon
        gamma0=theta+epislon
        
        FA=log((1-beta)/alpha)
        FB=log(beta/(1-alpha))

        dm=0
        m=1
        end = False
        Fm=0
        Vadd=log(gamma1/gamma0)
        Vrem=log((1-gamma1)/(1-gamma0))
        while (not end):
            res=new_model.simulate(steps)
            m+=1
            if res[-1]==target :
                Fm=Fm+Vadd
                dm+=1
            else:
                Fm=Fm+Vrem
                
            if Fm>FA:
                end=True
                return 'H1'
            elif Fm<FB:
                end=True
                return 'H0'
       
       
class MarkovDecisionProcess(MarkovModel):
    
    def __init__(self,states,actions):
        super().__init__(states)
        self.actions=actions
        
    def __str__(self):
        st=super().__str__()
        st+= '\n'
        for s in self.states:
            st += s.name + '->'
            for a,t in s.transitions.items():
                st += str(a) + ': '
                for k,v in t.items():
                    st += str(k)+ ' : ' +str(v) + '; '
            st+= '\n'
        return st   
    def simulate(self,steps,init=None,reward_mode=False,random_mode=False):
        init=self.states[0] if not init else init
        current=init
        history = []
        reward_final=0
        history.append(current.name)
        for i in range(steps):
            if random_mode:
                act_id=random.choice(range(len(current.actions)))
                act=current.actions[act_id]
                print(f"current choice {i} is {act}")
            else:
                print(current.actions)
                try:
                    act = input("please choose an action")
                except EOFError:
                    print("No input given")
                while act not in current.actions:
                    try:
                        act = input("invalid action, please choose again!")
                    except EOFError:
                        print("No input given")   
                      
            to_states=current.transitions[act]
            p=random.uniform(0,1)  
            pc=0 
            for key,ps in to_states.items():
                pc+=ps
                if p<pc:
                    current=key
                    break
            if reward_mode and i!=steps-1:
                reward_final+=current.reward
            history.append(current.name)
        if reward_mode:
            return history,reward_final
        else:
            return history
     
    def check_access(self,target):
        s2=[state for state in self.states if state.name!=target]
        s1=[state for state in self.states if state.name==target]
        nb_states=len(s2)
        print(nb_states)
        A=list()
        b=list()
        
        for i,state in enumerate(s2):
            nb_actions=len(list(state.transitions.keys()))
            M_current = [[0 for j in range(nb_states)] for i in range(nb_actions+2)]
            b_current = [ 0 for i in range(nb_actions+2)]
            b_current[nb_actions]=-1
            for j,act in enumerate(state.actions):
                for k in range(nb_states):
                    M_current[j][k]= - s2[i].transitions[act].get(s2[k],0)
                    if s2[k]==state:
                        M_current[j][k]+=1
            for t in s1:                
                b_current[j] += state.transitions[act].get(t,0)
                      
            for j in range(nb_states):
                if s2[j]==state:
                    M_current[nb_actions][j]=-1
                    M_current[nb_actions+1][j]=1    
            A.extend(M_current)
            b.extend(b_current)
        print(A)
        print(b)  
        A=np.array(A)
        b=np.array(b)
        
        c=np.ones((nb_states,1))
        A_ub=-A
        b_ub=-b
        
        res=scipy.optimize.linprog(c,A_ub,b_ub)
        print(res)            
        return res
                            
    def reward_expected(self,target):
        #不会
        pass
    
    def iter_val(self,gamma,error):
        nb_states=len(self.states)
        V= dict.fromkeys([s.name for s in self.states],0)
        V_next = dict.fromkeys([s.name for s in self.states],0)
        G = dict.fromkeys([s.name for s in self.states],0)
        nb_iter=0
        end=False
        while not end:
            for i,s in enumerate(self.states):
                max = float('-inf')
                V_current = s.reward
                for act,t in s.transitions.items():
                    for st,prob in t.items():
                        V_current += gamma*prob*V[st.name]
                        if V_current > max:
                            max = V_current
                V_next[s.name]=max
            
            V_vector=np.array(list(V.values()))  
            V_next_vector=np.array(list(V_next.values()))
            diff=np.linalg.norm(V_next_vector-V_vector)
            if diff<error:
                end=True
            V=V_next
          
        for i,s in enumerate(self.states):
            max = float('-inf')
            act_max = s.actions[0]
            V_current = s.reward
            for act,t in s.transitions.items():
                for st,prob in t.items():
                    V_current += gamma*prob*V[st.name]
                    if V_current > max:
                        max = V_current
                        act_max = act
                
            G[s.name]=act_max
        
        return V,G
    
    def chooseState(self,state):
        
        if list(state.transitions[state.actions[0]].values())[0] == 1 :
            return self.states[0]
        else: 
            return state

    def chooseAction(self,state,Q,sigma):
        p = random.uniform(0,1)
        if p < sigma:
            return random.choice(state.actions)
        else:
            values = Q[state.name] 
            act_max = None
            max = float('-inf')
            
            for act,value in values.items():
                if value > max :
                    act_max = act
                    max = value
            return act_max
        
    def simulate_qlearning(self,state_t,action_t):
        p = random.uniform(0,1)
        pc = 0
        for s,ps in state_t.transitions[action_t].items():
            pc += ps
            if p < pc:
                return s,state_t.reward
             
    def q_learning(self,gamma,sigma,nb_iters):
        #initialize  Q,alpha
        Q = dict()
        alpha = dict()
        strategy = dict()
        state_t = self.states[0]
        for s in self.states:
            Q[s.name] = dict.fromkeys(s.actions,0)
            alpha[s]=dict.fromkeys(s.actions,0)
            
        for i in range(nb_iters):
            state_t = self.chooseState(state_t)
            action_t = self.chooseAction(state_t,Q,sigma)
            state_t1,reward = self.simulate_qlearning(state_t,action_t)
            alpha[state_t][action_t]+=1
            
            Qmax = float('-inf')
            act_max = state_t1.actions[0]
            for act,val in Q[state_t1.name].items():
                if val>Qmax:
                    Qmax = val
                    act_max = act
                    
            delta=reward+gamma*Qmax-Q[state_t.name][action_t]
            Q[state_t.name][action_t]+=1/alpha[state_t][action_t]*delta   
            state_t=state_t1
        
        for s in self.states:    
            Qmax = float('-inf')
            act_max = s.actions[0]
            for act,val in Q[state_t1.name].items():
                if val>Qmax:
                    Qmax = val
                    act_max = act
            strategy[s.name]=act
        
        return Q,strategy
        
def main():
    while True:
        
        filename = input('please enter a filename')
        mode = input('please enter a mode for model: mc or mdp?')
        
        lexer = gramLexer(FileStream(filename))
        stream = CommonTokenStream(lexer)
        parser = gramParser(stream)
        tree = parser.program()
        walker = ParseTreeWalker()
        
        model_listener =gramModelListener(mode=mode)
        walker.walk(model_listener, tree)
        
        if mode == 'mc':
            model = model_listener.get_mc()
            print(model)
            while True:
                option=input('simulate, check_access, reward_expected, SMC_mc, SMC_sprt,exit')
                if option == 'simulate':
                    reward_mode = False
                    if reward_mode:
                        history,reward=model.simulate(steps=10,reward_mode=reward_mode)
                        print(history)
                        print(reward)
                    else:
                        history=model.simulate(steps=10,reward_mode=reward_mode)
                        print(history)
                        
                elif option == 'check_access':
                    results=model.check_access(target='F',steps=None)
                    print(results)
                    
                elif option == 'reward_expected':
                    results=model.reward_expected(target='F')
                    print(results)
                    
                elif option == 'SMC_mc' :
                    res_proba=model.SMC_quantitatif_mc(steps=5,target='S1',precision=0.01,error=0.05)
                    print(res_proba)
                    
                elif option == 'SMC_sprt' :
                    H=model.SMC_qualitatif_sprt(steps=5,target='S1',theta=0.2,epislon=0.01,alpha=0.01,beta=0.01)
                    print(H)
                elif option == 'exit':
                    break
                
            #model-checking accessibility of mc
            target='W'
            model.check_access(target)
            
        elif mode=='mdp':
            model = model_listener.get_mdp()
            print(model)
            while True:
                option=input('simulate, check_access, iter_val,q_learning')
                if option == 'simulate':
                    model.simulate(steps=10,reward_mode=False,random_mode=True)
                elif option == 'check_access':
                    model.check_access(target='T2')
                elif option == 'iter_val' :
                    V,G=model.iter_val(gamma=0.5,error=1)
                    print(V)
                    print(G)
                    
                elif option == 'q_learning' :
                    Q,strategy=model.q_learning(gamma=0.5,sigma=0.1,nb_iters=1000)
                    print(Q)
                    print(strategy)
                    
                elif option == 'exit':
                    break

if __name__ == '__main__':
    main() 