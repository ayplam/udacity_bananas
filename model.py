from torch import nn
import torch
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size=37, action_size=4, seed=0):
        """
        Initialize the layers in the model

        Args:
            state_size <int>        : Number of states
            action_size <int>       : Number of actions
            seed <int>              : seed
        """
        super(QNetwork, self).__init__()
        
        self.action_size = action_size
        self.state_size = state_size

        # Keep the fully connected layers pretty small
        fc1_units = 16
        fc2_units = 8
        
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)

        # Dueling DQN - two outputs
        # 1. advantage of taking an action
        self.adv = nn.Linear(fc2_units, action_size)

        # 2. the state value
        self.state = nn.Linear(fc2_units, 1)

    def forward(self, state):
        """Build a network that maps state -> action values."""

        fc1_out = F.relu(self.fc1(state))
        fc2_out = F.relu(self.fc2(fc1_out))
        
        # Advantage of taking an action
        x1 = self.adv(fc2_out)
        
        # State value function 
        x2 = self.state(fc2_out).expand(-1,self.action_size) 
        
        # Adv + state - avg(actions)
        out = x1 + x2 - torch.mean(x1, 1, True).expand(-1, self.action_size)
        
        return out
