print("data cleaner file runs")
class DataCleaner:
    """
    Handles all data cleaning operations.
    Keeps preprocessing separate from analysis logic.
    """

    def clean_data(self, df):
        # Remove duplicate records
        df = df.drop_duplicates()

        # Remove rows with missing values
        df = df.dropna()

        return df












