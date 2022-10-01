import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv("SpotifyFeatures.csv")
df = df.drop(columns=["artist_name", "track_name", "track_id"])

enc = OneHotEncoder(sparse=False, dtype=int)

y_data = enc.fit_transform(df[["genre"]])
x_data = df.drop(columns=["genre"])

x_cat_data = enc.fit_transform(x_data[["key", "mode", "time_signature"]])
x_cat_data = pd.DataFrame(x_cat_data, columns=enc.get_feature_names_out())
x_num_data = x_data.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])

x_data = pd.concat([x_num_data, x_cat_data], axis=1)

scaler = MinMaxScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)
# x_data = normalize(x_data, norm="max", axis=0)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train, y_train)

# TODO: https://stackoverflow.com/questions/38334296/reversing-one-hot-encoding-in-pandas

y_pred = neigh.predict(x_test)
y_test = pd.DataFrame(y_test).idxmax(axis=1)
y_pred = pd.DataFrame(y_pred).idxmax(axis=1)
cm = confusion_matrix(y_test, y_pred)

df_cm = pd.DataFrame(cm, range(27), range(27))
sn.set(font_scale=1.4)
sn.heatmap(df_cm, annot=True, annot_kws={"size": 27})

plt.show()
