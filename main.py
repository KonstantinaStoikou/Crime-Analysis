import pandas as pd

# SET YOUR LOCAL PATHS to be used later in the program
dataset_path = './crime.csv'

col_names = []
# read data and store them in a dataframe
# train_df = pd.read_csv(dataset_path, engine='python', sep='\t+',
#                        names=col_names)
df = pd.read_csv(dataset_path, engine='python')
print(df['OFFENSE_CODE_GROUP'].head(10))
