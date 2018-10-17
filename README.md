## Project Details

For this project, a slightly modified version of the Unity "Banana Collectors" environment was used. The goal of this environment is to collect as many yellow bananas as possible. +1 point is awarded for each yellow banana collected. -1 points are awarded for each purple banana collected. The state space is defined by a 37d vector, where 36 of the values represent rays showing what is in front of the agent, and 1 value represents the speed of the agent. There are 4 actions the agent can take: left, right, forwards, or backwards. The environment is considered "solved" when an average score of 13 can be achieved over the last 100 episodes.

## Getting Started

#### Python Environment Setup
In order to ensure that your environment has all the necessary dependencies, follow the steps [here](https://github.com/udacity/deep-reinforcement-learning#dependencies)

#### Download the Environment

Next, you will need to download the environment used for this exercise.

* Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
* Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
* Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
* Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Unzip the file and take note of the unzipped path.

## Instructions

Run through cells in Banana.ipynb to train an agent. Parameters regarding the agent can be found in `agent.py`, while the model architecture can be found in `model.py`.