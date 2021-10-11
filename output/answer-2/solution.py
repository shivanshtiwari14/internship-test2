import pandas as pd #importing library 
dataq2 = pd.read_csv("q2.csv") #importing the data
dataq2.head() #checking the data
datagr = dataq2.groupby(by=["occupation"]).agg({"age":["max","min"]}) #grouping the data and using aggregate functions
datagr.head() #checking the output
datagr.to_csv("main2.csv") # converting into csv
