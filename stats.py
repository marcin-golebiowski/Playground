import datetime
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

# Read data from the file
file_name = 'log.txt'
with open(file_name, 'r') as file:
    data = file.readlines()

# Extract information from the commit log
commits = []
authors = Counter()
dates = []
commit_messages = defaultdict(list)

for line in data:
    try:
        parts = line.strip().split(',')
        commit_id = parts[0].strip()
        author_info = parts[1].strip()
        author_name = author_info.split('<')[0].strip()
        commit_date_str = parts[2].strip()
        commit_date = datetime.datetime.strptime(commit_date_str, "%Y-%m-%d %H:%M:%S %z")
        commit_message = parts[3].strip()

        commits.append(commit_id)
        authors[author_name] += 1
        dates.append(commit_date)
        commit_messages[author_name].append(commit_message)
    except (IndexError, ValueError):
        pass  # Ignore lines that don't match the expected format

# Generate statistics
total_commits = len(commits)
unique_authors = len(authors)
most_active_author = authors.most_common(1)[0]
commits_per_day = Counter([date.date() for date in dates])

# Print statistics
print(f"Total commits: {total_commits}")
print(f"Unique authors: {unique_authors}")
print(f"Most active author: {most_active_author[0]} with {most_active_author[1]} commits")

print("\nCommits per day:")
for date, count in commits_per_day.items():
    print(f"{date}: {count} commits")

# Example of printing commit messages by author
print("\nCommit messages by author:")
for author, messages in commit_messages.items():
    print(f"\nAuthor: {author}")
    for msg in messages:
        print(f"  - {msg}")

# Generate plot for commits over time
sorted_dates = sorted(commits_per_day.keys())
commit_counts = [commits_per_day[date] for date in sorted_dates]

plt.figure(figsize=(10, 5))
plt.plot(sorted_dates, commit_counts, marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Commits')
plt.title('Commits Over Time')
plt.grid(True)
plt.show()
