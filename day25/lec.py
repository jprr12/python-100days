# day 25 - working with CSV files and analyzing data with Pandas library

import pandas

# # reading CSV data with python
# # reading csv without pandas library
# weather_data = []
# with open('weather_data.csv', 'r') as data:
#     for item in data.readlines():
#         weather_data.append(item.strip())
# print(weather_data)

# # importing csv module instead
# import csv
# with open('weather_data.csv') as data:
#     raw_data = csv.reader(data) # reader() method can read csv files
#     # print(raw_data) # returns a reader object that programmers can loop through
#     temp = []
#     for row in raw_data: # looping through the object
#         print(row) # outputs a each line in the csv file as a list. 
#         # number of lines in csv file = number of lists
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

# # using pandas library
# # opening csv file with panda
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print("\n")
# # saving a column of data in the csv labeled temp in a variable temp
# temp = data['temp']
# same_temp = data.temp # different way of calling a column in a csv file
# print(temp)
# print(same_temp)

# ==============================================
# # data frames and series - working with rows and columns

data = pandas.read_csv('weather_data.csv')
# print(type(data)) # returns data frame
# print(type(data['temp'])) # returns series
# # check pandas API references for more info

# # converting csv file to dictionary
# data_dict = data.to_dict()
# print(f"Data in dictionary: {data_dict}")

# # convert csv column to list
# temp_list = data['temp'].to_list()
# print(f"Temperatures: {temp_list}")
# # now that the series is converted to a list, you can now perform list operations
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 1))

# # statistical methods with pandas
# print(round(data['temp'].mean(), 2)) # returns the mean/average of a data column
# print(data['temp'].max()) # returns the max value in a data column
# print(data['temp'].median()) # returns the median in a data column
# print(data['temp'].min()) # returns the min value in a data column

# # getting all data in a column through a csv label
# print(data.day)
# print(data.temp)
# print(data.condition)

# # getting all data in a row through an instance of data in the csv
# mon_data = data[data.day == 'Monday']
# print(mon_data)
# sunnny_data = data[data.condition == 'Sunny']
# print(sunnny_data)

# # getting the data from weather_data where temp was highest
# print(data[data.temp == data.temp.max()]) # returns data frame
# print(data.temp.max()) # returns the max temp in weather_csv

# # returning a row as a data frame
# mon_data = data[data.day == 'Monday']
# print(mon_data.condition) # returns the condition in the monday row

# # convert monday temp to fahrenheit
# monday_og_temp = int(mon_data.temp) # converting directly to int will return future warning
# print(monday_og_temp)
# # do this insead to convert series to int
# monday_temp = int(mon_data.temp.iloc[0])
# F_monday_temp = monday_temp * 9/5 +32
# print(F_monday_temp)

# # converting all temp from weather_data to fahrenheit
# temp = data.temp.to_list()
# i = 0
# for t in temp:
#     new_temp = t * 9/5 + 32
#     temp[i] = new_temp
#     i += 1
# print(temp)

# # create a data frame from a python dictionary
# sample_data = {
#     'students': ['sheldon', 'amy', 'leonard', 'bernadette'],
#     'scores': [99, 95, 92, 94]
# }
# df = pandas.DataFrame(sample_data) # turns a data structure into a data frame
# print(df)
# df.to_csv('sample_data.csv') # creates a csv file after running code

# ==============================================
# data analysis with pandas challenge
# open squirrel_data
data = pandas.read_csv('squirrel_data.csv')
# count the total number of squirrels based on color
greys = len(data[data['Primary Fur Color'] == 'Gray'])
blacks = len(data[data['Primary Fur Color'] == 'Black'])
reds = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(len(data))
# create a csv of the squirrel color data
squirrel_count = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [greys, blacks, reds]
}
sc_data = pandas.DataFrame(squirrel_count)
print(sc_data)
sc_data.to_csv('squirrel_count.csv')

