import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = pd.read_csv("Airlines.csv")

# flights.drop(["Unnamed"], axis=1, inplace= True)

x1 = list(flights[flights['name'] == 'United Air Lines Inc.']['arr_delay'])
x2 = list(flights[flights['name'] == 'American Airlines Inc.']['arr_delay'])
x3 = list(flights[flights['name'] == 'JetBlue Airways']['arr_delay'])
x4 = list(flights[flights['name'] == 'ExpressJet Airlines Inc.']['arr_delay'])
x5 = list(flights[flights['name'] == 'Delta Air Lines Inc.']['arr_delay'])

colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']

airlines = ['United Air Lines Inc.', 'American Airlines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.', 'Delta Air Lines Inc.']

plt.hist([x1, x2, x3, x4, x5], color = colors ,edgecolor = 'black', bins = int(180/20), label = airlines, normed= True)

# normed to normalize the graph
# to see different result put stacked = true, to see the stacked graph

plt.legend()
plt.set_title = ("side by side Histogram binwidth")
plt.set_xlabel = ('Delay Min')
plt.set_ylabel = ('Flights')
plt.show()

# single variable histogram with muplti binwidth

# for i, binwidth in enumerate([5, 10, 15, 20]):
#     ax = plt.subplot(2, 2, i+1)
#
#     # Using Matplot Lib
#     ax.hist(flights['arr_delay'], color = 'Blue',edgecolor = 'black', bins = int(180/binwidth))
#
#     # Using Seaborn Lib
#     # sns.distplot(flights['arr_delay'], hist= True, kde= False, bins=int(180/binwidth), color = "Blue", hist_kws={'edgecolor':'black'})
#
#     ax.set_title = ("Histogram binwidth = %d" % binwidth)
#     ax.set_xlabel = ('Delay Min')
#     ax.set_ylabel = ('Flights')
#     plt.show()
# plt.tight_layout()
