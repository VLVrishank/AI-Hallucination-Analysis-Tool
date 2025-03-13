import pandas as pd
from datetime import datetime
import os
from typing import List, Dict

class DataManager:
    def __init__(self, storage_path: str = 'responses_data.csv'):
        self.storage_path = storage_path

    def save_responses(self, question: str, responses: List[str], 
                      consistency_score: float, entities: List[Dict]):
        data = {
            'timestamp': datetime.now(),
            'question': question,
            'responses': responses,
            'consistency_score': consistency_score,
            'entities': entities
        }
        df = pd.DataFrame([data])
        
        if os.path.exists(self.storage_path):
            df.to_csv(self.storage_path, mode='a', header=False, index=False)
        else:
            df.to_csv(self.storage_path, index=False)

    def load_responses(self) -> pd.DataFrame:
        if os.path.exists(self.storage_path):
            return pd.read_csv(self.storage_path)
        return pd.DataFrame()
