import pandas as pd #importing_library
dataq3 = pd.read_csv("q3.csv") #importing data
dataq3.head() #checking the data
cards = dataq3[["Team", "Yellow Cards","Red Cards"]] #selecting the required columns
cards.sort_values(by=["Red Cards","Yellow Cards"]) #sorting the data based on requirement
cards.to_csv("main3.csv") #converting into csv
