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

now to the main reports
company financial performance
these charts show total company revenue over the given time span:
these are the 4 reports prepared for this purpose: 
1- comparision of revenue change over each month
This report was created to compare monthly revenue patterns across multiple years and identify seasonal trends or structural changes in business volume. It helps determine whether revenue fluctuations are part of normal seasonality or indicate meaningful shifts in overall performance.
<!-- TODO add picture -->
The monthly revenue comparison across 2022–2024 shows a relatively stable revenue structure with moderate seasonal fluctuations rather than extreme growth or decline. Revenues consistently range between roughly 6.5M and 7.7M, suggesting operational stability and steady demand. Some seasonal tendencies appear, such as stronger performance in mid-to-late year months (particularly August 2022 and July 2023), while February tends to be one of the weaker months across years. Although there are minor year-to-year shifts within specific months, there is no clear long-term upward or downward revenue trend over the three-year period, indicating that overall business volume remained steady. This stability, combined with declining fuel costs observed earlier, suggests that profitability conditions may have improved over time even without significant revenue growth.

2- Total Revenue per Year
<!-- TODO add picture -->
Total annual revenue remains highly stable across the three-year period, fluctuating within a narrow range of approximately 86.9M to 87.9M. While 2023 shows a slight dip compared to 2022, revenue recovers in 2024, indicating no significant long-term growth or decline. This stability suggests consistent business volume, making profitability improvements more likely driven by cost efficiency rather than revenue expansion.

3- Total Revenue per Month 
<!-- TODO add picture -->
Monthly revenue remains consistently within the 6.5M–7.7M range across the entire period, showing moderate seasonality rather than volatility. Peaks commonly appear in mid-year months, while February tends to be one of the weaker months. The absence of extreme spikes or drops suggests stable operational demand and predictable freight volume. This consistency supports reliable planning for fleet utilization, staffing, and cash flow management, while also reinforcing that performance improvements are more likely tied to cost control than revenue growth.

4- Average fuel cost in each year/month
this analysis shows the trends behind fuel cost change over time
<!-- TODO add picture -->
The average fuel cost data shows a clear year-over-year decline, with 2022 averaging around 4.19–4.21 per month, dropping to approximately 3.84–3.86 in 2023, and further stabilizing around 3.64–3.66 in 2024. The most significant changes occur between years rather than within them, as monthly fluctuations inside each year are minimal, indicating price stability rather than volatility. This pattern suggests that broader market conditions drove fuel cost reductions over time, easing operational cost pressure after 2022. From a business perspective, this steady decline would likely improve profit margins and reduce fuel-to-revenue ratios, assuming revenue levels remained consistent, making 2024 the most favorable cost environment in the observed period.

5- Fuel Cost as % of Revenue (Financial Health Indicator) 
Fuel is one of the largest variable expenses in trucking. This metric could tells us:
- How heavy fuel expenses are relative to income
- Whether rising fuel prices are eating into profits
- How efficiently the fleet is operating
<!-- TODO add picture -->
The dataset shows that fuel expenses consistently represent a substantial portion of monthly revenue, ranging roughly from 33% to 40% over the three-year period. Early 2022 exhibits the highest ratios, reflecting elevated fuel prices, while the trend gradually declines through 2024 as fuel costs drop. This report highlights how fuel efficiency and cost management directly impact profitability, providing a clear operational KPI for monitoring financial health and identifying periods where fuel optimization could meaningfully improve margins.

6- Route Profitability Analysis
How much profit each route generates after subtracting fuel costs.
Some routes look busy but barely profitable
Some long routes may generate high revenue but burn too much fuel
Some shorter lanes may be extremely efficient
<!-- TODO add picture -->
The analysis reveals that several long-haul routes generate exceptionally high profits, with the top lanes producing over 20M in net profit after fuel costs. Routes such as Seattle–Charlotte and Philadelphia–Seattle lead performance, indicating strong revenue generation combined with relatively controlled fuel expenses. Interestingly, while total revenues are fairly close among the top routes, differences in fuel cost levels slightly impact final profitability, highlighting the importance of cost efficiency even on high-revenue lanes.

A noticeable pattern is the frequent appearance of cities like Seattle, Charlotte, Columbus, and Portland among the most profitable routes, suggesting these locations function as strong demand hubs within the network. This insight can guide strategic decisions such as prioritizing equipment allocation, strengthening customer contracts in these corridors, or analyzing what makes these lanes structurally more profitable compared to others.

Terminology:
MPG: MPG stands for miles per gallon and measures a vehicle's fuel efficiency by indicating how many miles it can travel on a single gallon of gasoline or diesel.

Dataset from kaggle: https://www.kaggle.com/datasets/yogape/logistics-operations-database

