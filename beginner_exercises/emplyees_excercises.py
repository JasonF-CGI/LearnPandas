import pandas as pd

# Load data into 'employees_df'
employees_df = pd.read_csv('../datasets/employees_data.csv')

# 1. Show the first 5 rows.
# Hint: use .head()


# 2. What is the average salary?
# Hint: use .mean()


# 3. What is the minimum salary?
# Hint: use .min()


# 4. What is the maximum salary?
# Hint: use .max()


# 5. What is the average years of experience?
# Hint: select the column first, then use .mean()


# 6. Show summary statistics for `salary` and `years_experience` using `.describe()`.
# Hint: select multiple columns with [[]]


# 7. Find all employees in the `IT` department.
# Hint: boolean filtering with ==


# 8. Find all full-time employees.
# Hint: filter using the 'full_time' column


# 9. Find employees with more than 10 years of experience.
# Hint: use > for comparison


# 10. Create a new column called `salary_per_year_experience`
#     using `salary / years_experience`.
# Hint: assign a new column using df["new_column"] = ...


# 11. Group by `department` and calculate the average salary.
# Hint: use .groupby() and .mean()


# 12. Group by `department` and count employees.
# Hint: use .groupby() and .count() or .size()


# 13. Find the highest-paid employee.
# Hint: use .max() with filtering


# 14. Sort by `salary` from highest to lowest.
# Hint: use .sort_values()


# 15. Find how many employees are full-time vs part-time.
# Hint: use .value_counts()


# 16. Find employees whose salary is above the overall average salary.
# Hint: calculate the average first, then filter


# ----------------------
# Challenge
# ----------------------

# 17. Which department has the highest average salary?
# Hint: combine .groupby() with sorting or .idxmax()