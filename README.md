<!-- TODO: recheck the whole readme sectoin with chatgpt -->
this project aims to analyze logistic data from a trucking company
this git repository also holds data for python notes which were writen from MFT DataAnalysis Course i completed lately, and will be removed in later commits

dataset link: https://www.kaggle.com/datasets/yogape/logistics-operations-database
This dataset represents a simulated but realistic operational database of a Class 8 trucking company covering three years (2022–2024). It includes interconnected tables for drivers, trucks, customers, routes, loads, fuel purchases, maintenance, and performance metrics
Because it contains multi-table relationships, financial transactions, and time-series operational data, it requires proper data modeling, joins, and analytical techniques to extract insights. Its structure makes it a strong choice for building dashboards, performing cost and profitability analysis, and demonstrating real-world logistics analytics skills rather than basic descriptive reporting.

this diagram shows the relations between 
<!-- TODO: i should add the image of the diagram here, using an image hosting service -->
link to the diagram: https://dbdiagram.io/d/Logistics-Operations-Database-6976750ebd82f5fce28c51a8
the markup language used to create this diagram is DBML

A number of principles followed in this report for transfering data:
- categorical encoding: Converting text categories into numeric representations reduces memory usage and speeds up comparisons, grouping, and joins.
- type enforcement: Explicitly enforcing data types prevents unexpected behavior in calculations, comparisons, and time-based operations.
- referential consistency: Ensuring consistent encoding of shared attributes (e.g., states or cities) preserves integrity across joins and prevents relational mismatches.

allow me to walk you through what ive done within this report:
first i imported some packages and libraries. (you can tell me to add any other library and i will add them too for my reports)
- then i craeted a class that ill later be using for splitting certain columns cotaining open and close time, which putting it simple, has to get the dataframe itself, and perform some operations on it to separate start time from end time, and generate a column containing a boolean flag for companies that are open 24/7
- then there is a PrintClass class, which is kind of a debugging toll for me. it helps me print some descriptions for all 13 dataframes i have easier.
- there are some modifications in the display setting of pandas
- preparing the relative path
- then I'll be reading the csv files containing data for each table
- also there is function which categorizes items within a column, gives each one an integer index for better performance. it will be used for the cleaning section (next part)
- then there is this huge section, trying to transfer data and cleaning them, by changing each columns data type to what it should be, and applying some changes in some of them in order to improve the performance 
** Operating hours were normalized into structured time columns to enable temporal performance analysi
** some columns data will be categorized and indexed in order to improve performance, in these cases there are some variables included and named based on the dataframeName_columName which contain the dictionary showing what each index represents in that column
** some of these dictionaries are used across multiple dataframes which will help reducing redundant data (like state names, city names, etc.)
- after preparing data types and indexing them, we will deal with nan and nat data within each dataframe. comments in this section represent the mindset i had behind what i did
** i mostly used the fillna option and filled nan data with a placeholder so i can prepare some reports on that nan data itself, also some of na values are kept, and there is one case i droped rows with nan values as i think i had a reach amount of data within that dataframe and an small amount of nan values will not matter that much
- then there is this simple report i created as a test. 

prepared reports:
the first section of this report focuses on the company financial performance
there charts show total company revenue over the given time span:

these are the 4 reports generated: 
1- comparision of revenue change over each month
2- revenue per year
3- revenue per month

the resaults are quite self explanetory:
the company experienced a gap in company income.
also the company usually experiences the least revenue in February


Dataset from kaggle: https://www.kaggle.com/datasets/yogape/logistics-operations-database

