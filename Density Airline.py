import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights = pd.read_csv("Airlines.csv")

# flights.drop(["Unnamed"], axis=1, inplace= True)

airlines = ['United Air Lines Inc.', 'American Airlines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.', 'Delta Air Lines Inc.']

for airline in airlines:

    subplot = flights[flights['name'] == airline]
    sns.distplot(subplot['arr_delay'], hist= False, kde= True, kde_kws={'linewidth': 3}, label= airline)
    # sns.distplot(subplot['arr_delay'], hist= False, kde= True, kde_kws={'shade': True,'linewidth': 3}, label= airline)

# legend is to show labeling
plt.legend(prop = {'size': 16}, title = 'Airline')
plt.set_title = ("Density plot")
plt.set_xlabel = ('Delay Min')
plt.set_ylabel = ('Density')
plt.show()