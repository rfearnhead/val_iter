{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "97a8c176-6bd6-4e18-a7dd-6c6346f0d585",
   "metadata": {},
   "source": [
    "# val_iter"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7322e828-68bc-4342-9d14-40dd7d56ae80",
   "metadata": {},
   "source": [
    "val_iter is a python package that can be used to perform the value iteration algorithm in order to determine the optimal policy for a decision process modelled as a Markov Decision Process."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b06cb212-9d7b-4ac7-b545-39756f0b40c7",
   "metadata": {},
   "source": [
    "## Installing the package"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4664c27f-ec71-46f1-b575-2624f9b41cd7",
   "metadata": {},
   "source": [
    "This package can be installed in Python from github using:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cd7b9816-47d9-47e1-a26f-b527189d72ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting git+https://github.com/rfearnhead/val_iter\n",
      "  Cloning https://github.com/rfearnhead/val_iter to c:\\users\\fearnhe1\\appdata\\local\\temp\\pip-req-build-d632ebxw\n",
      "  Resolved https://github.com/rfearnhead/val_iter to commit faeb164dcbd37626da6244702e69ae18adf3258f\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "  Preparing metadata (pyproject.toml): started\n",
      "  Preparing metadata (pyproject.toml): finished with status 'done'\n",
      "Requirement already satisfied: numpy in c:\\users\\fearnhe1\\stor-601\\env\\lib\\site-packages (from val_iter-python==1.0.0) (2.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  Running command git clone --filter=blob:none --quiet https://github.com/rfearnhead/val_iter 'C:\\Users\\fearnhe1\\AppData\\Local\\Temp\\pip-req-build-d632ebxw'\n",
      "\n",
      "[notice] A new release of pip is available: 24.2 -> 25.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!python -m pip install git+https://github.com/rfearnhead/val_iter"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7f3e223-1fb8-4a3c-a769-932c082d5ed2",
   "metadata": {},
   "source": [
    "## A simple Example"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac9cf952-a25f-4f7a-bbab-44bc7c8f567b",
   "metadata": {},
   "source": [
    "We can use example 9.27 in section 9.5 of *Artificial Intelligence: Foundations and Computational Agents 2nd edition* (https://artint.info/2e/html2e/ArtInt2e.html) to see how to use this package"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d36cba7d-a6e1-4eb3-989e-52c59f89e1be",
   "metadata": {},
   "source": [
    "First we can import val_iter and numpy, and then we need to define the four variables that are inputs to the function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4715f09a-b835-4891-ab84-544ae8f58900",
   "metadata": {},
   "outputs": [],
   "source": [
    "import val_iter\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "873e67d5-d93a-4d06-a989-70bcc612aaaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "P = [[[0.95, 0.7 ],\n",
    "        [0.5 , 0.1 ]],\n",
    "       [[0.05, 0.3 ],\n",
    "        [0.5 , 0.9 ]]]  \n",
    "R = [[ 7, 10],\n",
    "       [ 0,  2]]\n",
    "S = ['h','i']\n",
    "A = ['r','p']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9823eff0-fc97-4ec0-94a6-fb8b51bd18d2",
   "metadata": {},
   "source": [
    "P specifies the dynamics of the MDP and represents the probabilities of moving to a new state $s'$, given that you are currently in state $s$ and then perform an action $a$. The input can be given as a multi-dimensional list, or a numpy array. The values should be given so the probability of moving to a state, given the action performed and the current state is located at $P[s',s,a]$.\n",
    "\n",
    "R represents the expected reward from performing action $a$ in state $s$ and can also be given as a multi-dimensional list, or a numpy array. The values should be given so that the expected reward gained from action $a$ in state $s$ is located at $R[s,a].$\n",
    "\n",
    "S is a list that represents each of the states that can be visited.\n",
    "\n",
    "A is a list that represents each of the actions that can be performed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6fd1d55b-633b-4000-a848-7dbdd9ce0f9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(['p', 'r'], [35.71428571428571, 23.80952380952381])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "val_iter.val_iter(S,A,P,R)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71332c2f-d6bc-40a7-9972-64324d073bb0",
   "metadata": {},
   "source": [
    "Calling the val_iter function with these inputs returns a list containing the optimal policy - which action should be performed in each state, given in the order that the states were provided in the input - and the value function for each of the optimal actions.\n",
    "\n",
    "This solution shows that the optimal policy is to party when the person is feeling healthy (first state), and rest when they are feeling ill."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8e088e8-3440-4ca6-affd-91a5c085af88",
   "metadata": {},
   "source": [
    "## Second Example"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae833553-7614-41cf-a8e0-4449b76ccbfd",
   "metadata": {},
   "source": [
    "There are two other inputs that can be given for the function. We can look at them using a second example.\n",
    "\n",
    "Imagine that you have a 2x2 grid where each square has a reward for being in it. Each turn you have a choice to either move to the square horizontally adjacent to the one you are in, or move to the square vertically adjacent. If you choose to move horizontally, there is a 0.8 chance you successfully move horizontally, and a 0.2 chance of instead moving vertically. On the other hand, if you choose to move vertically, there is a 0.9 chance you move vertically and a 0.1 chance you instead move horizontally.\n",
    "\n",
    "\n",
    "The squares are positioned like this:\n",
    "| | |\n",
    "|---|---|\n",
    "| A | B |\n",
    "| C | D |\n",
    "\n",
    "\n",
    "And the rewards for entering each square are:\n",
    "| | |\n",
    "|---|---|\n",
    "| 5 | 1 |\n",
    "| 0 | 2 |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b35e611-194b-41b3-a56c-14c5f6dc70db",
   "metadata": {},
   "source": [
    "We can set up the inputs for $S,A,P,R$ with:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7f70d08c-7e6c-4ea3-8c92-e9872e7ee1e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "S = ['A','B','C','D']\n",
    "A = ['H','V']\n",
    "P = [[[0,0],\n",
    "      [0.8,0.1],\n",
    "      [0.2,0.9],\n",
    "      [0,0]],\n",
    "     [[0.8,0.1],\n",
    "      [0,0],\n",
    "      [0,0],\n",
    "      [0.2,0.9]],\n",
    "     [[0.2,0.9],\n",
    "      [0,0],\n",
    "      [0,0],\n",
    "      [0.8,0.1]],\n",
    "     [[0,0],\n",
    "      [0.2,0.9],\n",
    "      [0.8,0.1],\n",
    "      [0,0]]]        \n",
    "\n",
    "R = [[0.8,0.1],[4.4,2.3],[2.6,4.7],[0.2,0.9]]   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ac74216-b02b-46a0-a610-35d9f2d0e080",
   "metadata": {},
   "source": [
    "There are two other possible parameters for the input that we can define.\n",
    "\n",
    "iters represents the number of iterations that the value iteration algorithm performs. It usually takes the value of 1000, but can be specified by the user as any positive integer.\n",
    "\n",
    "gamma represents the discount factor for the value iteration. It usually takes the value of 0.8, however can be specified by the user as a real number between 0 and 1. This represents how much futer rewards are worth comapred to current rewards. If gamma is 0, then all future rewards are ignores, and if gamma is 1, then the value functions given would be the same as the total reward\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e4939cf-6ae6-4e92-a686-92fc3ec097b6",
   "metadata": {},
   "source": [
    "In this second example, we can run it with 500 iterations, and a discount factor, gamma, of 0.7:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2e981350-fb91-40bd-ad0f-3766697cff29",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(['H', 'H', 'V', 'V'],\n",
       " [7.703925706550331, 9.803862455443436, 10.098305225014334, 7.783314712680369])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "val_iter.val_iter(S,A,P,R, iters=500, gamma=0.7)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4addad1c-fe92-4022-83a4-20ee42e41ca4",
   "metadata": {},
   "source": [
    "This solution shows that if you are in either of the top squares (A or B), you want to choose to move horizontally, and if you are in squares C or D you want to move vertically."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
