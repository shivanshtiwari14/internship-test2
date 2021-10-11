import pandas as pd #importing_library
data = pd.read_csv("q1.csv") #importing_data
data.head()  #checking_the_data
data1 = data.groupby((data.Year//10)*10).sum() #grouping the_year_with_nearest_tenth_year
data1 = data1.drop("Year",axis=1) #dropping_the_extra_column_with_years_sum
data1.head() #checking_the_data
data1.to_csv("main1.csv") #converting_into_csv
