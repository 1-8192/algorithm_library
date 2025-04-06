# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.

# Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+

# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Schema:
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    """

    # Get unique salary values
    unique_salaries = employee['salary'].unique()
    
    # Sort in descending order
    unique_salaries = np.sort(unique_salaries)[::-1]
    
    # Create result DataFrame with appropriate column name
    result = pd.DataFrame(columns=['SecondHighestSalary'])
    
    # Check if there is a second highest salary
    if len(unique_salaries) >= 2:
        result.loc[0] = unique_salaries[1]
    else:
        result.loc[0] = None
        
    return result