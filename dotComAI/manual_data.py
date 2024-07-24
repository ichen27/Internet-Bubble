import pandas as pd

netscape = {
    'Date': ['1995-08-09', '1995-12-01', '1999-11-24', '2001-07-01'],
    'MarketCap': [2900000000, 5000000000, 10000000000, 0],
    'Notes': ['IPO', 'Pre Bubble', 'Acquisition by AOL', 'Post Bubble'],
    'Profit': [-75000000, -90000000, -115000000, -75000000],
    'Profit Notes': ['1995 Total', '1996 Total', '1997 Total', '1998 Total']
}

aol = {
    'Date': ['1992-03-19', '1999-12-01', '2001-12-01'],
    'MarketCap': [70000000, 200000000000, 20000000000],
    'Notes': ['IPO', 'Peak', 'Post Bubble'],
    'Profit': [2000000, 1500000000, -1000000000],
    'Profit Notes': ['1992 Total', '1999 Total', '2001 Total']
}


csco = {
    'Date': ['1990-02-16', '1995-12-01', '2000-03-27', '2002-10-01'],
    'MarketCap': [224000000, 40000000000, 555000000000, 60000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [5000000, 1090000000, 2600000000, 1800000000],
    'Profit Notes': ['1990 Total', '1995 Total', '2000 Total', '2001 Total']
}

amzn = {
    'Date': ['1997-05-15', '1999-12-01', '2001-12-01'],
    'MarketCap': [438000000, 30000000000, 2000000000],
    'Notes': ['IPO', 'Peak', 'Post Bubble'],
    'Profit': [-3000000, -720000000, -560000000],
    'Profit Notes': ['1997 Total', '1999 Total', '2001 Total']
}


msft = {
    'Date': ['1986-03-13', '1995-12-01', '1999-12-01', '2002-01-01'],
    'MarketCap': [778000000, 40000000000, 620000000000, 275000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [25000000, 1440000000, 7800000000, 7500000000],
    'Profit Notes': ['1986 Total', '1995 Total', '1999 Total', '2001 Total']
}

intel = {
    'Date': ['1971-10-13', '1995-12-01', '1999-12-01', '2002-01-01'],
    'MarketCap': [5800000000, 80000000000, 500000000000, 200000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [6600000, 3100000000, 10600000000, 2900000000],
    'Profit Notes': ['1971 Total', '1995 Total', '1999 Total', '2001 Total']
}


orcl = {
    'Date': ['1986-03-12', '1995-12-01', '2000-09-01', '2002-01-01'],
    'MarketCap': [270000000, 12000000000, 210000000000, 50000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [10000000, 239000000, 2688000000, 549000000],
    'Profit Notes': ['1986 Total', '1995 Total', '2000 Total', '2001 Total']
}

qcom = {
    'Date': ['1991-12-13', '1999-12-01', '2000-01-03', '2002-01-01'],
    'MarketCap': [950000000, 20000000000, 470000000000, 35000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [-19000000, 670000000, 3600000000, 800000000],
    'Profit Notes': ['1991 Total', '1999 Total', '2000 Total', '2001 Total']
}
yahoo = {
    'Date': ['1996-04-12', '1998-12-01', '1999-12-01', '2002-01-01'],
    'MarketCap': [848000000, 42000000000, 125000000000, 5000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [-5600000, 25000000, 47000000, -93000000],
    'Profit Notes': ['1996 Total', '1998 Total', '1999 Total', '2001 Total']
}
ebay = {
    'Date': ['1998-09-24', '1999-12-01', '2000-03-10', '2002-01-01'],
    'MarketCap': [700000000, 27000000000, 31000000000, 18000000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble'],
    'Profit': [-5000000, 1000000, -3000000, -6500000],
    'Profit Notes': ['1998 Total', '1999 Q4', '2000 Q1', '2001 Total']
}

webvan = {
    'Date': ['1999-11-05', '1999-12-01', '2000-01-03', '2001-07-09'],
    'MarketCap': [4800000000, 7800000000, 8900000000, 12000000],
    'Notes': ['IPO', 'Pre Bubble', 'Peak', 'Post Bubble/Pre Bankruptcy'],
    'Profit': [-50000000, -76000000, -90000000, -830000000],
    'Profit Notes': ['1999 Total', '2000 Q1', '2000 Q2', '2000 Total']
}

petscom = {
    'Date': ['2000-02-11', '2000-03-10', '2000-04-01', '2000-11-06'],
    'MarketCap': [290000000, 340000000, 360000000, 5600000],
    'Notes': ['IPO', 'Peak', 'Post-IPO', 'Post Bubble/Pre Bankruptcy'],
    'Profit': [-61000000, -85000000, -95000000, -147000000],
    'ProfitNotes': ['2000 Q1', '2000 Q2', '2000 Q3', '2000 Total']
}

