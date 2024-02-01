import pandas as pd

team_stats = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/team_stats22')
team_hustle = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/team_hustle_stats22.csv')

team_merged = pd.merge(team_stats, team_hustle, on='TEAM_ID', how='inner')

exclude_columns = ['TEAM_ID', 'GP']

# Calculate per game averages
for col in team_merged.columns:
    if col not in exclude_columns:
        team_merged[col + '_PG'] = team_merged.apply(lambda x: x[col] / x['GP'] if x['GP'] > 0 else 0, axis=1)

# Assuming your per game columns end with '_per_game'
per_game_columns = [col for col in team_merged.columns if '_PG' in col]

# Round these specific columns to 2 decimal places
team_merged[per_game_columns] = team_merged[per_game_columns].round(2)

team_merged = team_merged.drop(columns=['GP', 'BLK', 'BLKA', 'STL', 'DREB', 'BOX_OUTS', 'CONTESTED_SHOTS_2PT',
                           'CONTESTED_SHOTS_3PT', 'CONTESTED_SHOTS', 'DEFLECTIONS', 'LOOSE_BALLS_RECOVERED',
                           'CHARGES_DRAWN'])

team_merged.to_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/merged_team_stats22.csv', index=False)