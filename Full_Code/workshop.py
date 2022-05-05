import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

laptops = pd.read_csv('/Users/samraykhman/coding_projects/get_better_code/python_workshop/Cleaned_Laptop_data.csv')

# check the (rows, columns) of the dataset
laptops.shape

# familiarize with first 5 rows
laptops.head()

# familarize with last 5 rows
laptops.tail()

print(laptops.columns)

laptops.info()

laptops.describe()

# calling a specific column as series and using a method on the column
laptops['brand'].head()

# same thing as above line but now calling the column as a dataset instead of as a series
laptops[['brand']].head()

laptops['ssd'].count()

# creating a conditional for the dataset
condition = (laptops['brand'] == 'DELL')

laptops[condition]
laptops[laptops['brand'] == 'DELL']

laptops[laptops['star_rating'] >= 3.5]

laptops[(laptops['brand'] == "DELL") & (laptops['latest_price'] < 100000)]
laptops[(laptops['brand'] == "DELL") & (laptops['latest_price'] < 100000)].mean()

# GETTING RID OF DUPLICATE VALUES/ROWS
# laptops.drop_duplicates
# laptops.shape
laptops.drop_duplicates(inplace=True)
laptops.shape
## the dataframe would not be updated if you do not include the "inplace" attribute

# if i have a variable with a 'Missing' label. I will replace that value with a null type object.
# i then use a command to drop all the null values
zero_dict = {'Missing' : np.nan}
laptops['processor_gnrtn'] = laptops['processor_gnrtn'].replace(zero_dict)
laptops.dropna(inplace=True)

# BOXPLOT
fig, ax = plt.subplots(figsize=(6,4))

ax.boxplot(laptops['latest_price'])
ax.set_xticklabels(['latest_price'])
ax.set_ylabel('prices')

plt.show()

# HISTOGRAM
fig, ax = plt.subplots(figsize=(6,4))

ax.hist(laptops['latest_price'], bins=15)
ax.set_xlabel('prices')
ax.set_ylabel('Number of computers')

plt.show()

#creating a dataframe for each brand that I want and 
# filtering that dataframe to only have laptops by that brand
apple = laptops[laptops['brand'] == 'APPLE']
hp = laptops[laptops['brand'] == 'HP']
sams = laptops[laptops['brand'] == 'SAMSUNG']

# calculating the mean price of laptops per brand
apl_price = apple['latest_price'].mean()
hp_price = hp['latest_price'].mean()
sams_price = sams['latest_price'].mean()

#creating a bar graph with the info we just created
fig, ax = plt.subplots(figsize=(6,4))

ax.bar(['Apple', 'HP', 'Samsung'], [apl_price, hp_price, sams_price])
ax.set_xlabel('Brands')
ax.set_ylabel('AVG Laptop Price')
ax.set_title('Average Laptop Price per brand')

plt.show()


# interesting and efficient ways to group different data together.
# has capabilities for statistical inferences
laptops.groupby('brand')['star_rating'].mean()
laptops.groupby(['os', 'brand'])['latest_price'].mean()