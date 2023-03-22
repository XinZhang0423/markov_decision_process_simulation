import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt

class StateDiagram():
    
    """
        下面创建一个可视化的类,用于画图
    """
    def __init__(self, states, history=None):
        self.G = nx.DiGraph()
        self.states = states
        self.history=history if history is not None else [states[0]]
        self.fig,self.ax=plt.subplots()
        
    def load_node(self,frame=0):
        self.current=self.history[frame]
        for state in self.states:
            if state.name == self.current:
                self.G.add_node(state.name,label=state.name,color='#b41f2e')
            else:
                self.G.add_node(state.name,label=state.name,color='#1f78b4')
        return self.G
    
    def load_edge(self):
        for state in self.states:
            for act,transition in state.transitions.items():
            #将转移的to_states作为图的节点
                for s,prob in transition.items():
                    #在当前状态和to_states之间添加有向边
                    if state.actions:
                        self.G.add_edge(state.name,s.name,action=act, proba=prob)
                    else:
                        self.G.add_edge(state.name,s.name,action='', proba=prob)
        
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
