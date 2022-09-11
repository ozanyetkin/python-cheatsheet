import pandas as pd

df = pd.read_csv("SpotifyFeatures.csv")
y_data = df["popularity"]
x_data = df.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])
