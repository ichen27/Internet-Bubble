import pandas as pd
import json
import plotly.express as px



with open('dotcom_bubble_data.json', 'r') as file:
    data = json.load(file)

long_format_data = []


for company, details in data.items():
    for i in range(len(details['Date'])):
        entry = {
            'Company': company,
            'Date': details['Date'][i],
            'MarketCap': details['MarketCap'][i],
            'Notes': details['Notes'][i],
            'Profit Notes': details['Profit Notes'][i]
        }
        long_format_data.append(entry)


long_format_df = pd.DataFrame(long_format_data)

long_format_df['Date'] = pd.to_datetime(long_format_df['Date'])

# Create the Plotly graph
fig = px.line(long_format_df, x='Date', y='MarketCap', color='Company', markers=True,
              title='Market Cap of Companies Over Time',
              labels={'MarketCap': 'Market Cap', 'Date': 'Date'})

# Update layout for better visualization
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Market Cap',
    legend_title='Company',
    hovermode='x unified'
)

# Show the graph
fig.show()