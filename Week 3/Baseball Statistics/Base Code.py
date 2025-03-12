dtype = np.dtype([('Year',int),('Age',int),('PA',int),('AB',int),('R',int),('H',int),('2B',int),('3B',int),('HR',int),
                ('RBI',int),('BB',int),('SO',int),('BA',int),('OBP',int),('SLG',int),('OPS',int),('OPS+',int),('TB',int)])

file_path_BB = r"C:\Users\zscon\Desktop\SSE 591-Python and Data Science\Baseball Statistics\Barry Bonds Stats.csv"
file_path_MM = r"C:\Users\zscon\Desktop\SSE 591-Python and Data Science\Baseball Statistics\Mark McGwire Stats.csv"
file_path_AR = r"C:\Users\zscon\Desktop\SSE 591-Python and Data Science\Baseball Statistics\Alex Rodriguez Stats.csv"
file_path_SS = r"C:\Users\zscon\Desktop\SSE 591-Python and Data Science\Baseball Statistics\Sammy Sosa Stats.csv"

data_BB = np.genfromtxt(file_path_BB,delimiter = ',',dtype = dtype,names = True)

data_MM = np.genfromtxt(file_path_MM,delimiter = ',',dtype = dtype,names = True)

data_AR = np.genfromtxt(file_path_AR,delimiter = ',',dtype = dtype,names = True)

data_SS = np.genfromtxt(file_path_SS,delimiter = ',',dtype = dtype,names = True)

print('Barry Bonds\' Home Runs during the "Steriod Era":')
#Extracting data from original array using boolean conditions
HR_BB_data = data_BB[(data_BB['Year'] >= 1994) & (data_BB['Year'] <= 2001)]
HR_BB_year = HR_BB_data['Year']
HR_BB_hr = HR_BB_data['HR']
#combining year and hr into 2D array
HR_BB = np.column_stack((HR_BB_year, HR_BB_hr))
print(HR_BB)

print('\nMark McGwire\'s Home Runs during the "Steriod Era":')
HR_MM_data = data_MM[(data_MM['Year'] >= 1994) & (data_MM['Year'] <= 2001)]
HR_MM_year = HR_MM_data['Year']
HR_MM_hr = HR_MM_data['HR']
#combining year and hr into 2D array
HR_MM = np.column_stack((HR_MM_year, HR_MM_hr))
print(HR_MM)

print('\nAlex Rodriguez\'s Home Runs during the "Steriod Era":')
HR_AR_data = data_AR[(data_AR['Year'] >= 1994) & (data_AR['Year'] <= 2001)]
HR_AR_year = HR_AR_data['Year']
HR_AR_hr = HR_AR_data['HR']
#combining year and hr into 2D array
HR_AR = np.column_stack((HR_AR_year, HR_AR_hr))
print(HR_AR)

print('\nSammy Sosa\'s Home Runs during the "Steriod Era":')
HR_SS_data = data_SS[(data_SS['Year'] >= 1994) & (data_SS['Year'] <= 2001)]
HR_SS_year = HR_SS_data['Year']
HR_SS_hr = HR_SS_data['HR']
#combining year and hr into 2D array
HR_SS = np.column_stack((HR_SS_year, HR_SS_hr))
print(HR_SS)

# Sort HR_BB array to show home run totals in second column
HR_BB_sort = player_array[player_array[:, 1].argsort()][::-1]

# Display the top three years and home run totals
print("Top Three Years with Most Home Runs by Barry Bonds:")
for i in range(3):
    Year = int(HR_BB_sort[i][0])
    HR = int(HR_BB_sort[i][1])
    print(f"Year: {Year}, Home Runs: {HR}")

        # Display the top three years and home run totals
    print(f"\nTop three years with the most Home Runs by {player}:")
    for i in range(3):
        Year = int(player_array_sort[i][0])
        HR = int(player_array_sort[i][1])
        print(f"Year: {Year}, Home Runs: {HR}")

import pandas as pd
import os

# CSV files to pull desired data
files = {
    "HA": "Hank Aaron Stats.csv",
    "BB": "Barry Bonds Stats.csv",
    "TC": "Ty Cobb Stats.csv",
    "WM": "Willie Mays Stats.csv",
    "SM": "Stan Musial Stats.csv",
    "AP": "Albert Pujols Stats.csv",
    "PR": "Pete Rose Stats.csv",
    "BR": "Babe Ruth Stats.csv",
    "HW": "Honus Wagner Stats.csv",
    "TW": "Ted Williams Stats.csv"
}

# Base directory path
#base_dir = r"C:\Users\zscon\Desktop\SSE_591\repo\SSE591_Week3\Week 3\Baseball Statistics"
base_dir = r"C:\Users\zscon\Desktop\SSE_591\repo\SSE591_Week3\Week 3\Baseball Statistics"

# List to store all the player DataFrames
player_dataframes = {}
all_player_dfs = []

# Load data for each player into a pandas DataFrame
for player, file_name in files.items():
    file_path = os.path.join(base_dir, file_name)
    player_df = pd.read_csv(file_path)
    # Drop rows with any missing values (empty cells)
    player_dataframes[player] = player_df.dropna()

# Accessing Ted Williams' information
print('Willie Mays stats without military status:\n',player_dataframes["WM"])
print('\nStan Musial stats without military status:\n',player_dataframes["SM"])
print('\nTed Williams stats without military status:\n',player_dataframes["TW"]) 

# Load data for each player into a pandas DataFrame
for player, file_name in files.items():
    file_path = os.path.join(base_dir, file_name)
    player_df = pd.read_csv(file_path)
    # Selecting columns "AB" to "RBI"
    selected_df = player_df.loc[:, "AB":"RBI"]
    # Summing the selected columns
    sum_result = selected_df.sum()
    # Transpose the DataFrame
    transposed_df = sum_result.to_frame().transpose()
    # Set the headers as the items in .loc slice
    transposed_df.columns = selected_df.columns
    # Replace the zero index with the player's name
    transposed_df.rename(index={0: player}, inplace=True)
    # Append the transposed DataFrame to the list
    all_player_dfs.append(transposed_df)

# Concatenate all the player DataFrames into one DataFrame
merged_df = merged_df.sort_values(by = "H",ascending=False)
print(merged_df)