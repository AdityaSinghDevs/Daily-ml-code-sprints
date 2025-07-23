import pandas as pd

path  = "/Titanic.csv"

df = pd.read_csv(path)

# parameters and their defaults are [sep : ',' (separation in file)], [header: first row (which row of file contains column names)], [skiprow : allows to skip specific number of rows at beginning of the file, useful for excluding header rows], [skipfooter : same but for end] , [on_bad_lines : Indicates course of action when encountering a line containing too many fields]

#exploring data 
df.head() # displays firts few(default 5 rows of Df)
df.tail() # same for end
df.shape() #returns number of rows and columns
df.describe() #Heneratess summary stats for numeric columns

#missing data handled
#for detection of missing values 
df.isna() # df.isna().sum().... will return sum for each column
df.notna()

#handling
df.dropna()
df.fillna() # df["column_1"].fillna("No Data").... will fill in with this text at all missing places

#saving data to a csv
# once data is worked upon using dataframes, it is ready for export in csv
df.to_csv() # Prameters ["filneame.csv"] , [index : write row names(index) default true], [mode : "W" to truncate the file first, "x" exclusive creation, failing if the file lready exists, "a" append to end of file if exists]




