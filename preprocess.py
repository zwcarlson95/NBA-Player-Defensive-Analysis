import pandas as pd

team_stats = pd.read_csv('team_stats22')
player_stats = pd.read_csv('player_stats22.csv')
hustle_stats = pd.read_csv('hustle_stats22.csv')

player_merged = pd.merge(player_stats, hustle_stats, on='PLAYER_ID', how='inner')

exclude_columns = ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'GP']

# Calculate per game averages
for col in player_merged.columns:
    if col not in exclude_columns:
        player_merged[col + '_PG'] = player_merged.apply(lambda x: x[col] / x['GP'] if x['GP'] > 0 else 0, axis=1)

per_game_columns = [col for col in player_merged.columns if '_PG' in col]

# Round these specific columns to 2 decimal places
player_merged[per_game_columns] = player_merged[per_game_columns].round(2)

player_merged = player_merged.drop(columns=['GP', 'MIN', 'BLK', 'BLKA', 'STL', 'DREB', 'BOX_OUTS', 'CONTESTED_SHOTS_2PT',
                           'CONTESTED_SHOTS_3PT', 'CONTESTED_SHOTS', 'DEFLECTIONS', 'LOOSE_BALLS_RECOVERED',
                           'CHARGES_DRAWN'])

player_merged.to_csv('player_merged_stats22.csv', index=False)
