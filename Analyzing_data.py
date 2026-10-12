import pandas as pd

a = pd.read_csv(r"C:\Users\user\Downloads\archive (12).zip")
print(a.head(10))
print("::"*50)
print(a.tail(10))
print("::"*50)
print(a.info())
print("::"*50)

empty_a = a.dropna(inplace = True)#empty cells = a.dropna() and inplace = true will replace original data with new dataframe
print(empty_a)

fill_a = a.fillna(0, inplace = True)# fillna is used to fill that empty data with some value or data
print(fill_a)
print("::"*50)
print(f"Average age is {a["Age"].mean()}")
print(f"Median age is {a["Age"].median()}")
print(f"Mode or most frequent age is {a["Age"].mode()[0]}")
print("::"*50)
remove_row_a = a.dropna(subset = ["Age"], inplace = True)#remove row which has null value
print(remove_row_a)

print(a.corr())





