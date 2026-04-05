import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 40000, 60000, 45000, 55000]
}
df = pd.DataFrame(data)

# Grouping by Department to find average salary
avg_salary = df.groupby('Department')['Salary'].mean()
print("Average Salary per Dept:")
print(avg_salary)
