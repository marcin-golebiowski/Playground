import matplotlib.pyplot as plt
from collections import Counter
import datetime

# Read data from the file
file_name = 'log.txt'
with open(file_name, 'r') as file:
    data = file.readlines()

# Extract dates from the commit log
dates = []
for line in data:
    try:
        parts = line.strip().split(',')
        date_str = parts[2].strip()  # Extract the date part
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")  # Adjusting the date format
        dates.append(date)
    except (IndexError, ValueError):
        pass  # Ignore lines that don't match the expected format

# Count commits per date
commit_counts = Counter(dates)
sorted_dates = sorted(commit_counts.keys())
commit_counts = [commit_counts[date] for date in sorted_dates]

# Generate the plot
plt.figure(figsize=(10, 5))
plt.plot(sorted_dates, commit_counts, marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
plt.title('Commits Over Time')
plt.grid(True)
plt.show()
