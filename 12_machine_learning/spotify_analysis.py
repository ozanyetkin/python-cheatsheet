import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("SpotifyFeatures.csv")
df = df.drop(columns=["artist_name", "track_name", "track_id"])

enc = OneHotEncoder(sparse=False, dtype=int)

y_data = df["popularity"]
x_data = df.drop(columns=["popularity"])

x_cat_data = enc.fit_transform(x_data[["genre", "key", "mode", "time_signature"]])
x_cat_data = pd.DataFrame(x_cat_data, columns=enc.get_feature_names_out())
x_num_data = x_data.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])

x_data = pd.concat([x_num_data, x_cat_data], axis=1)

scaler = MinMaxScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)
# x_data = normalize(x_data, norm="max", axis=0)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.7, random_state=7)

regressor = LogisticRegression(max_iter=1000, solver="liblinear")

regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

coefficients = regressor.coef_[0]
feature_names = list(x_num_data.head()) + list(x_cat_data.head())
for c, f in sorted(zip(coefficients, feature_names), key=lambda x: x[0]):
    print(f"Feature {f} has weight of {c}")

"""
plt.scatter(list(range(0, len(y_pred))), y_pred-y_test, s=0.01)
plt.show()
"""
"""
plt.scatter(list(range(i + 1)), errors, c="red")
plt.show()
"""
"""
for i in range(56):
    plt.scatter(x_test[50:100, i], y_test[50:100], c="blue")
    plt.scatter(x_test[50:100, i], y_pred[50:100], c="orange")
    plt.show()
"""

