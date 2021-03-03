from torch.utils.data import Dataset

class Dataset(Dataset):
    def __init__(self, partition):
        # dataset init method
        self.partition = partition
        
    def __len__(self):
        # logic to get lenght of dataset
        return

    def __getitem__(self):        
        # logic to get item
        return
