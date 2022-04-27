#%%

import matplotlib.pyplot as plt
import numpy as np
veriler = np.random.normal(27000,15000,10000)
veriler = np.append(veriler,[100000000000])
plt.hist(veriler,bins=50)
plt.show()
print(veriler.mean())
# %%
import os
import pandas as pd

dosya_yolu=os.path.join(os.getcwd(), "veri_madenciligi", "dmo.csv")
veri=pd.read_csv("dmo.csv")
veri.head(12)
# %%
