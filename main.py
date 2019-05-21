import pandas as pd
from plot_data import make_plot

# SET YOUR LOCAL PATHS to be used later in the program
dataset_path = './crime.csv'
images_path = './stat_images/'

# read data and store them in a dataframe
df = pd.read_csv(dataset_path, engine='python')
print(df.head(10))
print(df.dtypes)
print(df.columns.values)
print(df.shape)

# choose only useful columns
df = df[['INCIDENT_NUMBER', 'DISTRICT', 'SHOOTING', 'YEAR',
         'MONTH', 'DAY_OF_WEEK', 'HOUR', 'Lat', 'Long', 'Location']]

print(df.shape)
# calculate the % of null values on each column
print(df.isnull().sum() / df.shape[0])

# display unique values of 'shooting' column
print(df['SHOOTING'].unique())
# replace nan values in 'shootings' columns with N
df['SHOOTING'].fillna('N', inplace=True)
print(df['SHOOTING'].unique())

year_group = df.groupby(['YEAR'])['INCIDENT_NUMBER'].count()
month_group = df.groupby(['MONTH'])['INCIDENT_NUMBER'].count()
day_group = df.groupby(['DAY_OF_WEEK'])['INCIDENT_NUMBER'].count()
distr_group = df.groupby(['DISTRICT'])['INCIDENT_NUMBER'].count()

# change order of rows (based on week days order)
day_group = day_group.reindex(
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
print(day_group)

# make plots
make_plot(year_group, 'Year', 'Crime frequency',
          'Crime frequency by year', images_path, 'year.png')
make_plot(month_group, 'Month', 'Crime frequency',
          'Crime frequency by month', images_path, 'month.png')
make_plot(day_group, 'Day', 'Crime frequency',
          'Crime frequency by day', images_path, 'day.png')
make_plot(distr_group, 'District', 'Crime frequency',
          'Crime frequency by district', images_path, 'district.png')

# find in which year most shootings have occured
shootings_year_group = df.loc[df['SHOOTING'] == 'Y'].groupby(
    ['YEAR'])['INCIDENT_NUMBER'].count()
print(shootings_year_group)
print('Year with most shootings: ', shootings_year_group.idxmax())

# find in which district most shooting have occured
shootings_distr_group = df.loc[df['SHOOTING'] == 'Y'].groupby(
    ['DISTRICT'])['INCIDENT_NUMBER'].count()
print(shootings_distr_group)
print('District with most shootings: ', shootings_distr_group.idxmax())
