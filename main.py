import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from interactive_map import make_map
from scipy import stats
from plot_data import make_plot
from kmeans import kmeans
from sklearn.cluster import KMeans


# SET YOUR LOCAL PATHS to be used later in the program
dataset_path = './crime.csv'
images_path = './stat_images/'

# read data and store them in a dataframe
df = pd.read_csv(dataset_path, engine='python')
print(df.head(5))
print(df.shape)

# choose only useful columns
df = df[['INCIDENT_NUMBER', 'OFFENSE_CODE', 'OFFENSE_CODE_GROUP', 'DISTRICT',
         'SHOOTING', 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR', 'Lat', 'Long', 'Location']]

print(df.head(5))

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
# drop rows with null 'DISTRICT' before grouping by district
distr = df.dropna(subset=['DISTRICT'])
distr_group = distr.groupby(['DISTRICT'])['INCIDENT_NUMBER'].count()

# change order of rows (based on week days order)
day_group = day_group.reindex(
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

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
print('Year with most shootings is ', shootings_year_group.idxmax())

# find in which district most shooting have occured
shootings_distr_group = df.loc[df['SHOOTING'] == 'Y'].groupby(
    ['DISTRICT'])['INCIDENT_NUMBER'].count()
print('District with most shootings is', shootings_distr_group.idxmax())

# add new series ('LIGHT) to dataframe that show if incident occured during the day or during the night
l = []
for i, val in df['HOUR'].iteritems():
    # if hour is between 6pm (18) and 6am (0) it's night, else it's day
    if (val >= 18) or (val <= 6):
        l.append('night')
    else:
        l.append('day')

new_ser = pd.Series(l)
df['LIGHT'] = new_ser

# find if most crimes were committed during the day or during the night
light_count = df.groupby(['LIGHT'])['INCIDENT_NUMBER'].count()
print('Most crimes were committed during the', light_count.idxmax())

# find most frequent type of crime during the day
light_group = df.loc[df['LIGHT'] == 'day'].groupby(
    ['OFFENSE_CODE_GROUP'])['INCIDENT_NUMBER'].count()
print('Most frequent type of crime during the day is', light_group.idxmax())

location = df[['Lat', 'Long']]
# drop nan values in location
location = location.dropna()
# remove outliers
location = location.loc[(location['Lat'] > 40) & (location['Long'] < -60)]
# make a scatterplot for crime locations
ax = sns.scatterplot(x='Long', y='Lat', data=location)
plt.title('Crime locations')
plt.savefig(images_path + 'scatter.png', bbox_inches="tight")
plt.show()

kmeans(location, images_path, 'kmeans2.png', 'KMeans with 2 clusters', 2)
kmeans(location, images_path, 'kmeans3.png', 'KMeans with 3 clusters', 3)
kmeans(location, images_path, 'kmeans5.png', 'KMeans with 5 clusters', 5)
kmeans(location, images_path, 'kmeans10.png', 'KMeans with 10 clusters', 10)

location = df[['Lat', 'Long', 'OFFENSE_CODE']]
# drop nan values in location
location = location.dropna()
# remove outliers
location = location.loc[(location['Lat'] > 40) & (location['Long'] < -60)]

kmeans(location, images_path, 'kmeansoffence2.png',
       'KMeans with 2 clusters and offence code', 2)
kmeans(location, images_path, 'kmeansoffence3.png',
       'KMeans with 3 clusters and offence code', 3)
kmeans(location, images_path, 'kmeansoffence5.png',
       'KMeans with 5 clusters and offence code', 5)
kmeans(location, images_path, 'kmeansoffence10.png',
       'KMeans with 10 clusters and offence code', 10)

location = df[['Lat', 'Long', 'MONTH']]
# drop nan values in location
location = location.dropna()
# remove outliers
location = location.loc[(location['Lat'] > 40) & (location['Long'] < -60)]

kmeans(location, images_path, 'kmeansmonth2.png',
       'KMeans with 2 clusters and month', 2)
kmeans(location, images_path, 'kmeansmonth3.png',
       'KMeans with 3 clusters and month', 3)
kmeans(location, images_path, 'kmeansmonth5.png',
       'KMeans with 5 clusters and month', 5)
kmeans(location, images_path, 'kmeansmonth10.png',
       'KMeans with 10 clusters and month', 10)

location = df[['Lat', 'Long', 'OFFENSE_CODE_GROUP']]
# drop nan values in location
location = location.dropna()
# remove outliers
location = location.loc[(location['Lat'] > 40) & (location['Long'] < -60)]
make_map(location, 'Larceny')
