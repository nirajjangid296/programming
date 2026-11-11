votes = input().split()
vote_counts = {}

for candidate in votes:
    vote_counts[candidate] = vote_counts.get(candidate, 0) + 1

for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")

winner = max(vote_counts, key=vote_counts.get)
print(f"Winner: {winner}")
