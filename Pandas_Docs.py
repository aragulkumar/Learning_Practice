import pandas
# this is a placeholder for the pandas documentation
mydataset = {
    "car": ["BMW", "Volvo", "Ford"],
    "passings": [3,7,2]
,}
myvar = pandas.DataFrame(mydataset)
print(myvar)


# mostly we use alias pd for pandas import
import pandas as pd 
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

# To check the version of pandas installed
print(pd.__version__)

# how to use series in pandas
a = [1,11,5,9]
myvar = pd.Series(a)
print(myvar)

# Output:
# 0     1
# 1    11
# 2     5
# 3     9

# labels
print(myvar[0])

# Output:
# 1

# Create labels 
a = [11,22,33,44]
myvar = pd.Series(a, index=["a","b","c","d"])
print(myvar)

# Output:
# a    11
# b    22
# c    33
# d    44

print(myvar["a"])

# Output:
# 11

# Key/Value pairs as Series
calories = {
    "day1": 420,
    "day2": 350,
    "day3": 300,
}

myvar = pd.Series(calories)
print(myvar) #Keys of the dictionary become the labels of the series

# Output:
# day1    420
# day2    350
# day3    300

# Return values using index
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

# Output:
# day1    420
# day2    350

# create a DataFrame from a series
data = {
    "calories": [420,350,300],
    "duration": [50,40,45],
}
myvar = pd.DataFrame(data)
print(myvar)
# Output:
#    calories  duration
# 0       420        50
# 1       350        40
# 2       300        45


