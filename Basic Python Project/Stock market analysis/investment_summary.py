import pandas as pd
import yfinance as yf
import gc

try:
    stocks = pd.read_csv('stocks.csv')
    if 'Ticker' not in stocks.columns or 'Weightage' not in stocks.columns:
        raise ValueError("CSV must contain 'Ticker' and 'Weightage' columns.")

    # Convert Weightage to float
    stocks['Weightage'] = pd.to_numeric(stocks['Weightage'], errors='coerce')
    if stocks['Weightage'].isnull().any():
        raise ValueError("Some weightages could not be converted to numeric values.")
except Exception as e:
    print(f"Error loading CSV file: {e}")
    exit()

investment_amount = float(input("Enter the investment amount: "))
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

investment_data = []
all_data = pd.DataFrame()

for ticker in stocks['Ticker']:
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        if stock_data.empty:
            print(f"No data found for {ticker} in the specified date range.")
            continue

        closing_prices = stock_data['Close'].squeeze()

        for date, closing_price in closing_prices.items():
            if pd.notnull(closing_price):
                weightage = stocks.loc[stocks['Ticker'] == ticker, 'Weightage'].values[0]
                amount_invested = investment_amount * weightage
                shares_bought = amount_invested / closing_price
                investment_data.append([
                    date.strftime('%Y-%m-%d'),
                    ticker,
                    round(amount_invested, 2),
                    round(closing_price, 2),
                    round(shares_bought, 4)
                ])

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

if investment_data:
    df = pd.DataFrame(investment_data, columns=[
        'Date', 'Ticker', 'Amount Invested', 'Closing Price',  'Shares Bought'
    ])
    file_name = "output.csv"
    df.to_csv(file_name, index=False)
    print(f"Investment summary saved to {file_name}")
else:
    print("No data to save.")

gc.collect()
