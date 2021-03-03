import torch
from torch import nn

class Network(nn.Module):
    def __init__(self):
        super().__init__()

        # Layers & activations
        self.fc_in = nn.Linear(300, 2048)
        self.fc1 = nn.Linear(2048, 2048)
        self.fc_out = nn.Linear(2048, 10)
        self.activation_hidden = nn.RReLU()
        self.activation_output = nn.Sigmoid()
        self.drop_out = nn.Dropout(p=0.2)

        # Init weights
        nn.init.xavier_uniform_(self.fc_in.weight)
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc_out.weight)

    def forward(self, inputs, labels=None):

        # Input Layer
        x = self.fc_in(inputs)
        x = self.activation_hidden(x)

        # Layer 1
        x = self.drop_out(x)
        x = self.fc1(x)
        x = self.activation_hidden(x)

        # Output Layer
        x = self.drop_out(x)
        x = self.fc_out(x)
        preds = self.activation_output(x)

        # Return
        if labels is not None:
            loss = self.loss_function(preds, labels)
            return preds, torch.mean(loss)
        return preds
