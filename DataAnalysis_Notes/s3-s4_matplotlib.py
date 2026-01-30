
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x=np.array([0,10])
y=np.array([10,100])
lesson=np.array(["python", "ML", "NLP", "deeplearning", "java script"])
number=np.array([1000, 850, 500, 380, 220])
mft=np.array([1000,850,500,380,220])
sharif=np.array([800,620,400,300,210])


#region fonts
# -------------------------- fonts ---------------------------------
font1 = {"famlily":"serif", "color":"bllue", "size":20}         # font families are in two groups: serif & sans serif. serif has broken lines in them, but sans serif fonts are smooth
font2 = {"famlily":"sans serif", "color":"red", "size":20}

#endregion

#region pyplt
# --------------------------- pyplot -----------------------------------
plt.figure(figsize=(5,5), dpi=100)                              # figsize: makes a 5 in 5 box to create the plot | dpi: dot per inch (the quality of the picture)
plt.subplot(1,2,1)                                              # 1st argument: number of rows | 2nd argument: number of columns | 3rd argumen: which picture (picture number ...). ** arguments could be separated with commas or could be concatenated into a single int. e.g.: plt.subplot(1,2,3) or plt.subplot(123). example:
                                                                #   plt.subplot(1,2,1)
                                                                #   plt.plot(lesson, mft, color="silver")
                                                                #   plt.subplot(1,2,2)
                                                                #   plt.plot(lesson, sharif, color="magenta")
                                                                #   plt.tight_layout()          # for adding some extra space between figures
                                                                #   plt.show()

plt.plot(x,y,"p-r", ms=20,mec="g", mfc="y", lw=3, ls="--", mew=3, marker="+", lw=3, color="silver")     # making a plot based on x and y. the "p-r" defines what kind of line will be used for drawing the plot, and what color it is ('p' means rounded, 'r' means red) | ms: marker size | mec: marker edge color ("g" means green) | mfc: marker face color ("y" means yellow) | lw: line width
                                                                # other options: ls: line style "--", ":" | mew: (marker edge width) | marker: (ther markers style) "*", "+" | lw: (line width)
                                                                # it could be used multiple times to make a diagram that contains multiple plots. e.g.: plt.plot(lesson, mft)  plt.plot(lesson, sharif)
                                                                # we could pass multiple arrays to get a single plot, but its advised to separate them to have more customisation over each one. e.g.: plt.plot(lesson, mft, sharif)
                                                                # in jupyter (?plt.plot) opens the help section for that module
plt.scatter(lesson, number)
plt.hist(number, bins=4)                                        # bins: number of groups to categorize the resaults in . bins 4 means separate the chart into 3 sections. (could be set to auto)
plt.pie(number, labels=lesson, explode=[0.05,0.05,0.05,0.05,0.05], autopct="%0.2f%%", wedgeprops={"edgecolor":"black", "linewidth":1})      # labesl: the array containing labels for the numbers | autopct: shows the numbers withing the pie chart, and enter the formatting for that | wedgeprops: edge properties, which are stored within a dictionary (edge color, linewidth)

plt.title("chart1", loc="left")                                 # its optional. by default is placed in the middle. loc: defines the location for the title
plt.xlabel("lesson", fontdict=font1)                            # a label for the x axis that shows the nme for that axis. fontdict is used for having fonts
plt.ylabel("number", fontdict=font2)
plt.yticks([1000,700,500,1200,150], ["1000m","700m","500m","1200m","150m"])     # marks some spots on the y axis of the plot and names each one with the given labels
plt.xticks(np.arange(0,200,10), rotation=90)                                         # rotates the labesl shown alongside the x axis. also the np.arange passed to the function defines that it should be showing labels alongside x axis starting from 10, and ending with 70, with the step of 2
plt.margins(0.7)                                                # adds margins from each side
plt.legend(["mft", "sharif"], loc="best")                       # the loc options (location) defines were the legend should be placed in on the picture
plt.annotate("mftpython", xytext=(0.5,500), xy=(0,900), arrowprops={"facecolor":"cyan", "width":2}, fontsize=10)        # if arrowprops wasnt passed, there will be no arrow drawn. xytext: is the location of the text itself, xy is the point of the arrow, the first argument is the text to be shown
for i in range(len(lesson)):
    plt.text(i, number[i], lesson[i])                           # writes text on the plot. the first parameter is x (i), the socond one is y (number[i]), the third one is the label (lesson[i])
plt.tight_layout()                                              # when using the plt.sublot, helps increasing the spacing between plots a little bit (making it look cleaner)
plt.show()                                                      # if not used for printing the plot, it will show an extra line at the top of the blot in jupyter. (is required in vscode to show, and in pycharm is required)

plt.savefig(r"/path/to/save/chart001.png", bbox_inches="tight")                      # could be set to jpg, or some other formats. bbox_inches: sets bounding box for the figure (it fixes the problem of some parts of picture beeing cropped)


# question: make each item appear on the plot on its point (this is my way, it should be tested):
# test = zip(lesson, number)
# for n,ln in enumerate(test):
#     plt.annotate("{}".format(ln[0]), xytext=(ln[1],n))




#endregion

# ------------------------------------------------------------------------


