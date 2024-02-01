import pandas as pd

player_stats = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/merged_stats22.csv')

player_filtered = player_stats[player_stats['MIN_PG'] >= 12]

index_to_drop = player_filtered[player_filtered['PLAYER_ID'] == 1630270].index

# Now drop this row
player_filtered = player_filtered.drop(index_to_drop)

player_filtered.to_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/player_filtered_stats22.csv', index=False)