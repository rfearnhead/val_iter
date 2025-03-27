# val_iter

val_iter is a python package that can be used to perform the value iteration algorithm in order to determine the optimal policy for a decision process modelled as a Markov Decision Process.

## Installing the package

This package can be installed in Python from github using:


```python
!python -m pip install git+https://github.com/rfearnhead/val_iter
```

## A simple Example

We can use example 9.27 in section 9.5 of *Artificial Intelligence: Foundations and Computational Agents 2nd edition* (https://artint.info/2e/html2e/ArtInt2e.html) to see how to use this package

First we can import val_iter and numpy, and then we need to define the four variables that are inputs to the function.


```python
import val_iter
import numpy as np

```


```python
P = [[[0.95, 0.7 ],
        [0.5 , 0.1 ]],
       [[0.05, 0.3 ],
        [0.5 , 0.9 ]]]  
R = [[ 7, 10],
       [ 0,  2]]
S = ['h','i']
A = ['r','p']

```

P specifies the dynamics of the MDP and represents the probabilities of moving to a new state $s'$, given that you are currently in state $s$ and then perform an action $a$. The input can be given as a multi-dimensional list, or a numpy array. The values should be given so the probability of moving to a state, given the action performed and the current state is located at $P[s',s,a]$.

R represents the expected reward from performing action $a$ in state $s$ and can also be given as a multi-dimensional list, or a numpy array. The values should be given so that the expected reward gained from action $a$ in state $s$ is located at $R[s,a].$

S is a list that represents each of the states that can be visited.

A is a list that represents each of the actions that can be performed.


```python
val_iter.val_iter(S,A,P,R)
```




    (['p', 'r'], [35.71428571428571, 23.80952380952381])



Calling the val_iter function with these inputs returns a list containing the optimal policy - which action should be performed in each state, given in the order that the states were provided in the input - and the value function for each of the optimal actions.

This solution shows that the optimal policy is to party when the person is feeling healthy (first state), and rest when they are feeling ill.

## Second Example

There are two other inputs that can be given for the function. We can look at them using a second example.

Imagine that you have a 2x2 grid where each square has a reward for being in it. Each turn you have a choice to either move to the square horizontally adjacent to the one you are in, or move to the square vertically adjacent. If you choose to move horizontally, there is a 0.8 chance you successfully move horizontally, and a 0.2 chance of instead moving vertically. On the other hand, if you choose to move vertically, there is a 0.9 chance you move vertically and a 0.1 chance you instead move horizontally.


The squares are positioned like this:
| | |
|---|---|
| A | B |
| C | D |


And the rewards for entering each square are:
| | |
|---|---|
| 5 | 1 |
| 0 | 2 |


We can set up the inputs for $S,A,P,R$ with:


```python
S = ['A','B','C','D']
A = ['H','V']
P = [[[0,0],
      [0.8,0.1],
      [0.2,0.9],
      [0,0]],
     [[0.8,0.1],
      [0,0],
      [0,0],
      [0.2,0.9]],
     [[0.2,0.9],
      [0,0],
      [0,0],
      [0.8,0.1]],
     [[0,0],
      [0.2,0.9],
      [0.8,0.1],
      [0,0]]]        

R = [[0.8,0.1],[4.4,2.3],[2.6,4.7],[0.2,0.9]]   
```

There are two other possible parameters for the input that we can define.

iters represents the number of iterations that the value iteration algorithm performs. It usually takes the value of 1000, but can be specified by the user as any positive integer.

gamma represents the discount factor for the value iteration. It usually takes the value of 0.8, however can be specified by the user as a real number between 0 and 1. This represents how much futer rewards are worth comapred to current rewards. If gamma is 0, then all future rewards are ignores, and if gamma is 1, then the value functions given would be the same as the total reward



In this second example, we can run it with 500 iterations, and a discount factor, gamma, of 0.7:


```python
val_iter.val_iter(S,A,P,R, iters=500, gamma=0.7)
```




    (['H', 'H', 'V', 'V'],
     [7.703925706550331, 9.803862455443436, 10.098305225014334, 7.783314712680369])



This solution shows that if you are in either of the top squares (A or B), you want to choose to move horizontally, and if you are in squares C or D you want to move vertically.


```python

```


```python

```


```python

```


```python

```


```python

```
