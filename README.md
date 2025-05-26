# Loan Simulator Application

A Streamlit web application that simulates loan payments based on user inputs like loan amount and repayment period.

## Overview

This application allows users to:
- Simulate loan payments for amounts between a minimum and maximum value
- Choose a repayment period between 1 and 18 months
- View the resulting monthly payment amount
- Get a unique reference ID for their simulation

## Features

- Dynamic interest rate calculation based on loan amount and repayment period
- Connection to Google Sheets for retrieving up-to-date parameters
- Fallback to default values when online data is unavailable
- Mobile-friendly interface with Streamlit
- Generates unique reference IDs for each simulation

## Code Structure

### `main.py`

The main application file that contains:
- Streamlit UI implementation
- The `Main` class that runs the application
- Connection to Google Sheets for retrieving configuration data
- Input validation and business logic for loan simulation

### `calculator.py`

Contains the core financial calculation functions:
- `calculate_compound_interest`: Calculates compound interest for a given principal, rate, and time
- `compound_interest`: Generates monthly payment and total interest based on loan amount, rate, and time
- `generate_random_string`: Creates random strings for reference ID generation

### `.streamlit/secrets.toml`

Contains configuration secrets like the Google Sheet ID for retrieving application parameters.

## How to Run

1. Install dependencies:
   ```
   pip install streamlit pandas
   ```

2. Run the application:
   ```
   streamlit run main.py
   ```

## Data Source

The application retrieves key parameters from a Google Sheet:
- Interest rate
- Minimum loan amount
- Maximum loan amount

It falls back to default values if the sheet is unavailable.
