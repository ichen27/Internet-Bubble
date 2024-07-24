import quandl

# Set your API key
quandl.ApiConfig.api_key = 'YOUR_API_KEY'

# Define the Quandl code for the company
quandl_code = 'WIKI/YHOO'  # Example for Yahoo!

# Download the data
data = quandl.get(quandl_code, start_date='1990-01-01', end_date='2000-12-31')
print(data.head())
