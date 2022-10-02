import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db
df = pd.read_csv("SpotifyFeatures.csv")

df.drop(columns=["artist_name", "track_name", "track_id"], inplace=True)
# row_index = df[df["genre"] == "A Capella"].index
# df.drop(row_index, inplace=True)
df.reset_index(inplace=True)

enc = OneHotEncoder(sparse=False, dtype=int)
print(list(df["genre"].unique()))
labels = list(df["genre"].unique())
y_data = df["genre"].replace(labels, list(range(len(labels))))
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

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(8, activation='sigmoid'),
    tf.keras.layers.Dense(27)
])

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

model.compile(
              optimizer=opt,
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000)

test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])

y_pred = probability_model.predict(x_test)
y_pred = pd.DataFrame(y_pred, columns=y_test.columns).idxmax(axis=1)
y_test = y_test.idxmax(axis=1)
cm = confusion_matrix(y_test, y_pred)

df_cm = pd.DataFrame(cm, range(27), range(27))
sn.set(font_scale=0.4)
sn.heatmap(df_cm, annot=True)

plt.show()

report = classification_report(y_test, y_pred)
