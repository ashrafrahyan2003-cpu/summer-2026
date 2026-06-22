import pandas as pd

data = [100, 2020, 20202]

series = pd.Series(data, index = ["a", "b", "c"])

print(series)

series.loc["c"] = 200
print(series.loc["c"])


data2 = {"Fruit1":"Orange", "Fruit2":"Apple", "Fruit3":"Mango", "Fruit4":"Pineapple", "Fruit5" : "Pear"}
series2 = pd.Series(data2)
print(series2)