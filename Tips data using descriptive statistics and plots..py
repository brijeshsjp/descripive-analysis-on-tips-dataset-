#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sources
# https://www.kaggle.com/code/sanjanabasu/tips-dataset
# https://www.angela1c.com/projects/tips-project/
# https://www.angela1c.com/projects/tips-project-files/part1/


# ## Describe the tips dataset using descriptive Statistics and plots

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[3]:


# cheking version of package
print("Numpy version",np.__version__)


# In[4]:


print("Pandas version:\n",pd.__version__,":\nSeaborn version:\n",pd.__version__,":\nMatplotlib version:\n",pd.__version__)


# In[5]:


# # setting print options with floating point: precisions=4, summarise ling arraya using thresold=5, supress small results=True 
# np.set_printoptions(precision=4, threshold=5, suppress=True)

# pd.options.display.max_rows=8 # setting max numbers of displays


# In[6]:


# Reading in Pandas

# import pandas as pd  # import pandas library

# csv_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'

# ## creata a DataFrame named df from reading in the csv file from a URL
# df =  pd.read_csv(csv_url)  ## creata a DataFrame named df from reading in the csv file from a URL


# In[7]:


#Reading in seaborn
df=sns.load_dataset("tips")

#printing head & tail rows
print("first 5 rows...:\n",df.head())
print("\nlast 5 rows...:\n",df.tail())


# The Tips dataset is a data frame with 244 rows and 7 variables which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant. In all the waiter recorded 244 tips. The data was reported in a collection of case studies for business statistics (Bryant & Smith 1995).[4] The waiter collected several variables: The tip in dollars, the bill in dollars, the sex of the bill payer, whether there were smokers in the party, the day of the week, the time of day and the size of the party.

# In[8]:


print("The index of the tips DataFrame: \n", df.index) # the index or row labels of the DataFrame


# In[9]:


print("The data-types in the dataframe are:", end='\n\n')
print(df.dtypes) # the data types attributes for each column in df
df.dtypes.value_counts() # types of variable 


# In[10]:


df['sex']=df['sex'].astype('category') # convert sex to be a categorical value
df['smoker']=df['smoker'].astype('category') # convert smoker to be a categorical value
df['day']=df['day'].astype('category') 
df['time']=df['time'].astype('category') 
print(*df.dtypes)


# In[11]:


# checking if there are any missing values, using * to save printing space

print(df.isna().any()) # isna returns boolean values 0 or 1, sum them to get count of NA's


# In[12]:


print("Top five tips: \n",df.sort_values(by='tip', ascending = False).head()) # sort by tip size and look at top 5 tip sizes


# In[13]:


print("Top three bills: \n",df.sort_values(by='total_bill', ascending = False).head(3)) # sort by total bill amount and then look at top 3 amounts


# In[14]:


# use pandas describe for the categorical variables in the dataframe
print("\nCharacteristics of the categorical variables:")
df.describe(include=['category'])


# In[15]:


# get summary statistics of the numerical values, 
df.describe() # get statistics summary of the tips dataframe df


# In[39]:


print("The mean bill amount is $%.3f" %df['total_bill'].mean(),"while the median bill amount is $%.3f" %df['total_bill'].quantile(q=0.5))
print("The mean tip amount is $%.3f" %df['tip'].mean(),"while the median tip is $%.3f" %df['tip'].quantile(q=0.5))
print(f"The mean bill amount is ${df['total_bill'].mean():.2f} ,while the median bill amount is ${df['total_bill'].quantile(q=0.5):.2f}")


# In[35]:


#Print Standard deviation and variance

print(f"The variance and standard deviations of Total Bill amounts are ${df['total_bill'].var():.3f} and ${df['total_bill'].std():.3f}")
print(f"The variance and standard deviations of tip amounts are ${df['tip'].var():.3f} and ${df['tip'].std():.3f}")
print(f"The variance and standard deviations of size are ${df['size'].var():.3f} and ${df['size'].std():.3f}")


# The standard deviation for total bill is quite high at almost 9 dollars but when the size of the party is taken into account this may not seem as large. (I will add a variable that shows the total bill per person).

# In[18]:


# the range of data
print("The minimum bill amount is $",df['total_bill'].min()," while the maximum bill amount is $", df['total_bill'].max(), " giving range of ",df['total_bill'].max() - df['total_bill'].min())
print("The minimum tip amount is $",df['tip'].min()," while the maximum tip amount is $", df['tip'].max(), "giving a range of ",df['tip'].max() - df['tip'].min())
print("The number of people in each dining party varies from",df['size'].min(),"to",df['size'].max(), "people" )


# In[19]:


#interquartile link
print("The median bill amount is ",df['total_bill'].quantile(q=0.5), "dollars and the median tip amount is", df['tip'].quantile(q=0.5),"dollars")
print(f"The total bill IQR is the range from {df['total_bill'].quantile(q=0.25):.2f} to {df['total_bill'].quantile(q=0.75):.2f}")
print(f"The tip IQR ranges from {df['tip'].quantile(q=0.25):.2f} to dollars {df['tip'].quantile(q=0.75):.2f}")


# The range of values for the bill amount is quite large varying between roughly 3 and 48 dollars while the tip amounts range from between 1 and 10 dollars. The interquartile range is closer to the mean values.

# In[20]:


#Countplot of Tables served by Day.
df.describe(include=['category'])


# In[21]:


#I will create a `day_order` to store the order in which to display the days on the plots.
day_order=["Thur", "Fri", "Sat","Sun"] # the order to be shown on the plot

# countplot showing the count of total_bill 
sns.set(style="ticks", palette="muted")

f, axes = plt.subplots(1, 2, figsize=(12, 4)) # set up 1 by 2 plot and figure size 12 by 4
# create a variable to store the order of days to show on the plots
day_order=["Thur", "Fri", "Sat","Sun"] # the order to be shown on the plot

# plot number of tables per day, added in time too
sns.countplot(x ="day",data =df, hue="time", palette=["teal","yellow"], order=day_order, ax=axes[0])
axes[0].set_title("Count of tables served by Day")

# plot number of  tables per day by size of party
sns.countplot(x =("day"), hue="size",data =df, ax=axes[1], order=day_order)
axes[1].set_title("Tables served by Day and by party size");

plt.show()


# •Fridays are the quietest days for this waiter. Saturdays are the busiest days followed by Sundays so there are more customers   at the weekend.
# 
# • The mosy common party size by far is 2. There are very few lone diners and very few parties of 5 and 6.

# In[22]:


# create a colour palette for plotting times
pal = dict(Lunch="seagreen", Dinner="gray")

# countplots by gender of bill payer and by smoker in the group
sns.set(style="ticks")

f, axes = plt.subplots(1, 2, figsize=(12, 4)) # set up 1 by 2 plot and figure size 12 by 4
order=["Thur", "Fri", "Sat","Sun"] # the order to be shown on the plot

# create a dictionary mapping hue level to colors (as per the FacetGrid plot!)
gender_pal=dict(Female="pink",Male="skyblue")
smoker_pal=dict(Yes="r",No="g")

# plot number of tables per day, use the palette as per the dict pal. specify the order of days on the axes.
sns.countplot(x ="day", hue="sex", palette=gender_pal,data =df, order=order, ax=axes[0])
axes[0].set_title("Count of tables served per day by sex of bill payer")

# plot number of  tables per day by size of party
sns.countplot(x =("day"), hue="smoker",data =df, ax=axes[1], palette=smoker_pal, order=day_order)
axes[1].set_title("Count of tables served per day with smoker(s) present");

plt.show() 


# •There are almost equal numbers of male and female bill-payers on Thursdays and Fridays but the number of male bill-player far out-weighs female bill-payers at the weekend.
# 
# •There are more non-smokers than smokers on any day but especially on Thursdays and Sundays. While there are much less customers recorded for Fridays than any other days, these customers are mostly smokers.
# 
# •There are almost equal number of male and female bill-paying customers for lunch but far more males for dinner. There are more male paying customers overall.

# ## Histogram and Kernel Density estimate plots of Total bill and Tip amount.

# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')

# set up the subplots and figure sizes
f, axes = plt.subplots(1, 2, figsize=(12, 4))

# plot the histograms of total bill amounts
sns.histplot(df['total_bill'], kde=True, ax=axes[0], color="blue", bins=25)
# add a vertical line at the mean
axes[0].axvline(df['total_bill'].mean(), color='yellow', linewidth=2, linestyle="--")
# add a vertical line at the median
axes[0].axvline(df['total_bill'].quantile(q=0.5), color='cyan', linewidth=2, linestyle=":")
# add a title
axes[0].set_title("Histogram of  Total Bill amounts")


#plot the histogram of tips
sns.histplot(df['tip'], kde=True, ax=axes[1], color="purple", bins=25)
# add a vertical line to show the mean
axes[1].axvline(df['tip'].mean(), color='yellow', linewidth=2, linestyle="--")
# add a vertical line to show the median
axes[1].axvline(df['tip'].quantile(q=0.5), color='cyan', linewidth=2, linestyle=":")
# add title
axes[1].set_title("Histogram of  Tip amounts")

plt.show()


# The histograms show that most total bill amounts fall in the range between 10 and 30 dollars with a peak around 16 dollars. It has only one peak when the default number of bins is used. As more bins are used you would expect to see more peaks in the distribution. The mean is the light yellow line and the median is the broken blue line. As the summary statistics above showed the median total total bill is about 2 dollars less than the mean indicating a non-symmetrical distribution. The mean and median tip amount are very close to each other. The distributions here do look slightly right skewed but you would expect not to see values near zero anyway for total bill amounts. The tips histograms shows that most tips fall in the range between 2 and 4 dollars with two distinct peaks at about 2.50 and 3.50.
# 
# The peaks of the kernel density estimates show which values have the highest priobability.

# ## Boxplots of Total Bill amounts and Tip amounts

# In[24]:


f, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.set(style="ticks", palette="pastel")
sns.boxplot(y=df['total_bill'], ax=axes[0], color="blue")

# add a title
axes[0].set_title("Boxplot of Total Bill amount")
sns.boxplot(y=df['tip'], ax=axes[1], color="purple")
axes[1].set_title("Boxplot of Tips amounts")


# The boxplots above shows similar information on the distribution of total bill and tip amounts as the distribution plots above. The rectangular boxes show the middle half of the distribution. The median bill amount is about 18 and the median tip amount is over 3 dollars. Total bills over 40 represent outliers while tips over 6 dollars are considered outliers. Boxplots can be used to compare distributions, often for one variables at different levels of another variable. I will look at this more in section 3 but for now will just look at the number of bills by day and by sex.

# In[25]:


sns.set(style="ticks", palette="pastel")

# set up 2 by 2 plots, overall figure size 12 by 4
f, axes = plt.subplots(1, 2, sharey=False, figsize=(12, 4))

# bill amount by day, grouped by sex
sns.set(style="ticks", palette="muted")
sns.boxplot(x="day",y="total_bill" ,data=df, order=day_order, ax=axes[0]) # controlling the day or
# bill amount by sex, grouped by smoking status
axes[0].set_title("Boxplot of total bill amount by day")
sns.boxplot(x="day",y="total_bill" ,hue="sex",data=df, palette=gender_pal,order=day_order, ax=axes[1]) 
# bill amount by dining time, grouped by sex
axes[1].set_title("Total bill amount by day by sex of bill payer")
sns.despine(offset=10, trim=True); # remove the spines


# # # Adding additional variables

# In[26]:


df['Tip%']=df['tip']/df['total_bill']*100
df['BillPP']=df['total_bill']/df['size']
df['TipPP']=df['tip']/df['size']
df['total_spent']=df['total_bill']+df['tip']
df.head()


# In[27]:


print(f"\nWhile the standard deviation of the total_bill amount was quite high at ${df['total_bill'].std():.2f}, the standard deviation of the bill per person seems more reasonable at ${df['BillPP'].std():.2f}\n")

print(f"This makes sense when the average (mean) bill per person is ${df['BillPP'].mean():.2f}.\n")
print(f"The tip amount as a percentage of the total bill amount is {df['Tip%'].mean():.2f} percent.\n")


# ## plotting the distribution of the bill per person and percentage tip rates.

# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
# set up the subplots and figure sizes
f, axes = plt.subplots(1, 2, figsize=(12, 4))

# plot the histograms of total bill amounts
sns.histplot(df['BillPP'], kde=True, ax=axes[0], color="blue", bins=25)
# add a vertical line at the mean
axes[0].axvline(df['BillPP'].mean(), color='yellow', linewidth=2, linestyle="--")
# add a vertical line at the median
axes[0].axvline(df['BillPP'].quantile(q=0.5), color='cyan', linewidth=2, linestyle=":")
# add a title
axes[0].set_title("Distribution of BillPP")

#plot the histogram of tip rate
sns.histplot(df['Tip%'], kde=True, ax=axes[1], color="purple", bins=25)
# add a vertical line to show the mean
axes[1].axvline(df['Tip%'].mean(), color='yellow', linewidth=2, linestyle="--")
# add a vertical line to show the median
axes[1].axvline(df['Tip%'].quantile(q=0.5), color='cyan', linewidth=2, linestyle=":")
# add title
axes[1].set_title("Distribution of  Tip percentages")


# ### The distribution of bill per person still seems to be a litle bit right skewed like the total bill distibution but less so and also it is less spread out. The distribution of the percentage tip is now distinctly unimodal. 
# 
# ### The plots below show the distributions of total bill and amount per person on the same plot.

# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="ticks", palette="muted")
# plot the histograms of total bill amounts and bill per person
sns.distplot(df['total_bill'], color="r", label="total_bill")
sns.distplot(df['BillPP'], color="c", label="Bill per person")
# add a title, set the x and y axis limits then plot the legends
plt.title("Total Bill amount and Bill per person")
plt.xlim(-5,50) 
plt.ylim(0,0.21)
plt.legend()
plt.show()


# ## Aside on Unique Tip amounts

# In[30]:


print(f"There are {len(df['total_bill'].unique())}  unique total bill amounts and {len(df['tip'].unique())}  unique tip amounts ")

# import stats module to use mode function
from scipy import stats

# Find the mode
mode= stats.mode(df['tip'])
print("The most common tip amount is ", *mode[0],"which occurs ", *mode[1],"times in the Tips dataset")
print(f"Tip of exactly 2 dollars occur {len(df[df.loc[:, 'tip'] ==2])} times") 
      
# use pandas isin function to check if the tip amounts are rounded
# create a set of tip values
values =[1.00,1.50, 2.00,2.50,3.00,3.50,4.00,4.50,5.00]
# get the count using len of how many tips fall into these range
print(f"For tips between 1 and 5 dollars there were {len(df[df['tip'].isin(values)])} rows where the tip was rounded to nearest 50 cent or dollar. \n")


# ## Summary plots of the Tips dataset

# In[31]:


# To just select the original variables of the dataframe and not included the added variables
df.loc[:, ['total_bill','tip','sex','smoker','size']];

print("\n\n Pairplot showing relationships between total bill, tip and size by sex of bill payer \n")

# plot the pairplot using palette defined earlier for hue levels
sns.pairplot(df.loc[:, ['total_bill','tip','sex','smoker','size']], hue="sex",palette=gender_pal)


# In[ ]:




