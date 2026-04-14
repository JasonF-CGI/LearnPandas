import pandas as pd

# Load data into 'fitness_df'
fitness_df = pd.read_csv('../datasets/fitness_data.csv')

# 1. Show the first 5 rows.
# Hint: use .head()


# 2. Convert the `date` column to datetime.
# Hint: use pd.to_datetime()


# 3. Find the day with the most steps.
# Hint: use .max() or .idxmax()


# 4. Find the day with the fewest steps.
# Hint: use .min() or .idxmin()


# 5. Calculate the average number of steps.
# Hint: use .mean()


# 6. Calculate the average sleep hours.
# Hint: select the column first


# 7. Create a new column called `calories_per_active_minute`.
# Hint: divide one column by another


# 8. Sort by `sleep_hours` from highest to lowest.
# Hint: use .sort_values()


# 9. Find all days where `active_minutes` was greater than 60.
# Hint: boolean filtering with >


# 10. Group by month and calculate total steps.
# Hint: extract month from the date, then use .groupby()


# 11. Calculate the rolling 7-day average for `steps`.
# Hint: use .rolling()


# 12. Find the day with the highest calories burned.
# Hint: use .idxmax()


# ----------------------
# Challenge
# ----------------------

# 13. On which day were both steps and active minutes above their averages?
# Hint: calculate averages first, then filter with multiple conditions