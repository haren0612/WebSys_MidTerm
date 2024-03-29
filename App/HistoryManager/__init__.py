import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename='operations_history.csv', directory='data'):
        self.directory = directory
        self.filename = filename
        self.filepath = os.path.join(self.directory, self.filename)
        
        # Ensure the directory exists
        os.makedirs(self.directory, exist_ok=True)

        if os.path.exists(self.filepath):
            # Load existing history from the file
            self.history_df = pd.read_csv(self.filepath)
        else:
            # Initialize an empty DataFrame if the file does not exist
            self.history_df = pd.DataFrame(columns=['Operation', 'Operands', 'Result'])

    def add_entry(self, operation, operands, result):
        new_entry = pd.DataFrame([[operation, operands, result]],
                                 columns=self.history_df.columns)
        # Prepare for concatenation by ensuring no all-NA columns; this step may vary based on your needs
        new_entry.dropna(axis=1, how='all', inplace=True)
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True).dropna(axis=1, how='all')
        self.save_history()

    def save_history(self):
        self.history_df.to_csv(self.filepath, index=False)

    def print_history(self):
        print(self.history_df)