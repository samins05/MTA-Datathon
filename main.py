#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("https://data.ny.gov/resource/wujg-7c2s.json", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("5f5g-n3cz", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

