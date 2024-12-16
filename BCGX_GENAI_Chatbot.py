import pandas as pd

# Load financial data reports
final_report = pd.read_csv('final_data_report.csv')
summary_report = pd.read_csv('Summary_final_report.csv')


def get_financial_data(query, company, year):
    """
    Retrieve financial data based on the user's query, company name, and fiscal year.

    Parameters:
    query (str): The financial query.
    company (str): The name of the company.
    year (int): The fiscal year.

    Returns:
    str: The response containing the requested financial information.
    """
    # Define a mapping of queries to the corresponding data retrieval logic
    data_mapping = {
        "What is the total revenue?": 'Total Revenue',
        "What is the Net Income?": 'Net Income',
        "What is the sum of total assets?": 'Total Assets',
        "What is the sum of total liabilities?": 'Total Liabilities',
        "What is cash flow from operating activities?": 'Cash Flow from Operating Activities',
        "What is the revenue growth(%) ?": 'Revenue Growth (%)',
        "What is the net income growth(%) ?": 'Net Income Growth (%)',
        "What is the assets growth(%) ?": 'Assets Growth (%)',
        "What is the liabilities growth(%) ?": 'Liabilities Growth (%)',
        "What is the cash flow from operations growth(%) ?": 'Cash Flow from Operations Growth(%)',
        "What is the year by year average revenue growth rate(%)?": 'Revenue Growth (%)',
        "What is the year by year average net income growth rate(%)?": 'Net Income Growth (%)',
        "What is the year by year average assets growth rate(%)?": 'Assets Growth (%)',
        "What is the year by year average liabilities growth rate(%)?": 'Liabilities Growth (%)',
        "What is the year by year average cash flow from operations growth rate(%)?": 'Cash Flow from Operations Growth(%)'
    }

    # Check if the query is valid
    if query in data_mapping:
        column_name = data_mapping[query]
        if "year by year average" in query:
            # For average growth rates, use the summary report
            result = summary_report[summary_report['Company'] == company][column_name].values[0].round(4)
        else:
            # For other queries, use the final report
            result = \
            final_report[(final_report['Year'] == year) & (final_report['Company'] == company)][column_name].values[0]
        return f"{query} for {company} for fiscal year {year} is $ {result}" if "growth" not in query else f"{query} for {company} from 2021 to 2023 is {result}(%)"
    else:
        return "Sorry, I can only provide information on the requested queries."


def main():
    """
    Main function to run the financial chatbot.
    """
    print("----------------------------------------------------------------------------")
    while True:
        user_input = input("\nEnter 'Hi' to start the chatbot session; type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print("Thank you for using the Financial Chatbot. Goodbye!")
            break
        elif user_input == "hi":
            print("\nHello! Welcome to the AI-Driven Financial Chatbot!")
            print("\nI can assist you with your financial queries.")
            print("Please select a company from the following options:")
            print("\n1. Microsoft \n2. Tesla \n3. Apple")
            company_input = input("Enter company name: ").strip().capitalize()

            if company_input not in ['Apple', 'Microsoft', 'Tesla']:
                print("Invalid Company Name. Please restart the chatbot session and enter a valid company name.")
                continue

            print("\nThe data for the fiscal years 2023, 2022, and 2021 is currently available.")
            fiscal_year = int(input("Enter the fiscal year for the selected company: "))
            if fiscal_year not in [2023, 2022, 2021]:
                print("Invalid fiscal year. Please restart the chatbot session and enter a valid fiscal year.")
                continue

            # Start the financial query session
            while True:
                print("\nPlease enter your financial query:")
                user_query = input().strip()
                response = get_financial_data(user_query, company_input, fiscal_year)
                print(response)
                if input("\nWould you like to ask another question? (yes/no): ").strip().lower() != 'yes':
                    break
        else:
            print("Please enter 'Hi' to start the chatbot session or 'exit' to quit.")


if __name__ == "__main__":
    main()
