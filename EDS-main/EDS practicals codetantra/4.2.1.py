import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
df['TotalSales'] = df['Quantity'] * df['Price']
df['Month']=pd.to_datetime(df['Date']).dt.to_period('M')
montly_sales= df.groupby('Month')['TotalSales'].sum()



# Find the month with the highest total sales
best_month = montly_sales.idxmax()
highest_sales = montly_sales.max()

print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
