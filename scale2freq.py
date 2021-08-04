import pandas as pd

scale2freq = {}

def set_scale():
    # read data from CSV file
    df = pd.read_csv("scale2freq.csv",header=0)
    # set dictionaly of scales and frequencies
    for i in range(df.shape[0]):
        scale2freq[df["Var"][i]] = df["Freq"][i]

if __name__ == "__main__":
    set_scale()
    for scale,freq in scale2freq.items():
        print("{} -> {}".format(scale,freq))