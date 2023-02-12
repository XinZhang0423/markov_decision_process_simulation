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





