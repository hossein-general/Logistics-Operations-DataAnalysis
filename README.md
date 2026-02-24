<h1>Logistics Operations DataAnalysis</h1>

This project aims to analyze operational logistics data from a trucking company in order to evaluate financial performance, cost efficiency, and route-level profitability. The repository also temporarily contains personal Python notes from the MFT Data Analysis Course, which will be removed in future revisions to maintain a clean project structure. <br>
The dataset used in this analysis is available on Kaggle: <br>
https://www.kaggle.com/datasets/yogape/logistics-operations-database <br>
It represents a simulated yet realistic relational database of a Class 8 trucking company covering the years 2022–2024. The data includes interconnected tables for drivers, trucks, customers, routes, loads, fuel purchases, maintenance records, and performance metrics. Due to its multi-table relationships, financial transactions, and time-series structure, the dataset requires proper data modeling, joins, and analytical techniques to extract meaningful insights. Its relational design makes it well-suited for dashboard development, cost analysis, and profitability evaluation.


A database schema diagram illustrating the relationships between tables is as bellow: <br>
<img width="2389" height="1976" alt="Logistics Operations Database" src="https://github.com/user-attachments/assets/cdbd10ac-96c1-41f7-a3c9-f66883f317fa" />

https://dbdiagram.io/d/Logistics-Operations-Database-6976750ebd82f5fce28c51a8
The diagram was created using DBML (Database Markup Language).


<h2>Data Preparation Principles</h2>

**The following principles were applied during data preparation and transformation:**<br><br>
•	Categorical Encoding: Text-based categorical variables were converted into indexed numeric representations to reduce memory usage and improve grouping and join performance. <br>
•	Type Enforcement: Explicit data type assignments were applied to ensure consistency in calculations, comparisons, and time-based analysis. <br>
•	Referential Consistency: Shared attributes such as states and cities were consistently encoded across tables to maintain relational integrity and prevent mismatches during joins. <br>

<h2>Implementation Overview</h2>

**The analytical workflow was structured as follows:**<br><br>
•	Required Python libraries were imported and configured. <br>
•	A custom class was implemented to normalize operating hours by separating opening and closing times and generating a boolean flag for 24/7 operations. <br>
•	A utility class was developed to simplify inspection and descriptive output across all 13 dataframes. <br>
•	Pandas display settings were adjusted to improve readability during exploratory analysis. <br>
•	Relative file paths were prepared, and CSV files were loaded into structured dataframes. <br>
•	A reusable function was implemented to encode categorical columns and generate dictionary mappings for indexed values. These mappings were reused across multiple tables where applicable to reduce redundancy. <br>
•	A comprehensive data cleaning phase followed, including: <br>
> o	Enforcing appropriate data types for each column. <br>
> o	Normalizing operating hours into structured time columns to enable temporal analysis. <br>
> o	Encoding selected categorical columns to improve computational performance. <br>
> o	Handling missing values using appropriate strategies, primarily through controlled fillna() operations to preserve analytical flexibility. In cases where missing values were minimal and unlikely to impact results, selected rows were removed.


<h2>The reports are as below:</h2>

<h3>1- Total Revenue per Year</h3>

![report_01](https://github.com/user-attachments/assets/7f2c34e6-4db8-4178-b118-12ae3a2eec85)

Total annual revenue remains highly stable across the three-year period, fluctuating within a narrow range of approximately 86.9M to 87.9M. While 2023 shows a slight dip compared to 2022, revenue recovers in 2024, indicating no significant long-term growth or decline. This stability suggests consistent business volume, making profitability improvements more likely driven by cost efficiency rather than revenue expansion.

<h3>2- Total Revenue per Month</h3>

![report_02](https://github.com/user-attachments/assets/6abc27c8-76f5-4a38-8b38-2e1878e33951)

Monthly revenue remains consistently within the 6.5M–7.7M range across the entire period, showing moderate seasonality rather than volatility. Peaks commonly appear in mid-year months, while February tends to be one of the weaker months. The absence of extreme spikes or drops suggests stable operational demand and predictable freight volume. This consistency supports reliable planning for fleet utilization, staffing, and cash flow management, while also reinforcing that performance improvements are more likely tied to cost control than revenue growth.

<h3>3- comparision of revenue change over each month</h3>
This report was created to compare monthly revenue patterns across multiple years and identify seasonal trends or structural changes in business volume. It helps determine whether revenue fluctuations are part of normal seasonality or indicate meaningful shifts in overall performance.<br>

![report_03](https://github.com/user-attachments/assets/ea93ec3d-77b6-45ea-9da1-a052ca3dc79c)

The monthly revenue comparison across 2022–2024 shows a relatively stable revenue structure with moderate seasonal fluctuations rather than extreme growth or decline. Revenues consistently range between roughly 6.5M and 7.7M, suggesting operational stability and steady demand. Some seasonal tendencies appear, such as stronger performance in mid-to-late year months (particularly August 2022 and July 2023), while February tends to be one of the weaker months across years. Although there are minor year-to-year shifts within specific months, there is no clear long-term upward or downward revenue trend over the three-year period, indicating that overall business volume remained steady. This stability, combined with declining fuel costs observed earlier, suggests that profitability conditions may have improved over time even without significant revenue growth.

<h3>4- Average fuel cost in each year/month</h3>
this analysis shows the trends behind fuel cost change over time<br>

![report_04](https://github.com/user-attachments/assets/9d6a054e-1af2-46d1-9cab-2810207a9cdd)

The average fuel cost data shows a clear year-over-year decline, with 2022 averaging around 4.19–4.21 per month, dropping to approximately 3.84–3.86 in 2023, and further stabilizing around 3.64–3.66 in 2024. The most significant changes occur between years rather than within them, as monthly fluctuations inside each year are minimal, indicating price stability rather than volatility. This pattern suggests that broader market conditions drove fuel cost reductions over time, easing operational cost pressure after 2022. From a business perspective, this steady decline would likely improve profit margins and reduce fuel-to-revenue ratios, assuming revenue levels remained consistent, making 2024 the most favorable cost environment in the observed period.

<h3>5- Fuel Cost as % of Revenue (Financial Health Indicator)</h3>
Fuel is one of the largest variable expenses in trucking. This metric could tells us:<br>
- How heavy fuel expenses are relative to income<br>
- Whether rising fuel prices are eating into profits<br>
- How efficiently the fleet is operating<br>

![report_05](https://github.com/user-attachments/assets/416fb155-df0f-482f-8a1f-9a7a624d8a40)

The dataset shows that fuel expenses consistently represent a substantial portion of monthly revenue, ranging roughly from 33% to 40% over the three-year period. Early 2022 exhibits the highest ratios, reflecting elevated fuel prices, while the trend gradually declines through 2024 as fuel costs drop. This report highlights how fuel efficiency and cost management directly impact profitability, providing a clear operational KPI for monitoring financial health and identifying periods where fuel optimization could meaningfully improve margins.

<h3>6- Route Profitability Analysis</h3>
How much profit each route generates after subtracting fuel costs.<br>
Some routes look busy but barely profitable<br>
Some long routes may generate high revenue but burn too much fuel<br>
Some shorter lanes may be extremely efficient<br>

![report_06](https://github.com/user-attachments/assets/0e5bc714-bc3f-4341-8fee-4b26ccd02c94)

The analysis reveals that several long-haul routes generate exceptionally high profits, with the top lanes producing over 20M in net profit after fuel costs. Routes such as Seattle–Charlotte and Philadelphia–Seattle lead performance, indicating strong revenue generation combined with relatively controlled fuel expenses. Interestingly, while total revenues are fairly close among the top routes, differences in fuel cost levels slightly impact final profitability, highlighting the importance of cost efficiency even on high-revenue lanes.

A noticeable pattern is the frequent appearance of cities like Seattle, Charlotte, Columbus, and Portland among the most profitable routes, suggesting these locations function as strong demand hubs within the network. This insight can guide strategic decisions such as prioritizing equipment allocation, strengthening customer contracts in these corridors, or analyzing what makes these lanes structurally more profitable compared to others.

Terminology: <br>
MPG: MPG stands for miles per gallon and measures a vehicle's fuel efficiency by indicating how many miles it can travel on a single gallon of gasoline or diesel.


