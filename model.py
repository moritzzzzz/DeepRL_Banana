import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        
        
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        # Defining the layers, 256, 128, 64 units each
        self.fc1 = nn.Linear(state_size, 256) #Fully connected Layer: Linear(input_size,output_size)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 64)
        # Output layer, dimensions defined by action_size... in this case action_size = 4
        self.fc4 = nn.Linear(64, action_size)
        

    def forward(self, state):
        """Build a network that maps state -> action values."""
        ''' Forward pass through the network, returns the output logits '''
        
        x = self.fc1(state)#passing tensor through first layer
        x = F.relu(x)#acting activation function relu on the output of the first layer
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        
        #wir lassen softmax weg fuer das Training, um die floating point Ungenauigkeit nicht im training zu haben
        #Wenn das Modell trainiert ist, kann die softmax wieder drangehaengt werden
        
        #x = F.softmax(x, dim=1) #do softmax over dimension 1, which is 10 (batch size dimension is dim=0)
        
        return x#return result after passing through network
