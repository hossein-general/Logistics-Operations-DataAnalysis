import numpy as np
import pandas as pd
import matplotllib.pyplot as plt
import seaborn as sb

insurance_data=pd.read_csv(r"/path/to/insurance.csv")
house = pd.read_csv(r"/mnt/Archive/data_analysis/session 4 files/house.csv")

# some important notes: (check the "s2-s3-s4_pandas.py" file for a more in depth description on how it works)
average=insurance_data.groupby("sex")["charges"].mean()     # the chain of items returning: (insurance_data) a data frame ---( .groupby("sex") )--->  pandas.core.groupby.generic.DataFrameGroupBy ---( ["charges"] )---> pandas.core.groupby.generic.SeriesGroupBy ---( .mean() )---> pandas.core.series.Series
average=average.reset_index()                               # technically  we are resetting the indexes of a Series object


# --------------------------------- seaborn ----------------------------------
sb.scatterplot(x=insurance_data["bmi"], y=insurance_data["charges"], hue=insurance_data["sex"], palette="Set2")            # something like the plt.scatter(). the hue option colors each data with a different color based on the given category (for gender (sex) it would be 2 colors ). the palette kwarg accepts a pallet, to change the color for hue. (there are some predefined palletes available)
sb.regplot(x=insurance_data["bmi"], y=insurance_data["charges"])           # draws the line to show how much does the bmi affect the data
sb.lmplot(x=["bmi"], y=["charges"], hue=["smoker"], data=insurance_data)            # just like the sb.regplot() plot, but draws multiple lines for each category given by the hue parameter
sb.histplot(insurance_data["age"], bins=20, kde=True)       # bins can accept "auto" as an argument. kde: if set to true, will draw a line representing the changing flow
sb.boxplot(x="sex", y="bmi", data=insurance_data)           # the bottom line is the minimum, the top line is the maximum, the middle line is the q2 (half), the line under the q2 is q1 (1/4), and the line at the top of it is q3 (3/4). also the dots upper than the max line are the noisy data (box plot is one of the plots that can mark the noisy data)
sb.countplot(x="smoker", data =insurance_data, palette="viridis")               # generates a plot that shows the count of possibble option within the given column. look for the seaborn color palettes
sb.barplot(x="sex", y="charges", data=average)

# note:
plt.show()      # even though its from plt, it should be used in order to show the plot

sb.palplot(sb.color_palette())              # shows the colors of palettes
sb.palettes.SEABORN_PALETTES                # shows all available palettes



# ------------------------------------------------------------------------



