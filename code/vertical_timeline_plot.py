from datetime import date
from datetime import timedelta
from datetime import datetime
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
from pandas import json_normalize
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

###### Timeline#
chartdata = pd.read_csv(
    "data/Events.csv"
)

chartdata=chartdata.query('Year > 1939')
dates = pd.to_datetime(chartdata['Date_Clean_Approx'])
min_date = date(np.min(dates).year - 2, np.min(dates).month, np.min(dates).day)
max_date = date(np.max(dates).year + 2, np.max(dates).month, np.max(dates).day)

###
# "fake date" 
# Note: This is my solution to keeping the text labels from overlapping
#           and the plot from looking horrible. Instead of using actual
#           date values to accurrately reflect the time gap between 
#           events as gaps in the plot's 2-dimensional space, I simply
#           replaced the dates with evenly spaced integer values.

fake_d=np.c_[0:len(dates)]
labels = chartdata['Name']

# labels with associated dates
labels = ['{0:%d %b %Y}:\n{1}'.format(d, l) for l, d in zip (labels, dates)]

fig, ax = plt.subplots(figsize=(10, 28))#, constrained_layout=True)
_ = ax.set_xlim(-25, 25)
#_ = ax.set_ylim(min_date, max_date)
_ = ax.set_ylim(1, 98)
_ = ax.axvline(0, ymin=0.05, ymax=.985, c='deeppink', zorder=1)#ymax=0.95
#_ = ax.scatter(np.zeros(len(dates)), dates, s=120, c='palevioletred', zorder=2)
#_ = ax.scatter(np.zeros(len(dates)), dates, s=30, c='darkmagenta', zorder=3)
_ = ax.scatter(np.zeros(len(fake_d)), fake_d, s=120, c='palevioletred', zorder=2)
_ = ax.scatter(np.zeros(len(fake_d)), fake_d, s=30, c='darkmagenta', zorder=3)

#label_offsets = np.repeat(2.0, len(dates))
label_offsets = np.repeat(2.0, len(fake_d))
label_offsets[1::2] = -2.0


for i, (l, d) in enumerate(zip(labels, fake_d)): #dates
    #d = d - timedelta(days=90) 
    align = 'right'
    if i % 2 == 0:
        align = 'left'
    _ = ax.text(label_offsets[i], d, l, ha=align, fontfamily='serif', 
				fontweight='bold', color='royalblue',fontsize=11)#fontsize=12

#stems = np.repeat(2.0, len(dates))
stems = np.repeat(2.0, len(fake_d))
stems[1::2] *= -1.0    
#x = ax.hlines(dates, 0, stems, color='darkmagenta')
x = ax.hlines(fake_d, 0, stems, color='darkmagenta')

# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)

# hide tick labels
_ = ax.set_xticks([])
_ = ax.set_yticks([])
_ = ax.set_title('Alien and UAP (UFO) Milestones, 1940 - 2022', 
				 fontweight="bold", 
				 fontfamily='serif', 
				 fontsize=16, 
                 color='darkgreen')


# Add a footnote
ax.annotate('(c) 2022 AlienDB.org', xy = (-25, 1))
fig.tight_layout()

# Save or show plot
fig.savefig("matplotlib_tmp.jpg") 
plt.show()

