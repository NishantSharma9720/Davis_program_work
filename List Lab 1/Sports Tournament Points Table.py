team_points = {"TeamA": 25, "TeamB": -5, "TeamC": 30, "TeamD": 28}

# Replace negative points with 0
team_points = {k: max(0, v) for k,v in team_points.items()}

# Sort leaderboard (descending)
leaderboard = dict(sorted(team_points.items(), key=lambda x: x[1], reverse=True))

# Winner and runner-up
teams_sorted = list(leaderboard.keys())
winner = teams_sorted[0]
runner_up = teams_sorted[1] if len(teams_sorted) > 1 else None

print("Leaderboard:", leaderboard)
print("Winner:", winner)
print("Runner-up:", runner_up)