import pandas as pd

team_stats = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/merged_team_stats22.csv')
player_stats = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/player_merged_stats22.csv')
defend_stats = pd.read_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/defend_stats22.csv')

pct_merged = pd.merge(player_stats, team_stats, on='TEAM_ID', suffixes=('_PLAYER', '_TEAM'))

# Calculate the contribution percentage for each stat
for stat in ['BLK', 'BLKA', 'DREB', 'STL', 'CONTESTED_SHOTS', 'CONTESTED_SHOTS_2PT', 'CONTESTED_SHOTS_3PT',
             'DEFLECTIONS', 'CHARGES_DRAWN', 'LOOSE_BALLS_RECOVERED', 'BOX_OUTS']:  # Add other stats as needed
    player_stat = f'{stat}_PG_PLAYER'
    team_stat = f'{stat}_PG_TEAM'
    contribution_stat = f'{stat}_PCT'

    pct_merged[contribution_stat] = (pct_merged[player_stat] / pct_merged[team_stat])

# Round the contribution percentages to 2 decimal points
pct_merged = pct_merged.round(2)

contribution_cols = [col for col in pct_merged.columns if '_PCT' in col]

player_stats = pd.merge(player_stats, pct_merged[['PLAYER_ID'] + contribution_cols], on='PLAYER_ID')
final_merged = pd.merge(player_stats, defend_stats, on='PLAYER_ID', how='inner')

final_merged.to_csv('/Users/zachcarlson/Documents/NBA Project/2021-22/merged_stats22.csv', index=False)

