from DEEP_Classifier.utils import read_yaml
from collections import namedtuple

DataIngestion=namedtuple('DataIngestion',['source','zip_dir','data_root'])

class ConfigManager:
    '''
    init takes config file path and params file path to returen configbox(dict)
    
    '''
    def __init__(self,config_path:str,params_path:str) -> DataIngestion:
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_path)
    
    

