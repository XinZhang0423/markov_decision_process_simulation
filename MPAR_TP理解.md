# TP1 理解：

## 基本文件介绍：

- .mdp文件是一种Markov Decision Process模型定义文件，用于定义一个有限的状态空间和可能的状态转移。
- .g4文件是一种语法描述文件，用于定义语法规则，包括产生式、终结符、非终结符等。
- mdp.py 主文件，负责读取.mdp内容，存起来做模拟，以及各种算法。

- 其他杂的（.interp文件是一种中间代码文件，用于描述编译器或解释器如何解释规则，从而生成最终的代码。.tokens文件是一种词法单元文件，用于描述编译器或词法分析器对代码进行词法分析后得到的词法单元。词法单元是代码中最小的可识别单位，例如关键字、标识符、常量等。.tokens文件中每一行表示一个词法单元，每一行包含词法单元的名称、类型和值等信息。在语法分析阶段，编译器或语法分析器会使用.tokens文件中的信息对代码进行语法分析，从而生成最终的代码）

我的理解是：先创建词法分析器lexer，在根据词法分析器生成tokens词法单元流。接下来创建一个语法分析器，去分析刚才创建的词法单元流，生成语法树tree。最后使用walker去遍历这个树，取出其中的元素放到listener中

使用python做markov模拟，需要在**.mdp文件中定义模型**，在**.g4文件中定义语法**，具体步骤如下。

## 第一步：编写gram.g4语法规则文件：

语法规则文件基本编写方式：

```
grammar gram;

program
    : defstates defactions transitions EOF    
    ;

#上面这里定义program基本组成类型（即状态，动作，transitions和结尾EOF end of file）

defstates : staterew | statenorew;

#类似Haskell状态分成两种： 一种是带reward， 一种是不带reward
#然后分别定义带reward和不带reward都应该怎么写

statenorew : STATES ID  (',' ID )* ';';
staterew : STATES ID ':'  INT (',' ID ':' INT)* ';';

#动作也这么定义

defactions : ACTIONS ID (',' ID)* ';';

#注意如果一个东西写很多行，可以用以下的定义方式

transitions : trans (trans)* ;

trans : transact | transnoact;

transact : ID '[' ID ']' FLECHE INT ':' ID 
    ('+' INT ':' ID)* ';';
transnoact : ID FLECHE INT ':' ID 
    ('+' INT ':' ID)* ';'
;

#最后定义每一个东西叫什么，也就是 全大写是常量名：代表的字符

STATES : 'States';
ACTIONS : 'Actions' ;
TRANSITION : 'transition' ;
DPOINT : ':' ;
FLECHE : '->';
SEMI : ';' ;
VIRG : ',';
PLUS : '+';
LCROCH : '[' ;
RCROCH : ']' ;

# +代表最少有一个可以循环好几次，*代表最少有0个可以循环好几次
INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
```

## 第二步： 使用anltr4  编译语法文件生成对应的python代码：

在编写好了`gram.g4`语法文件后，要使用ANTLR 4生成Python代码，可以按照以下步骤进行：

1. 打开命令行终端进入包含`gram.g4`文件的目录。

2. 运行以下命令，生成Python代码：

   ```
   antlr4 -Dlanguage=Python3 gram.g4
   ```

   注意，这里假设使用的是Python 3，如果使用的是Python 2，命令应该是`antlr4 -Dlanguage=Python2 gram.g4`。

3. 如果一切顺利，ANTLR 4将生成`gramLexer.py`和`gramParser.py`等Python源文件，以及其他必要的文件（一堆看不懂的，不用管）。

## 第三步：如何调用其读写代码：



1. 在Python主代码中这里是mdp.py，使用`gramLexer`和`gramParser`类来解析输入的源代码。需要实例化这些类，并调用它们的方法来执行解析操作。具体来说，需要使用以下代码：

   ```python
   from antlr4 import *
   from gramLexer import gramLexer
   from gramParser import gramParser
   
   # 创建输入流
   input_stream = FileStream("input.txt")
   # 或者使用StdinStream() 读入控制台
   # 创建词法分析器
   lexer = gramLexer(input_stream)
   # 创建词法符号流
   token_stream = CommonTokenStream(lexer)
   # 创建语法分析器
   parser = gramParser(token_stream)
   # 调用语法分析器的入口规则
   tree = parser.program()
   
   ```
   
   这里假设输入源代码保存在名为`input.txt`的文件中，而入口规则名为`program`。您可以根据需要更改这些值。执行以上代码，将会得到一棵语法分析树，代表输入源代码的抽象语法树。

## 第四步：定义listener存储规则，使用walker遍历语法树

1. Listener 存储规则的一个例子：

```python
class gramPrintListener(gramListener):
    #简单理解就是有四个方法，每个方法会读取在gram.g4定义的program中的类型
    #ctx.ID()返回读取的类型为字符
    #ctx.INT()返回读取的类型为数字
    def __init__(self):
        pass
        
    def enterDefstates(self, ctx):
        print("States: %s" % str([str(x) for x in ctx.ID()]))

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

```

2. 使用walker读取语法树

```python
mdp_listener = gramMDPListener()
walker = ParseTreeWalker()
walker.walk(mdp_listener, tree)
```

3. 本案例中的:



## 本案例中Markov Decision Process的构造：

为了区分两种不同的存储方式，我在noaction的transition是用字典存储的，每个目标状态作为key对应一个概率proba，而在有action的，则是每个action作为key对应一个transition，每一个transition又是一个字典

分成两种类来存：

1. state_mc ： 

- to_states 字典 key： state， value：proba

2. state_mdp ：

- transitions ： 字典 key：action， value：to_states 类似上面的字典

都有parents，列表存它的parents



# 算法1 simulation 

## 要求： 

给定一个初始状态，和模拟次数，返回经过的状态组成的列表,可以返回reward值



# model-checking probabiliste

PCTL 概率计算树逻辑 DTMC/MDP 离散时间马尔科夫

# 算法2 Markov chain accessibility

要求：
给定一个目标状态，和步数，返回经过该步数到达该节点的概率的向量，以字典的形式返回：

key：state.name 

value： proba

方法：

- 简单使用dfs找到s0，s1，s2
- 根据s2构造A和b，进行迭代即可

使用ex12.mdp验证target改成f值和老师一样



# 算法3 markov decision process accessibility

使用线性规划求解可达性：

将其转化成新型规划问题，如下：

![截屏2023-03-21 14.03.30](/Users/zhangxin/Documents/%E6%88%AA%E5%B1%8F/typora/%E6%88%AA%E5%B1%8F2023-03-21%2014.03.30.png)

等价于一个最优化问题，最后返回以字典的形式返回：

key：state.name 

value： proba



方法：

- 简单使用dfs找到s0，s1，s2
- 根据s2构造A和b，然后最优化即可



使用ex13.mdp验证，结果不详

# 算法4 计算reward attendu

1. Mc

给定一个target，计算到达这个target获得reward的期望。

因为两个公式高度一致，因此只需要将A和b进行相应改动即可：

- A仍然是转移矩阵
- b变成了每个节点的reward即可



2. mdp





Continuous Stochastic Logic连续统计逻辑CTMC/PTA



SMC 

- Quantitatif
- Qualitatif

# 模型验证统计学方法

通过采样计算模型满足某个性质的概率。

四要素：

- 采样sample
- 概率probability
- 性质property
- 准确度precision



有两种类型的性质：

- 定性分析：直接求出满足相应性质的概率
- 定量分析：满足相应性质的概率大于某一个值的概率

使用simu-mc.mdp验证 0.15

# 算法5 smc quantitatif

- Données : Modèle *M*, propriété *ϕ*, précision *ε*, taux d’erreur *δ*

- But : Estimer la probabilité *γ* avec laquelle *M* satisfait *ϕ*

使用simu-mc.mdp验证 i=target k=steps theta=proba

Monte Carle算法，使用z随机变量用来记录一个réalisation，zi表示第i个réalistaion成功了

Bornes de Chernoff-Hoeffding CH边界定理告诉我们：

<img src="/Users/zhangxin/Documents/%E6%88%AA%E5%B1%8F/typora/%E6%88%AA%E5%B1%8F2023-03-21%2015.01.40.png" alt="截屏2023-03-21 15.01.40" style="zoom:50%;" />

在做过N次试验后，可以保证满足|YN-Y|误差大于epsilon的概率小于precision





# 算法6 Sequential Probability Ratio Test

Sequential Probability Ratio Test（序贯概率比检验）是一种用于假设检验的统计方法，它可以帮助我们在样本收集的过程中，根据当前的数据来逐步更新对某个假设的置信度，并决定是否接受或拒绝该假设。

该方法的核心思想是，通过计算在两个假设（H0和H1）下的条件概率比（likelihood ratio），来判断当前观测到的数据更有可能来自哪个假设。具体地说，我们定义两个概率比（likelihood ratio）：a = P(X|H1) / P(X|H0) 和 b = P(X|H0) / P(X|H1)，其中X表示观测到的数据。在一开始，我们设定一个初始的置信度，然后每次根据当前观测到的数据计算出a或b的值，并将其与一个事先设定的阈值进行比较。如果a或b的值超过了阈值，我们就可以得出结论，接受或拒绝某个假设；如果没有超过，我们则需要继续收集数据，以进一步提高置信度。

与传统的假设检验方法相比，Sequential Probability Ratio Test更加适用于需要连续收集数据的情形，因为它可以根据当前的数据情况，灵活地更新置信度，并在收集到足够的数据后做出最终决策。



# 算法7 动态规划 iteration valeur politique





# 算法8 q-learning





















