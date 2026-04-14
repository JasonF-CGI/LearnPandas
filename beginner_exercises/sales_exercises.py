import pandas as pd

# Load data into 'sales_df'
sales_df = pd.read_csv('../datasets/sales_data.csv')

# 1. Show the first 5 rows.
# Hint: use .head()


# 2. Display the column names and data types.
# Hint: use .columns and .dtypes


# 3. Find the total number of orders.
# Hint: use len() or .shape


# 4. Select only the `product`, `region`, `price`, and `quantity` columns.
# Hint: use double brackets [[]]


# 5. Find all rows where `region` is `North`.
# Hint: boolean filtering with ==


# 6. Find all orders where `price` is greater than 500.
# Hint: use > for comparison


# 7. Create a new column called `total_value` using `price * quantity`.
# Hint: assign a new column using df["new_column"] = ...


# 8. Find the order with the highest `total_value`.
# Hint: use .idxmax() or sort and take the first row


# 9. Group by `product` and calculate the average `price`.
# Hint: use .groupby() and .mean()


# 10. Group by `region` and calculate the total `quantity`.
# Hint: use .groupby() and .sum()


# 11. Sort the DataFrame by `total_value` from highest to lowest.
# Hint: use .sort_values()


# 12. Find which product appears most often.
# Hint: use .value_counts()


# ----------------------
# Challenge
# ----------------------

# 13. Which region has the highest total sales value?
# Hint: create total_value if needed, then group by region and sum