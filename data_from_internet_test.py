import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import urllib

dataLink = 'https://api.iextrading.com/1.0/stock/aapl/chart'
data = urllib.request.urlopen(dataLink)
data = data.read().decode("utf-8")
data = json.loads(data)
data = pd.DataFrame(data)
time = data['date']
open = data['open']
plt.plot(time,open)
plt.show()
