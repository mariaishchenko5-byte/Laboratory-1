list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
half_team = len(list_players) // 2

team_one = list_players[:half_team]
team_two = list_players[half_team:]

print(team_one)
print(team_two)
