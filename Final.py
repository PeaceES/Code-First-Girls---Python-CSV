import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("\n")
print("# ----- Read the data from the spreadsheet ----- #")

def read_data():
    # Ensure 'sales.csv' is located in your project folder
    df = pd.read_csv('sales.csv')
    # Capitalise all column titles
    df.columns = [col.capitalize() for col in df.columns]
    # Capitalise all values in 'Month' column
    df['Month'] = df['Month'].str.capitalize()
    return df

# Read data into a data frame called "data_df"
data_df = read_data()

# Print the data frame
print(data_df)
print("\n")

print("# ----- Collect sales from each month into a single list ----- #")

# Use the 'data_df' data frame to access the 'sales' column and convert it to a list called "sales_list"
sales_list = data_df['Sales'].tolist()

# Print the sales list
print("Single list of all sales: ", sales_list)
print("\n")

print("# ----- Output the total sales across all months ----- #")

# Calculate the total sales using the 'sales' column from our data frame
total_sales = data_df['Sales'].sum()

# Output the total sales
print(f'Total sales across all months: £{total_sales:.2f}')
print("\n")

print("# ----- Arithmetic Calculations ----- #")

# Find the average monthly sales
monthly_average = round(total_sales/12, 2)
print(f'The monthly sales average is: £{monthly_average:.2f}')

# The highest sales
highest_sales = data_df['Sales'].max() # finds the highest number in the sales column
highest_sales_index = data_df['Sales'].idxmax() # finds the row position of the highest number in the sales column
highest_month = data_df.loc[highest_sales_index, 'Month'] # finds the month in the corresponding position
print('Month with highest sales:', highest_month, f'| Amount: £{highest_sales:.2f}') # display info

# The lowest sales
lowest_sales = data_df['Sales'].min() # finds the lowest number in the sales column
lowest_sales_index = data_df['Sales'].idxmin() # finds the row position of the lowest number in the sales column
lowest_month = data_df.loc[lowest_sales_index, 'Month'] # finds the month in the corresponding position
print('Month with lowest sales:', lowest_month, f'| Amount: £{lowest_sales:.2f}') # display info

# Calculate monthly changes as a percentage

# List to store the values of the percentage changes
percentage_list = []

# Starting from the second value, iterate through the sales_list & calculate the % change from the previous month
list_length = len(sales_list)
for i in range(1, list_length):
    current_sales = sales_list[i]
    previous_sales = sales_list[i-1]
    percentage_difference = round(((current_sales - previous_sales)/previous_sales)*100, 2)
    # Add each percentage change to the list
    percentage_list.append(percentage_difference)
print("Monthly Changes %: ", percentage_list)
print("\n")

print("# ----- Data Classification ----- #")

# Define bins as 0 to 2000, 2000 to 3500, 3500 to 5000, and 5000 to max sales + 1 to include the highest value in the range
bins = [0, 2000, 3500, 5000, data_df['Sales'].max() + 1]

# Define the names for the four categories
labels = ['Bad', 'Average', 'Good', 'Excellent']

# Create a new column 'Rating' using pd.cut to segment and sort data values into bins
data_df['Rating'] = pd.cut(data_df['Sales'], bins=bins, labels=labels, right=False)

# Display the DataFrame with the new 'Rating' column
print(data_df[['Month', 'Sales', 'Rating']])

# ----- Data Visualization ----- #

# Set the style
sns.set_theme(style="darkgrid")

# Plotting the sales line
sns.lineplot(data=data_df, x='Month', y='Sales', label='Sales', marker='o')

# Plotting the expenditure line on the same plot
sns.lineplot(data=data_df, x='Month', y='Expenditure', label='Expenditure', marker='o')

# Adding titles and labels
plt.title('Sales and Expenditure Over Time')
plt.xlabel('Month')
plt.ylabel('Value (£)')

# Adding a legend
plt.legend()

# Show the plot
plt.show()

# ----- Exporting to csv ----- #

# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Metric': ['Highest Sales', 'Lowest Sales', 'Total Sales'],
    'Month': [highest_month, lowest_month, ""],
    'Amount (£)': [highest_sales, lowest_sales, total_sales]})

# Specify the path where you want to save the file. If in the same folder as this python code, just specify the name
summary_csv_path = 'Summary.csv'
data_csv_path = 'Sales Classification.csv'

# Export the DataFrames
summary_df.to_csv(summary_csv_path, index=False, encoding='utf-8-sig')
data_df.to_csv(data_csv_path, index=False, encoding='utf-8-sig')
#  the index=False parameter tells pandas not to write the row indices into the csv file
# utf-8-sig displays the £ sign correctly without the preceding 'Â' character

print(f'Summary data exported to {summary_csv_path}')
print(f'Classification data exported to {data_csv_path}')
