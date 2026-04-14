import pandas as pd
from pandas.core.interchange import column

# Load data into 'employees_df'
employees_df = pd.read_csv('datasets/employees_data.csv')

# 1. Show the first 5 rows.
print(employees_df.head(5))

# 2. Display summary statistics for numeric columns (salary and years_experience)
print(employees_df[["salary", "years_experience"]].describe())

# Highest paid employees
pay_subset = employees_df[employees_df["salary"] == employees_df["salary"].max()]

# Longest serving employees
service_subset = employees_df[
    employees_df["years_experience"] == employees_df["years_experience"].max()
]

# print("The longest serving employees are:\n", service_subset)
# print("The highest paid employees are:\n", pay_subset)
# 3. Find all employees in the `IT` department.
# 4. Find all full-time employees.
# 5. Find employees with more than 10 years of experience.
# 6. Create a new column called `salary_per_year_experience` using `salary / years_experience`.
# 7. Group by `department` and calculate the average salary.
# 8. Group by `department` and count employees.
# 9. Find the highest-paid employee.
# 10. Sort by `salary` from highest to lowest.
# 11. Find how many employees are full-time vs part-time.
# 12. Find employees whose salary is above the overall average salary.
