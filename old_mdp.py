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
# import pygraphviz as pgv 这两个库都👎
# import networkx as nx
# import pydot 
# from IPython.display import Image, display
# import io
# import matplotlib.image as mpimg 

#👇专门用来画有向图的
import networkx as nx
from matplotlib.animation import FuncAnimation

#老师给的listener例子，改写用于将文件中的马尔可夫模型储存起来    
class gramPrintListener(gramListener):
    #简单理解就是有四个方法，每个方法会读取对应的状态，决策和转移方程
    def __init__(self):
        pass
     
    def enterStaterew(self, ctx):
        print("States :%s, " % str([str(x) for x in ctx.ID()]))
        print("Rewards :%s, " % str([str(x) for x in ctx.INT()]))
        
    def enterStatenorew(self, ctx):
        print("States :%s, " % str([str(x) for x in ctx.ID()]))
       

    def enterDefactions(self, ctx):
        print("Actions: %s" % str([str(x) for x in ctx.ID()]))

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with action "+ act + " and targets " + str(ids) + " with weights " + str(weights))
        
    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with no action and targets " + str(ids) + " with weights " + str(weights))

#老师给的main函数，类似一个黑箱子，不知道什么原理🤷，只需要仿写，把其中一行替换一下
def main_print():
    lexer = gramLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    printer = gramPrintListener() #只需要这一行替换成自己写的类
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

#仿写老师给的gramPrintListener例子
class gramMDPListener(gramListener):
    """
    1. 状态组成的列表
    2. 决策组成的列表
    """
    def __init__(self):
        self.states = []
        self.actions = []
    
    #带reward的版本：    
    def enterStaterew(self, ctx):
        #把对应的reward存到state里
        self.states = [State(str(x),i) for i,x in enumerate(ctx.ID())]
        rewards=[int(str(x)) for x in ctx.INT()]
        print(rewards)
        for i,s in enumerate(self.states):
            s.rew=rewards[i]
    #不带reward的版本：    
    def enterStatenorew(self, ctx):
        #先把状态都初始化出来，默认identity是按顺序的
        self.states = [State(str(x),i) for i,x in enumerate(ctx.ID())]
    
    def enterDefactions(self, ctx):
        self.actions = [str(x) for x in ctx.ID()]
        
    def enterTransact(self, ctx):
        #读一行把转移方程读进来
        ids = [str(x) for x in ctx.ID()]
        #from_state 
        dep = ids.pop(0)
        #decision
        act = ids.pop(0)
        
        #所有的weights按顺序
        weights = [int(str(x)) for x in ctx.INT()]
        #剩下所有的to_state按顺序
        targets = ids
        total_weights=sum(weights)
        flag=False
        # 找到当前的name存成一个state
        for state in self.states:
            if state.name==dep:
                current_state = state
                flag=True
                break
            
        if not flag : print(f"{dep} is not defined in States")       
        current_state.actions.append(act)
                
        for i,target in enumerate(targets):
            proba=weights[i]/total_weights
            flag_target=False 
            for state in self.states:
                if state.name==target:
                    current_target = state
                    current_target.parents[current_state]=proba
                    flag_target=True
                    break
            if not flag_target: print(f"{target} is not defined in States")
            if i==0:
                t_i=Transition(current_state, act)
            t_i.add_tostate(current_target)
            t_i.add_proba(proba)
        current_state.add_transition(t_i)

                    
    def enterTransnoact(self, ctx):
        #读一行把转移方程读进来
        ids = [str(x) for x in ctx.ID()]
        #from_state 
        dep = ids.pop(0)
        #所有的weights按顺序
        weights = [int(str(x)) for x in ctx.INT()]
        #剩下所有的to_state按顺序
        targets = ids
        total_weights=sum(weights)
        flag=False
        # 找到当前的name存成一个state
        for state in self.states:
            if state.name==dep:
                current_state = state
                flag=True
                break
            
        if not flag : print(f"{dep} is not defined in States")  

        for i,target in enumerate(targets):
            proba=weights[i]/total_weights
            flag_target=False 
            for state in self.states:
                if state.name==target:
                    current_target = state
                    current_target.parents[current_state]=proba
                    flag_target=True
                    break
            if not flag_target: print(f"{target} is not defined in States")
            if not i:
                t_i=Transition(current_state, None)
            t_i.add_tostate(current_target)
            t_i.add_proba(proba)
        current_state.add_transition(t_i)

    def get_mdp(self):
        return MarkovDecisionProcess(self.states, self.actions)

class State():
    """
    创建一个State类，用于存
    1. 状态名字,号码 name，identity
    2. 每个状态拥有的actions的列表，用于检查模型错误
    3. 每个状态拥有的reward，一个数（可以为none，意思是不考虑reward的模型），可以理解为从这个状态出来获得的奖励
    4. 每个状态拥有的转移transtion的列表 类
    """
    
    def __init__(self,name,identity,reward=None):
        self.name=name
        self.id=identity
        self.to_states=[]
        self.rew=reward
        self.actions=[]
        self.transitions=[]
        self.parents=dict()
    
    def __str__(self):
        return self.name
    
    #下面两个方法用于在listener中调用，存储对应的action和transition   
    def add_transition(self,transition):
        self.transitions.append(transition)
    
    def add_action(self,action):
        self.actions.append(action)
       
    def __copy__(self):
        #todo:
        pass     
class Transition():
    """
        定义一个transition
        起始+[决策]+终止+proba
    """
    def __init__(self, from_state, action):
        self.from_state = from_state
        self.action = action
        self.to_states =[]
        self.probas = []    
    
    def add_tostate(self,state):
        self.to_states.append(state)
    
    def add_proba(self,proba):
        self.probas.append(proba)
      
    def cumsum_probas(self):
        return list(accumulate(self.probas))
   

        
class MarkovDecisionProcess():
    """
        一个mdp有状态列表组成，每个状态中存储对应的转移矩阵
    """
    #基本思路如下：
    """
    模拟了一个Markov Decision Process（MDP）模型的运行。MDP 是一种决策过程的抽象模型，表示了一个随机的决策系统，在它的状态空间和行动空间内不断地进行决策。
    函数simulate的参数：

    times：模拟的步数。
    random_mode：是否是随机选择决策的模式，如果是随机的话，为True；反之，为False。
    init：初始状态，如果不指定，则使用MDP模型中的初始状态。
    reward_mode:如果使用reward_mode则会返回最后积累的reward的和
    
    函数的执行过程：

    创建一个列表history来存储每一步状态的名字。
    确定初始状态，如果没有给定init，则使用MDP模型中的初始状态，否则使用给定的init。
    循环执行times步：
    将当前状态的名字存入history。
    判断当前状态是否有决策可以选择，如果没有决策，则随机选择一个可能的下一个状态。
    如果有决策可以选择，则根据random_mode的值选择决策方式：
    如果是随机选择决策，则随机选择一个决策，并根据该决策选择一个可能的下一个状态。
    如果是人为选择决策，则要求用户选择    
    """
    def __init__(self, states, actions):
        self.states = states
        self.actions = actions
        self.init=states[0]
    
    def __str__(self):
        return str([s.name for s in self.states])
        
    def check(self):
        """
        验证model的合法性，同时返回模型是mc还是mdp，方便后面的计算
        """
        for state in self.states:
            if state.actions and (len(state.actions)!=len(state.transitions)):
                    print(f"error! {state.name} has a not-welldefined transaction !")                
            for act in state.actions:
                if act not in self.actions:
                    print(f"warning! {state.name}'s {act} is not in defined global actions")

    def simulate(self,times,init=None,random_mode=True,reward_mode=False):
        """
        给定初始状态init，以及模拟次数，返回模拟历史（state的名字）
        """
        init=self.init if not init else init
        current=init
        history = []
        reward_final=0
        history.append(current.name)
        for i in range(times):
            #没有决策
            if not current.actions: t_act=current.transitions[0]
            else:
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
                    for i,ac in enumerate(current.actions):
                        if ac==act:
                            act_id=i
                t_act=current.transitions[act_id]     
            p=random.uniform(0,1)   
            to_states=t_act.to_states
            cum_probas=t_act.cumsum_probas()
            for i,pc in enumerate(cum_probas):
                if p<pc:
                    current=to_states[i]
                    break
            if reward_mode and i!=times-1:
                reward_final+=current.rew

            history.append(current.name)

        if reward_mode:
            return history,reward_final
        else:
            return history
    
    
    
    def reverse_dfs(self,root):
        """
        反向dfs，给定目标节点，做反向dfs，
        使用node_list作open_set
        使用acces_list作close_set
        使用sur_list作到达当前节点的概率为1的set
        """
        node_list=list()
        node_list.append(root)
        acces_list=dict()
        sur_list=list()
        while not node_list:
            current_node=node_list.pop()
            for parent in current_node.parents:
                if parent not in acces_list.keys():
                    node_list.append(parent)
                    acces_list[parent]=current_node.parents[parent]
                    
        pass
                            
    
    def check_access_mc(self,target_state,steps=None):
        """
        概率模型检测-马尔科夫链。要求给定一个目标状态，返回各个可以到达目标状态到达该状态的概率
        """
        S1=list()
        S0=list()
        Si=list()
        
        dfs_list=list()
        dfs_list.append(target_state)
        S1.append(target_state)
        current_state=target_state
        end=False
        while not end:
            for parent,proba in current_state.parents.items():
                if proba==1:
                    S1.append(parent)
                
        

        

    def check_access_mdp(self,):
        """
        概率模型检测-马尔科夫决策过程。使用minmax方法？还没明白怎么写
        """
        pass
    
    
    def modify_model(self,state):
        states=list()
        for s in self.states:
            s0=s #todo s.copy
            if s0.name==state:
                t=Transition(s0,None)
                t.add_tostate(s0)
                t.add_proba(1)
                s0.transitions=[t]
            states.append(s0)
        new_model=MarkovDecisionProcess(states,[])
        return new_model  
                
    def check_statistic_mc(self,steps,state,precision,taux_error):
        new_model=self.modify_model(state)
        times=math.ceil((math.log(2)-math.log(taux_error))/(2*precision)**2)
        res_times=0
        for i in range(times):
            res=new_model.simulate(steps)
            if res[-1]==state:
                res_times+=1
        res_proba=res_times/times
        return res_proba
            
    def check(self,steps,state,epislon,theta,alpha=0.01,beta=0.01):
        new_model=self.modify_model(state)
    
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
            if res[-1]==state :
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
      
    def iterations_values(self,gamma,epsilon):
        nb_states = len(self.states)
        Vn = dict()
        for state in self.states:
            Vn[state.name]=0
            
        Vn1 = Vn.copy()
        end = False
        nb_iter=0
        while not end:
            for state in self.states:
                V_max = float('-inf')
                V_current = state.rew
                for transition in self.transitions:
                    for i in range(len(transition.to_states)):
                        V_current+=  gamma * transition.probas[i]*Vn[transition.to_states[i]]
                    if V_current>V_max:
                        V_max=V_current
                Vn1[state]=V_max
                
            nb_iter+=1
            
            Vn_vector=np.array(list(Vn.values()))
            Vn1_vector=np.array(list(Vn1.values()))
            
            if np.linalg.norm(Vn1_vector-Vn_vector)<epsilon:
                end=True
            
            Vn=Vn1.copy()
            
        adversaire = dict() 
        for state in self.states:
            V_max = float('-inf')
            V_current = state.rew
            action=state.actions[0]
            for i,transition in self.transitions:
                for i in range(len(transition.to_states)):
                    V_current+=  gamma * transition.probas[i]*Vn[transition.to_states[i]]
                if V_current>V_max:
                    V_max=V_current
                    action=self.actions[i]
            adversaire[state]=action
            
        return Vn,adversaire
    
    def q_learning(self,gamma,epsilon):
        Q=initialize()
        state_t='S1'
        
        reverse_alpha=np.zeros((5,2))
        
        for i in range(nb_iters):
            
            #state_t=chooseState()
            action_t=chooseAction(Q,state_t,0.1)
            state_t1,reward=simulate(state_t,action_t)
            reverse_alpha[index(state_t),index(action_t)]+=1
            delta=reward+gamma*np.max(Q[index(state_t1),:])-Q[index(state_t),index(action_t)]
            Q[index(state_t),index(action_t)]+=1/reverse_alpha[index(state_t),index(action_t)]*delta   
            state_t=state_t1
        
        
        strategy=np.argmax(Q,axis=1)   
        return Q,strategy
    
            
        
class StateDiagram():
    
    """
        下面创建一个可视化的类,用于画图
    """
    def __init__(self, states, history):
        self.G = nx.DiGraph()
        self.states = states
        self.history=history
        self.fig,self.ax=plt.subplots()
        
    def load_node(self,frame):
        self.current=self.history[frame]
        for state in self.states:
            if state.name == self.current:
                self.G.add_node(state.name,label=state.name,color='#b41f2e')
            else:
                self.G.add_node(state.name,label=state.name,color='#1f78b4')
        return self.G
    
    def load_edge(self):
        for state in self.states:
            for transition in state.transitions:
            #将转移的to_states作为图的节点
                for j,to_state in enumerate(transition.to_states):
                    #在当前状态和to_states之间添加有向边
                    if transition.action:
                        self.G.add_edge(state.name,to_state.name,action=transition.action, proba=transition.probas[j])
                    else:
                        self.G.add_edge(state.name,to_state.name,action='', proba=transition.probas[j])
        
        return self.G

    #经过实验验证pydot这个库不好用，不过用来学图论倒是不错
    #我改成了使用pygraphviz库 
    #pygraphviz库也👎最后换成了networkx                                
    def draw(self):
        pos = nx.spring_layout(self.G,seed=6,scale=20,k=3/sqrt(self.G.order()))
        node_colors = [nx.get_node_attributes(self.G,'color')[node] for node in self.G.nodes]
        
        nx.draw_networkx_nodes(self.G, pos,node_color=node_colors,ax=self.ax)
        nx.draw_networkx_labels(self.G, pos,ax=self.ax)
        #如果一个边有往返，就画成弯的
        curved_edges = [edge for edge in self.G.edges() if reversed(edge) in self.G.edges()]
        #反之就画成直的
        straight_edges = list(set(self.G.edges()) - set(curved_edges))
        #画直边
        nx.draw_networkx_edges(self.G, pos, ax=self.ax,edgelist=straight_edges)
        #画曲边
        arc_rad = 0.25
        nx.draw_networkx_edges(self.G, pos,ax=self.ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
        #画直线和曲线上的labels
        #我服了，这样直接画会把label画在直线上，但是画不到曲线上！！所以有写了一个函数来计算label应该在的位置
        edge_action = nx.get_edge_attributes(self.G,'action')
        edge_proba = nx.get_edge_attributes(self.G,'proba')
        curved_edge_labels = {edge: edge_action[edge] + ' ' + str(round(edge_proba[edge],2)) for edge in curved_edges}
        straight_edge_labels = {edge: edge_action[edge] +' '+ str(round(edge_proba[edge],2)) for edge in straight_edges}
        nx.draw_networkx_edge_labels(self.G, pos,ax=self.ax,edge_labels=straight_edge_labels)
        self.my_draw_networkx_edge_labels(self.G, pos, ax=self.ax,edge_labels=curved_edge_labels,rotate=False,rad = arc_rad)
        plt.axis('off')
        return self.G

    def update(self,frame):
        self.G=nx.DiGraph()
        self.load_node(frame)
        self.load_edge()
        self.draw()
        return self.G
        
    #动画模拟animate
    def animate(self):
        ani = FuncAnimation(self.fig, self.update, frames=len(self.history), interval=100,repeat_delay=0.001)
        plt.show()
        ani.save('./ani.gif')

        
    @staticmethod
    def my_draw_networkx_edge_labels(G,pos,edge_labels=None,label_pos=0.5,font_size=10,font_color="k",
                                     font_family="sans-serif",font_weight="normal",alpha=None,bbox=None,
                                     horizontalalignment="center",verticalalignment="center",ax=None,rotate=True,clip_on=True,rad=0):
        import matplotlib.pyplot as plt
        import numpy as np
        if ax is None:
            ax = plt.gca()
        if edge_labels is None:
            labels = {(u, v): d for u, v, d in G.edges(data=True)}
        else:
            labels = edge_labels
        text_items = {}
        for (n1, n2), label in labels.items():
            (x1, y1) = pos[n1]
            (x2, y2) = pos[n2]
            pos_1 = ax.transData.transform(np.array(pos[n1]))
            pos_2 = ax.transData.transform(np.array(pos[n2]))
            linear_mid = 0.5*pos_1 + 0.5*pos_2
            d_pos = pos_2 - pos_1
            rotation_matrix = np.array([(0,1), (-1,0)])
            ctrl_1 = linear_mid + rad*rotation_matrix@d_pos
            ctrl_mid_1 = 0.5*pos_1 + 0.5*ctrl_1
            ctrl_mid_2 = 0.5*pos_2 + 0.5*ctrl_1
            bezier_mid = 0.5*ctrl_mid_1 + 0.5*ctrl_mid_2
            (x, y) = ax.transData.inverted().transform(bezier_mid)

            if rotate:
                # in degrees
                angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
                # make label orientation "right-side-up"
                if angle > 90:
                    angle -= 180
                if angle < -90:
                    angle += 180
                # transform data coordinate angle to screen coordinate angle
                xy = np.array((x, y))
                trans_angle = ax.transData.transform_angles(
                    np.array((angle,)), xy.reshape((1, 2))
                )[0]
            else:
                trans_angle = 0.0
            # use default box of white with white border
            if bbox is None:
                bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
            if not isinstance(label, str):
                label = str(label)  # this makes "1" and 1 labeled the same

            t = ax.text(
                x,
                y,
                label,
                size=font_size,
                color=font_color,
                family=font_family,
                weight=font_weight,
                alpha=alpha,
                horizontalalignment=horizontalalignment,
                verticalalignment=verticalalignment,
                rotation=trans_angle,
                transform=ax.transData,
                bbox=bbox,
                zorder=1,
                clip_on=clip_on,
            )
            text_items[(n1, n2)] = t

        ax.tick_params(
            axis="both",
            which="both",
            bottom=False,
            left=False,
            labelbottom=False,
            labelleft=False,
        )

        return text_items
   
def main_mdp():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",type=str)
    args = parser.parse_args()
    filename=args.filename #'ex.mdp'
    lexer = gramLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    mdp_listener = gramMDPListener()
    walker = ParseTreeWalker()
    walker.walk(mdp_listener, tree)
    mdp = mdp_listener.get_mdp()
    mdp.check()
    print(mdp.simulate_smc(5,'W',0.05,0.01))
    print(mdp.simulate_sprt(5,'W',0.01,0.16))
    # print(mdp)
    # history,reward=mdp.simulate(10,random_mode=False,reward_mode=True)
    # print(history,reward)
    
    #graphe=StateDiagram(mdp.states,history)
    # graphe.load_node(0)
    # graphe.load_edge()
    # graphe.draw()
    # plt.show()
    #graphe.animate()
    
if __name__ == '__main__':
    main_mdp()
    # main_print()






    


    
    