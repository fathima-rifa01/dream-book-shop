from data_loader import DataLoader
from data_cleaner import DataCleaner
from menu import Menu


def main():
    # Load dataset
    loader = DataLoader("data/dataset_books.csv")
    df = loader.load_data()

    # Clean dataset
    cleaner = DataCleaner()
    df = cleaner.clean_data(df)

    # Launch menu system
    menu = Menu(df)
    menu.display()

# Application entry point
if __name__ == "__main__":
    print("Running main.py")
    main()

