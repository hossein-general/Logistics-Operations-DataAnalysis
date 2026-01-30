import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import ipdb


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
mydict = {"col1":[1,5,9], "col2":[2,6,10], "col3":[3,7,11], "col4":[4,7,12]}
func = lambda x:"{:.2f}".format(float(x))
a1 = np.array([1,10,25,24,65])
# df=pd.read_csv(r"/mnt/Archive/data_analysis/s02/data1.csv")
df=pd.read_csv(r"/mnt/Archive/data_analysis/data/data1.csv")

insurance_data=pd.read_csv(r"/mnt/Archive/data_analysis/data/insurance.csv")   # from session 4
 
#region pandas
# ------------------------ pandas ----------------------------------
pd.__version__

df = pd.DataFrame(a,index=["A","B","C"],columns=["col1","col2","col3","col4"])
                                                        # creating a dataframe and giving each column a name. index: row indexes | columns: column indexes
                                                        # can be created with dictionary, which then will use the keys as the column name, and indexes rows from 0 to n-1. e.g.: df2 = pd.DataFrame(mydict, index=["A", "B", "C"])
s = pd.Series(a1,index=["a","b","c","d","e"])           # index will changes the row index from 0-n to defined names

country = pd.read_csv(r"/mnt/Archive/data_analysis/data/country.csv", header=1)       # reads data from a csv file, and imports them as a data frame. the header option defines which row holds data for the header (its usually 0, but in this case the first row is not a valid column name so we go with the second row (index 1))

pd.options.display.max_rows=7                           # makes pandas return maximum of 7 rows (e.g.: first 3 + last 3 + 1 middle that shows "....")
pd.set_option("display.max_rows", None)                 # disables the max_rows modification, returning all available rows on every call

pd.to_numeric(country["growth"], errors="coerce")       # it should be saved in the column. e.g.: country.["growth"] = pd.to_numeric(country["growth"], errors="coerce")       
                                                        # error options: coerce (replaces with NaN), raise(raises error (i think) in case of errors), ignore(ignores errors and doesnt do anythin with them, will be removed from pandas)

# added by me:
pd.to_datetime(customers["contract_start_date"], errors="coerce")   # similar to pd.to_numeric, but coerce option in "errors" return erros with NaT (not a time)

#endregion

#region DataFrame
# ------------------------ pandas.core.frame.DataFrame ----------------------------------
# pandas.core.series.Series
df.loc["A"]["col2"]                                     # returns the values stored in row "A" and column "col2"
df.loc[["A","B"],"col2"]                                # for multiple rows/columns. other ways: df.loc["A", "col2"]
                                                        # could assign values using: df.loc["A","col2"] = 5


df.iloc[0][3]                                           # returns the values stored in row index 0 and column index 3
df.iloc[[0,1],3]                                        # also allowed for multiple rows/columns
df.iloc[:,3]                                            # all rows and only column number 3
                                                        # in newer versions: df.iloc["A", "col2"]

df["col5"] = [8,88,888]                                 # if "col5" exists: changes the values (same number of items is necessary) | if "col5" doesnt exist: creates a new column with those values
                                                        # df.col5 is also allowed for calling a column

df.dtypes                                               # returns the data type for each column ("objects" are strings, as much as i know)
country.describe()                                      # what returns for "objects": count, unique, top, freq | for "float64": count, mean, std(enheraf meyar), min, 25%, 50%, 75%, max

df["col2"].apply(func)                                  # apply a function to all items of a datafram/column/...
df.astype(float)                                        # change the type of the dataframe/column/...
df.applymap("{:,.2f}".format)                           # applies a map, this is depricated and removed in newer versions
df.map("{:.2f}".format)                                 # applies a map (the new version for applymap)
df.drop("col4", axis=1, inplace=True)                   # removes a column/row from data frame. (inplace=True: applies the changes to the df itself, and doesnt return a copy of changes)growth
                                                        # country.drop(columns=["1","CountryCode"], inplace=True)
df.rename(columns={"col3":"column3"},inplace=True)      # rename (i need to investigate more on this)
                                                        # country.rename(index=country.CountryName, inplace=True)     # rename the entire indexing system of columns or rows with something else (here we passed a whole column to it, so each row index changes to the equivalant item in the column)
                                                        # country.rename(columns={"Population growth":"growth", "Total population": "total", "Area (sq. km)": "area"}, inplace=True)
df.replace(8,"arash",inplace=True)                      # replaces all items with a certain value and replaces them with the new specified value "Arash"

df.head(7)                                              # returns the first (7) rows of the data frame. (default value if not specified is 5)
df.tail(3)                                              # returns the last (3) rows of the data frame. (default value if not specified is 5)
df.sample(5)                                            # returns (5) random rows. no default value is defined

df.to_string()                                          # returns the whole thing in a string format, separating each row with backslash-n (\n)

df.ffill(inplace=True)                                  # fill the NaN values with the top value of that cell
df.bfill(inplace=True)                                  # fill the NaN values with the bottom value of that cell
df.dropna(inplace=True)                                 # remove all rows containling NaN values (added by me: it also applies to NaT (This can apply to Null , None , pandas. NaT , or numpy. nan .))
df.fillna(1000, inplace=True)                           # replaces all NaN values with the value (1000)
                                                        # could be applied on only one column:  df["Weight"].fillna(1000,inplace=True). but as the previous way is depricated, use this instead:
                                                        # df.fillna({"Weight":1000}, inplace=True)

df["Weight"].mean()                                     # returns the average value for the Weight column
df["Weight"].median()                                   # returns the median of the available values. e.g.: 1-3-6-7-10 --> median is 6
                                                        # if there where two values in the middle, it will return the average for the two middle ones. e.g.: 1-3-5-6-7-10 ---> median is (5+6)/2
df["Weight"].mode()[0]                                  # returns the most used value. (the 0 in braces indicates the rate of usage compared to other values, 0 means the most used, 1 means the second most used, ...). e.g.: 1-2-1-3-2-1 --> mode()[0] = 1


df["total"].max()                                       # returns the maximum value within a column

df.to_csv(r"/path/to/save/dataset_clean.csv")


df.groupby("sex")                                           # returns an object of type pandas.core.groupby.generic.DataFrameGroupBy, wich contains multiple tuples depending on the category given (in this case there will be 2 tuples (male and female)), which in each tuple there are two items: 1- a string showing the name of that category ("male" or "female" in this case) 2- a data frame containing all items falling into that group category (all males or all females) (type of data frames: pandas.core.frame.DataFrame)
                                                            # e.g.: average=insurance_data.groupby("sex")["charges"].mean()     # from session 4. pandas df.groupby(return an object of type pandas.core.groupby.generic.DataFrameGroupBy)
df.reset_index()                                            # from session 4. resets the indexing for a data frame. it will also insert the previous indexing array/series before the first column, and make it a part of data

df.index                    # if the indexing is from 0-n of type integer, it will return an object of type: pandas.core.indexes.range.RangeIndex, if not (like ["A", "B", "C"]), it could be of type: pandas.core.indexes.base.Index
df.columns                  # it may return an object of type: pandas.core.indexes.base.Index (i believe )


# operations
maxpop = df["total"].max()
df["total"][df["total"]==maxpop]                        # df["total"] returns a Series, which is a column, then we pass a boolean base Seires with the same indexing (returned by the operations df["total"]==maxpop, which checks each item in the df["total"] series, and fills them with true in case of being equal to the value stored in maxpop) and then only items with True values in the equivalant bool searies remain.
house[['Parking', 'Warehouse', 'Elevator']]             # returns a data frame object (pandas.core.frame.DataFrame). it also could have only one item selected, and will still be a dataframe e.g.: house[["Parking"]]


#endregion

# ------------------------------- Groupby items ----------------------------
df.groupby("sex")                                       # returns a groupby dataframe (pandas.core.groupby.generic.DataFrameGroupBy). (in data frames, they are of type: pandas.core.frame.DataFrame)
df.groupby("sex")["charges"]                            # returns a groupby series (pandas.core.groupby.generic.SeriesGroupBy)  (in serieses, they are of type: pandas.core.series.Series)
df.groupby("sex")["charges"].mean()                     # returns a Series (pandas.core.series.Series) containing mean values (average values) (when the function is used on a normal series, it returns a single number (like np.float64))




#region SimpleImputer
# ------------------------------- SimpleImputer ----------------------------------------

# TODO check what exactly SimpleImputer does
i = SimpleImputer(missing_values=np.nan, strategy="mean")
i.fit(df)
new = i.transform(df)
newdf=pd.DataFrame(new, index=df.index, columns=df.columns)



#endregion

# -----------------------------------------------------------------------------

# other python functions:
df.col1 = ["{:.2f}".format(float(i)) for i in df.iloc[:,0]]

name = "hossein"
age = 23
avg = 12.5
print(f"my name is {name}, Im {age} years old, my average is {avg:0.2f}")
# print(f"my name is {}, Im {} years old, my average is {:0.2f}".format(name,age,avg))          # check the error
print(f"my name is %s, Im %d years old, my average is %0.2f"%(name,age,avg))


ipdb.set_trace()
