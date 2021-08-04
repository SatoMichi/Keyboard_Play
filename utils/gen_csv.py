import pandas as pd
import re

df = pd.read_csv("../scale2freq.csv",header=0)

for i,scale in enumerate(df["Scale"]):
    df["Var"][i] = scale.replace("#","s")

df.to_csv("scale2freq.csv")