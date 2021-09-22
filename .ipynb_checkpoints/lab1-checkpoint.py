import pandas as pb
import numpy as np

# If you want to use the csv from this git set
url = "https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/Lab1/stud.csv"
# You can also download the csv and set

df = pb.read_csv(url, sep=',')
df.head()
df = df.dropna()

df.isna().sum()
df = df.replace(r'^\s*$', np.nan, regex=True)

df['Column'] = df['Column'].astype(str).astype(float)

df.info()
