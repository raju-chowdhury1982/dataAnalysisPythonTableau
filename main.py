# Coronavirus Tracker Using Python Programming and Tableau
#def dataFrame: Data Frame is nothing but a heterogeneous two-dimentional tabular data structure

# phase-1 Data Collection by web scrapping
# phase-2 Data Cleaning
# phase-3 Data Storage
# phase1:
import pandas as pd
import requests

#api to fetch the dataFrame
url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
res = requests.get(url)

# print(res.content)
# print(res.__dict__)
# this res having all html, css and js all text it requires filtering data res.text get the data
data_list = pd.read_html(res.text)
# print(data_list[8])

target_df = data_list[8]
# print(target_df)
#phase2- issue1: columns name
target_df.columns = ["col0", "Country Name", "Total Cases", "Total Deaths", "Total Recoveries", "col5"]
# print(target_df)
#phase2- issue2: remove not required column i.e. extra columns
target_df = target_df[["Country Name", "Total Cases", "Total Deaths", "Total Recoveries"]]
#phase2- issue3: remove not required rows i.e. extra rows
last_row_ind = target_df.index[-1]
target_df = target_df.drop([last_row_ind, last_row_ind - 1])
# print(target_df)
#phase2- issue4: modify the country name by regEx
target_df["Country Name"] = target_df["Country Name"].str.replace('\[.*\]', '', regex=True)
#phase2- issue5: replacing No data cell with 0
target_df["Total Recoveries"] = target_df["Total Recoveries"].str.replace('No data', '0')
#phase2- issue6: convert the data type to number from string by to_numeric() from pandas
# target_df["Total Cases"] = pd.to_numeric(target_df["Total Cases"], errors='coerce').isnull()
# target_df["Total Deaths"] = pd.to_numeric(target_df["Total Deaths"],  errors='coerce').isnull()
# target_df["Total Recoveries"] = pd.to_numeric(target_df["Total Recoveries"], errors='coerce').isnull()
# print(target_df)
# phase3- export data into csv or xlsx file
# for csv
target_df.to_csv(r"covid19_dataset.csv")
# for xlsx
# target_df.to_excel(r"covid19_dataset.xlsx")
