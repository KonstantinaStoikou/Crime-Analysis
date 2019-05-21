import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# SET YOUR LOCAL PATHS to be used later in the program
dataset_path = './crime.csv'
images_path = './stat_images/'

# read data and store them in a dataframe
df = pd.read_csv(dataset_path, engine='python')
print(df.head(10))
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

print(year_group_df)
print(month_group_df)
print(day_group_df)
# change order of rows (based on week days order)
day_group_df = day_group_df.reindex(
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
print(day_group_df)

# make plots
sns.set(style="darkgrid")

norm = plt.Normalize(0, year_group_df.values.max())
colors = plt.cm.Blues(norm(year_group_df.values))
ax = sns.barplot(year_group_df.index,
                 year_group_df.values, palette=colors)
ax.set(ylabel='Crime frequency', xlabel='Year')
plt.title('Crime frequency by year')
plt.savefig(images_path + 'year.png', bbox_inches="tight")
plt.close()

norm = plt.Normalize(0, month_group_df.values.max())
colors = plt.cm.Blues(norm(month_group_df.values))
ax = sns.barplot(month_group_df.index,
                 month_group_df.values, palette=colors)
ax.set(ylabel='Crime frequency', xlabel='Month')
plt.title('Crime frequency by month')
plt.savefig(images_path + 'month.png', bbox_inches="tight")
plt.close()

norm = plt.Normalize(0, day_group_df.values.max())
colors = plt.cm.Blues(norm(day_group_df.values))
ax = sns.barplot(day_group_df.index,
                 day_group_df.values, palette=colors)
ax.set(ylabel='Crime frequency', xlabel='Day')
plt.title('Crime frequency by day')
plt.savefig(images_path + 'day.png', bbox_inches="tight")
plt.close()
