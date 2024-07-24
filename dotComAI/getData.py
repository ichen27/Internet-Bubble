
# Import Libraries
import yfinance as yf


# Specify Companies and Period
companies = ['SUNWQ', 'AABA', 'AOL', 'EMC']
start_date = '1990-01-01'
end_date = '2005-01-01'

# Download data for specified companies and date range
for company in companies:
    data = yf.download(company, start=start_date, end=end_date)
    if len(data.index) == 0:
        print(f"No data found for {company}")
        continue

    data.to_csv(f'aihist/{company}.csv')
    print(f"Data for {company} saved successfully.")

print('Download completed.')