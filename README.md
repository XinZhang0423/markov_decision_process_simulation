<!-- English Version -->

# Markov Decision Process (MDP) Simulation

This repository contains a Python simulation of Markov Decision Process (MDP) using Antlr4, Matplotlib and NetworkX. The simulation allows users to model, solve and visualize various MDP problems.

# Requirements
Python 3.x
Antlr4
Matplotlib
NetworkX

# Installation
```bash
git clone https://github.com/<your-username>/mdp-simulation.git


```

Install the required packages using pip:

```
pip install -r requirements.txt
```

Finally, you can run the simulation using the following command:

```
python3 mdp.py<ex.mdp
```



# Input
The input for the simulation is a file written in antlr4 syntax. The file should define the states, actions, rewards, and transitions of the MDP. An example input file is provided in the examples directory ex.mdp.

# Output
The simulation will generate a graphical representation of the MDP using networkx and matplotlib. It will also display the results of the selected algorithm, including the optimal policy and the value function for each state.

# Algorithms
The simulation currently supports the following algorithms for solving MDPs:
Value Iteration
Policy Iteration
Q-Learning

# Contributing
If you would like to contribute to this repository, please fork the project and submit a pull request. All contributions, big or small, are welcome!

<!-- Chinese Version -->
# 马尔可夫决策过程模拟

本仓库包含了一个使用antlr4，matplotlib和networkx的马尔可夫决策过程（MDP）模拟。该模拟允许用户可视化和分析MDP模型以及可用于解决它们的各种算法的结果。

## 要求

- antlr4
- matplotlib
- networkx
- Python 3.x

## 用法

要运行模拟，请先克隆仓库并导航到项目目录：

```
git clone https://github.com/[username]/markov-decision-process-simulation.git
cd markov-decision-process-simulation
```

然后使用pip安装所需的软件包：

```
pip install -r requirements.txt
```

最后，您可以使用以下命令运行模拟：

```
python3 mdp.py<ex.mdp
```

## 输入

模拟的输入是使用antlr4语法编写的文件。该文件应定义MDP的状态，动作，奖励和转换。示例目录中提供了一个输入文件示例。

## 输出

模拟将使用networkx和matplotlib生成MDP的图形表示。它还将显示选定算法的结果，包括最优策略和每个状态的价值函数。

## 算法

该模拟目前支持以下用于解决MDP的算法：

- 值迭代
- 策略迭代
- Q学习

## 贡献

如果您想为此仓库做出贡献，请fork项