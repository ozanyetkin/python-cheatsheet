import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix

df = pd.read_csv("SpotifyFeatures.csv")
df = df.drop(columns=["artist_name", "track_name", "track_id"])
row_index = df[df["genre"] == "A Capella"].index
df.drop(row_index, inplace=True)
df.reset_index(inplace=True)

enc = OneHotEncoder(sparse=False, dtype=int)

y_data = pd.get_dummies(df["genre"])
x_data = df.drop(columns=["genre"])

x_cat_data = enc.fit_transform(x_data[["key", "mode", "time_signature"]])
x_cat_data = pd.DataFrame(x_cat_data, columns=enc.get_feature_names_out())
x_num_data = x_data.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])

x_data = x_cat_data.join(x_num_data)

scaler = MinMaxScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)
# x_data = normalize(x_data, norm="max", axis=0)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7)

classifier = MLPClassifier(max_iter=1000)

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
y_pred = pd.DataFrame(y_pred, columns=y_test.columns).idxmax(axis=1)
y_test = y_test.idxmax(axis=1)
cm = confusion_matrix(y_test, y_pred)

df_cm = pd.DataFrame(cm, range(26), range(26))
sn.set(font_scale=0.4)
sn.heatmap(df_cm, annot=True)

plt.show()
