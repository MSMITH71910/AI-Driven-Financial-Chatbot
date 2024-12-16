# AI-Driven-Financial-Chatbot Project 
### This is a BCG GenAI Job Simulation on Forage

Welcome to the AI-Driven Financial Chatbot, an intelligent assistant designed to simplify the process of retrieving and analyzing financial data for major companies. This chatbot leverages Python and pandas to provide accurate and concise financial insights, including revenue, net income, asset growth, and more for companies like Apple, Microsoft, and Tesla.

## Features

### This chatbot is built to:

- Answer financial queries about total revenue, net income, total assets, liabilities, and cash flow.
- Provide year-over-year growth percentages for key financial metrics.
- Calculate average growth rates for financial data spanning multiple years.
- Allow users to select a company and fiscal year to tailor their queries.
- Deliver concise and formatted responses to assist in financial decision-making.

## How It Works

### The chatbot operates through a conversational interface where users can:

 1. **Start a session:** Enter "Hi" to initiate the chatbot.
 2. **Select a company:** Choose from a predefined list of companies — Apple, Microsoft, or Tesla.
 3. **Pick a fiscal year:** Select a year (2021, 2022, or 2023) for which data is available.
 4. **Ask financial questions:** Enter financial queries such as:
      - "What is the total revenue?"
      - "What is the net income growth(%)?"
      - "What is the cash flow from operations growth(%)?"
      - And more (see the full list below).
5. **Get instant responses:** The chatbot retrieves the requested data from pre-loaded CSV files and formats the response.

## Example Queries

### Here’s a list of queries the chatbot can handle:

- Total revenue, net income, total assets, and total liabilities.
- Revenue growth, net income growth, assets growth, and liabilities growth.
- Cash flow from operating activities and its growth rate.
- Year-by-year average growth rates for revenue, net income, assets, liabilities, and cash flow.
  
## Prerequisites

### To run the chatbot, you’ll need:

1. Python 3.x installed on your machine.
2. Two CSV files containing financial data:
   - final_data_report.csv: Contains detailed financial data by year and company.
   - Summary_final_report.csv: Contains summarized financial growth rates by company.
     
## Installation

1. **Clone this repository:**
   ```
   git clone https://github.com/your-username/financial-chatbot.git
   cd financial-chatbot
   ```
2. **Install required Python packages:**
   ```
   pip install pandas
   ```
3.  **Ensure the required CSV files (final_data_report.csv and Summary_final_report.csv) are in the same directory as the script.**
   
4.  **Run the chatbot:**
    ```
    python BCGX_GENAI_Chatbot.py
    ```
## Usage   

### When you run the chatbot, follow these steps:

 1. Start the chatbot by entering "Hi".
 2. Select a company: Apple, Microsoft, or Tesla.
 3. Enter the fiscal year (2021, 2022, or 2023).
 4. Type your financial query and get instant results.
 5. Optionally, continue asking questions or exit the chatbot by typing "no" when prompted.
    
## Sample Interaction

### Here’s an example of how the chatbot works:

```
Enter 'Hi' to start the chatbot session; type 'exit' to quit: Hi

Hello! Welcome to the AI-Driven Financial Chatbot!

I can assist you with your financial queries.
Please select a company from the following options:
1. Microsoft 
2. Tesla 
3. Apple
Enter company name: Apple

The data for the fiscal years 2023, 2022, and 2021 is currently available.
Enter the fiscal year for the selected company: 2023

Please enter your financial query:
What is the total revenue?
What is the total revenue? for Apple for fiscal year 2023 is $ 394700000000

Would you like to ask another question? (yes/no): no
Thank you for using the Financial Chatbot. Goodbye!
```
### Technologies Used

  - Python: Core programming language.
  - pandas: For data manipulation and retrieval from CSV files.
  - CSV Files: Contain financial data and summaries.
    
### Customization

## You can extend the chatbot’s functionality by:

 1. Adding more companies or fiscal years to the CSV files.
 2. Expanding the data_mapping dictionary in the code to include additional financial queries.
 3. Enhancing the user interface for better interactivity (e.g., integrating a web or GUI front end).
    
### Limitations

- The chatbot only supports three companies (Apple, Microsoft, Tesla) and three fiscal years (2021, 2022, 2023).   
- It relies on the accuracy and completeness of the provided CSV files.
- Queries outside the predefined data_mapping dictionary will not be processed.
   
