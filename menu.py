from analysis.publications_trends import TopPublicationTrendsAnalysis 
from analysis.top_authors import TopAuthorsAnalysis
from analysis.language_distribution import LanguageDistributionAnalysis
from analysis.author_publication import AuthorPublicationAnalysis
from analysis.missing_isbn_analysis import MissingISBNAnalysis
from analysis.per_year_language_publication import PerYearLanguagePublicationAnalysis

class Menu:
    """
    Displays menu and triggers selected analysis.
    Demonstrates Strategy Pattern.
    """

    def __init__(self, df):
        # Store cleaned dataset
        self.df = df

    def display(self):
        while True:
            print("\n===== Dream Book Shop Analysis Menu =====")
            print("1. Publication Trends Over Time ")
            print("2. Top 5 Most Prolific Authors ")
            print("3. Language Distribution of books")
            print("4. Number of books published by each publisher")
            print("5. Missing ISBN Analysis")
            print("6. Number of books published per year categorized by language")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                TopPublicationTrendsAnalysis(self.df).run_analysis()
            elif choice == "2":
                TopAuthorsAnalysis(self.df).run_analysis()
            elif choice == "3":
                LanguageDistributionAnalysis(self.df).run_analysis()
            elif choice == "4":
                AuthorPublicationAnalysis(self.df).run_analysis()
            elif choice == "5":
                MissingISBNAnalysis(self.df).run_analysis()
            elif choice == "6":
                PerYearLanguagePublicationAnalysis(self.df).run_analysis()
            elif choice == "0":
                print("Thank you! Program EXITING.")
                break
            else:
                print("Invalid choice. Please try again.")

















     