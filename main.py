#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
from passwords import *

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.ny.gov", key)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("wujg-7c2s", limit=2000) # increase limit if you want more data

# Convert to pandas DataFrame
#results_df = pd.DataFrame.from_records(results)

# make sure to download matplot and numpy and import before using 
# import numpy as np
# import matplotlib.pyplot as plt
# all arguments should be strings
def plot_graph(data_set, x_values, y_values, title, x_label, y_label): 
    graph = data_set.plot(x=x_values, y=y_values)
    plt.xticks(rotation=70)
    graph.set_xticks(np.arange(len(data_set)))
    graph.set_xticklabels(data_set[x_values])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()