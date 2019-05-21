import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# SET YOUR LOCAL PATHS to be used later in the program
dataset_path = './crime.csv'
images_path = './stat_images/'

# read data and store them in a dataframe
df = pd.read_csv(dataset_path, engine='python')
print(df['SHOOTING'].head(10))
print(df.dtypes)
print(df.columns.values)

# drop not useful columns

print(df.shape)
# calculate the % of null values on each column
print(df.isnull().sum() / df.shape[0])

# display unique values of 'shooting' column
print(df['SHOOTING'].unique())
# replace nan values in 'shootings' columns with N
df['SHOOTING'].fillna('N', inplace=True)
print(df['SHOOTING'].unique())

year_group_df = df.groupby(['YEAR'])['INCIDENT_NUMBER'].count()
month_group_df = df.groupby(['MONTH'])['INCIDENT_NUMBER'].count()
day_group_df = df.groupby(['DAY_OF_WEEK'])['INCIDENT_NUMBER'].count()
distr_group_df = df.groupby(['DISTRICT'])['INCIDENT_NUMBER'].count()

print(year_group_df.sum())
print(month_group_df.sum())
print(day_group_df)
print(type(distr_group_df))
sns.set(style="darkgrid")
sns.barplot(year_group_df.index, year_group_df.values)
# plt.show()
plt.savefig(images_path + 'year.png')
