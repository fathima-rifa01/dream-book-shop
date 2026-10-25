print("data loader file runs")
import pandas as pd

class DataLoader:
    """
    Responsible ONLY for loading data from a CSV file.
    This follows the Single Responsibility Principle (SRP).
    """

    def __init__(self, file_path: str):
        # Store the file path of the dataset
        self.file_path = file_path

    def load_data(self):
        # Read the CSV file and return a DataFrame
        return pd.read_csv(self.file_path)
