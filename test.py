import pandas as pd


arr = [2,3,4,5,6,7,7]

ds = pd.Series(arr)

print(ds)

lrr = list(ds)

print(type(lrr))
