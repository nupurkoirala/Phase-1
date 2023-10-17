import pandas as pd
import matplotlib.pyplot as plt

# question 1
# Load the CSV file into a DataFrame
df = pd.read_csv('Construction_Data_PM_Tasks_All_Projects.csv')

# Filter tasks that are overdue
overdue_tasks = df[df['OverDue'] == True]

# Count the number of overdue tasks
total_overdue_tasks = len(overdue_tasks)

# Print the result
print(f'Total number of tasks that are overdue: {total_overdue_tasks}')

# question 2
# Group tasks by 'Task Group' and 'Report Status', and count the occurrences
grouped = df.groupby(['Task Group', 'Report Status']).size().unstack(fill_value=0)

# Print the result
print(grouped)

#question 3

# Create a bar chart
grouped.plot(kind='bar', stacked=True)
plt.xlabel('Task Group')
plt.ylabel('Number of Tasks')
plt.title('Total Number of Open and Closed Tasks by Task Group')

# Show the chart
plt.legend(title='Report Status', loc='upper right')

plt.savefig('task_group_chart.png')
plt.close() # Close the current figure

# question 4

# Create a new figure for question 4
plt.figure()

# Group and count the total number of overdue tasks by project
overdue_by_project = df.groupby('project')['OverDue'].sum()

# Create a bar chart
overdue_by_project.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Project')
plt.ylabel('Number of Overdue Tasks')
plt.title('Total Number of Overdue Tasks by Project')

# Save the chart as an image
plt.savefig('overdue_tasks_by_project.png')
