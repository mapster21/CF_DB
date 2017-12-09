# Statisical analysis using Pandas.
# Run a section at a time to see results, both statistics and plots, clearly.
# ----------------------------------------------------------------------------------------------------

# Environment Set Up  
import matplotlib.pyplot as plt # might not need this
import pandas as pd
import seaborn as sns
import sys # Determine Python version number
import matplotlib # Determine Matplotlib version number
matplotlib.style.use('ggplot') # Use ggplot style plots*
from IPython import get_ipython # Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# ----------------------------------------------------------------------------------------------------
    
# Structure Data 
# Read in changes.csv, scrubbed output dataset from process_changes_with_object.py
Main_path = 'C:/13 DBS/PBD/CA4/' # Change as required to relevant path
Changes = pd.read_csv('C:/13 DBS/PBD/CA4/changes.csv') # Change as required to relevant path

# Create data frames (df)
df = pd.DataFrame(Changes)

# Display specific column for further inspection
df['author'] # Author contains mostly first names, one outlier seems to be an automated entry

# Explore df with descriptive statistics for each column
df['author'].describe() # 10 unique authors, Thomas authors 191 entries
df['revision'].describe() # 422 unique ID's - can be used as identifier
df['date'].describe() # 76 unique entries, most frequent (19)    
df['time'].describe() # 419 unique entry, only 1 has freq. 2
df['number_of_lines'].describe() # Returns a range of stats (count, mean, std, min, qrt, max)
df['comment'].describe() # 346 unique entries, top has frequency 24
df['comment1'].describe() # 21 unique entries
df['comment2'].describe() # Only 5 entry
df['comment3'].describe() # Only 1 entry
df['comment4'].describe() # Only 1 entry
df['comment5'].describe() # Only 1 entry
df[['author','date','time','revision']].describe() # Summary stats for all object types except comments

# Drop unuseful columns
df.drop(['revision','comment','comment1','comment2','comment3', 'comment4',
         'comment5'], axis = 1, inplace = True)

# Display header row plus number of lines specified to inspect data
df.head(2) # First 5 lines of data displayed 

# List data types by column in changes.csv
df.dtypes # All are objects except 'number-of_lines' which is integer (numeric)

# Check data shape
df.shape # 422 rows x 4 columns       

# Create data index
df.index # Data starts @ 0 and increments by 1 until it stops @ 422

# Column index list
df.columns # List of each column name as well as the predominant data type (object)

# Creates an array of all values in .csv
df.values # Shows the first and last 3 columns and 3 rows and ... between

# Descriptive statistics for numeric data values 
df.describe() # In this case just one column has numeric values:'number_of_lines'

# Transpose of descriptive statistics 
df.describe().transpose() # Presents statistics in a row

# Plot Numeric Data - various methods explored
df.plot() # needs numeric, plots all numeric data
plt.plot(df['number_of_lines']) # needs numeric, uses matplotlib
df['number_of_lines'].plot() # needs numeric, uses pandas (more intuitive)
df[['number_of_lines', 'author']].plot() # plot multiple columns, has to be a list within the df

# Plot Categorical Data
sns.countplot(y='author',hue='number_of_lines',data=df, palette="Greens_d") # Plots number of lines by author

# ---------------------------------------------1------------------------------------------------------

# 1. Author Analysis
# Create a table of counts for authors, then pass the counts to plot
author_table = pd.crosstab(index=df["author"], columns="count")
author_table # Counts for each author
author_table.to_csv('authorcount.csv') # Saves to .csv
author_table.describe() # Statistcs for number of author entries
author_table.plot(kind="bar", figsize=(8,8))

# Create new dataframe for author counts
Author = pd.read_csv('C:/13 DBS/PBD/CA4/authorcount.csv')
df1 = pd.DataFrame(Author)
df1

# Calculate % of total lines each author enters
df.describe() # total number of lines: count = 422
df1 # total number of lines per author e.g. Thomas: count = 191
df1['Total_Count'] = 422 # Add total number of lines to df1
df1['Percent_Total'] = df1['count']/df1['Total_Count']*100 # Calculate % & add as new column
df1['Percent_Total'] = ["%.2f" % elem for elem in df1['Percent_Total']] # Round to 2 decimal places
df1 # Result: Thomas wrote 45% of all lines

# Plot Results
fig1 = plt.figure()
plt.plot(df1['Percent_Total'])
plt.ylabel("% Revisions")
plt.xlabel("No. Unique Authors")
fig1.suptitle("Revision by Author")

# List author contribution as a percentage of total 
percentage = pd.crosstab(index=df1["Percent_Total"], columns=df1["Total_Count"])
percentage

# Plot as pie chart to display percentage distribution
var=df1.groupby(["author"]).sum().stack()
temp=var.unstack()
type(temp)
x_list = temp['count']
label_list = temp.index
plt.axis("equal") #The pie chart is oval by default. To make it a circle use plt.axis("equal")
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") #To show the percentage of each pie slice, pass an output format to the autopctparameter

# -----------------------------------------------2----------------------------------------------------

# 2. Date Analysis
# Create a table of counts for unique dates, then pass the counts to plot
date_table = pd.crosstab(index=df["date"], columns="count")
date_table # Counts of dates
date_table.to_csv('datecount.csv') # Saves to .csv

# Plots revision timeline
date_table.plot(kind="bar", figsize=(8,8), title=("No. Revisions by Date"))
plt.ylabel("Number of Revisions")

# Create new dataframe for date counts
Date = pd.read_csv('C:/13 DBS/PBD/CA4/datecount.csv')
df2 = pd.DataFrame(Date)
df2.sort_values('count') # sorts dates by revision count = popular dates for revisions
df2['count'].describe()
df2['Total_Count'] = df2['count'].sum() # Calculate total revisions and add as field to df2
df2['Percent_Total'] = df2['count']/df2['Total_Count']*100 # Calculate % & add as new column
df2['Percent_Total'] = ["%.2f" % elem for elem in df2['Percent_Total']] # Round to 2 decimal places
df2.sort_values('Percent_Total') # Result: 4.5% of revisions were made on 04/08/2015

# Plot Results
fig2 = plt.figure()
plt.plot(df2['Percent_Total'])
plt.ylabel("% Revisions")
plt.xlabel("No. Unique Dates")
fig2.suptitle("Revision by Date")

# Plot as pie chart to display date percentage distribution
var=df2.groupby(["date"]).sum().stack()
temp=var.unstack()
type(temp)
x_list = temp['count']
label_list = temp.index
plt.axis("equal") #The pie chart is oval by default. To make it a circle use plt.axis("equal")
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") #To show the percentage of each pie slice, pass an output format to the autopctparameter 

# ---------------------------------------------3------------------------------------------------------

# 3. Supervised V's Unsupervised Analysis
# A review of the author column indicates unsupervised revisions by author "/OU=Domain..."
# The remaining authors have at least a first name i.e. supervised revisions 
author_table # Counts for each author

# We will calculate the percentage of supervised v's unsupervised revisions using the merged df approach
# Merge df and df1(number of lines per author) 
# Add the count value for each authors entries to original
pd.merge(df, df1, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False) # Result: 422 rows x 5 columns
merge = pd.merge(df, df1, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
merge.drop(['time','date','number_of_lines'], axis = 1, inplace = True)
merge_table = pd.crosstab(index=df["author"], columns="count")
df3 = pd.DataFrame(merge_table)
df3

# Calculate % supervised and unsupervised
df3['Unsupervised'] = 24 # Add total number of lines to df3
df3['Supervised'] = df3['count'].sum() - df3['Unsupervised'] # Calculate sum and take away 
df3['Total'] = df3['count'].sum() # Calculate total
df3['Percent_U'] = df3['Unsupervised']/df3['Total']*100
df3['Percent_U'] = ["%.2f" % elem for elem in df3['Percent_U']] # Result: ~6% unsupervised
df3['Percent_S'] = df3['Supervised']/df3['Total']*100 
df3['Percent_S'] = ["%.2f" % elem for elem in df3['Percent_S']] # Result: ~94% supervised
df3

# Create new dataframe with just supervision values
dfnew = pd.DataFrame(columns=['Supervised','Unsupervised',], dtype='int64')
dfnew['Supervised'] = [94.31] # insert calcs from above
dfnew['Unsupervised'] = [5.69] # insert calcs from above
dfnew

# Bar plot to show the difference in values between revision methods
dfnew.plot(kind='bar', title ="Supervised V's Unsupervised", figsize=(10, 5), legend=True, fontsize=12)
dfnew.set_xlabel("Method", fontsize=12)
dfnew.set_ylabel("Revisions", fontsize=12)

# -------------------------------------------END------------------------------------------------------