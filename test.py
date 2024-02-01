import pandas as pd
from nba_api.stats.endpoints import playerestimatedmetrics, leaguedashplayerstats

df_off_stats = pd.DataFrame()
df_player_stats = pd.DataFrame()

pd.set_option('display.max_columns', None)

off_stats = playerestimatedmetrics.PlayerEstimatedMetrics(season='2022-23')
df_off_stats = off_stats.get_data_frames()[0]

player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2022-23')
df_player_stats = player_stats.get_data_frames()[0]

df_off_stats = df_off_stats[['PLAYER_ID', 'PLAYER_NAME', 'E_OFF_RATING']]
df_player_stats = df_player_stats[['PLAYER_ID', 'GP', 'MIN', 'FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTA',
                                   'OREB', 'AST', 'TOV', 'PTS', 'PLUS_MINUS']]

exclude_columns = ['PLAYER_ID', 'GP', 'FG_PCT', 'FG3_PCT']

# Calculate per game averages
for col in df_player_stats.columns:
    if col not in exclude_columns:
        df_player_stats[col + '_PG'] = df_player_stats.apply(lambda x: x[col] / x['GP'] if x['GP'] > 0 else 0, axis=1)

# Assuming your per game columns end with '_per_game'
per_game_columns = [col for col in df_player_stats.columns if '_PG' in col]

# Round these specific columns to 2 decimal places
df_player_stats[per_game_columns] = df_player_stats[per_game_columns].round(2)

df_player_stats = df_player_stats.drop(columns=['MIN', 'FGA', 'FG3A', 'FTA',
                                   'OREB', 'AST', 'TOV', 'PTS', 'PLUS_MINUS'])

player_merged = pd.merge(df_off_stats, df_player_stats, on='PLAYER_ID', how='inner')

player_filtered = player_merged[player_merged['MIN_PG'] >= 27.1]
player_filtered = player_filtered[player_filtered['GP'] >= 45]
player_filtered = player_filtered[player_filtered['PTS_PG'] >= 20]

# Assuming df is your original DataFrame and 'specific_stat_column' is the column of interest
top_30_players = player_filtered.nlargest(30, 'E_OFF_RATING')


top_30_players.to_csv('/Users/zachcarlson/Documents/NBA Project/2022-23/offensive_stats23.csv', index=False)