import pandas as pd

# Load data into 'students_df'
students_df = pd.read_csv('../datasets/students_data.csv')

# 1. Show the first 5 rows.
# Hint: use .head()


# 2. Display the number of rows and columns.
# Hint: use .shape


# 3. Find the unique courses.
# Hint: use .unique()


# 4. Select only the `name`, `age`, and `course` columns.
# Hint: use double brackets [[]]


# 5. Find all students older than 21.
# Hint: use > for comparison


# 6. Find all students enrolled in `CS`.
# Hint: boolean filtering with ==


# 7. Count how many students are in each course.
# Hint: use .value_counts()


# 8. Count how many students received each grade.
# Hint: use .value_counts()


# 9. Find the average age of the students.
# Hint: use .mean()


# 10. Sort by `age` from youngest to oldest.
# Hint: use .sort_values()


# 11. Find the students with grade `A`.
# Hint: boolean filtering


# 12. Find the oldest student.
# Hint: use .max() or .idxmax()


# ----------------------
# Challenge
# ----------------------

# 13. Which course has the highest number of grade `A` students?
# Hint: filter grade 'A', then count by course