# Ozan Yetkin | 1908227
# Importing numpy for matrix operations
import numpy as np


# Define class for logistic regression
class LogisticRegression:
    # Initialize the class with self, learning_rate and number_of_iterations with default values
    def __init__(self, learning_rate=0.01, number_of_iterations=1000):
        # In order to make learning rate and number of iterations parametric, set them to provided input values
        self.learning_rate = learning_rate
        self.number_of_iterations = number_of_iterations
        # Initialize data_x and data_y as empty numpy matrices
        self.data_y = np.zeros((0, 0))
        self.data_x = np.zeros((0, 0))
        # Initialize bias as 0 and weight matrix as empty np matrix
        self.bias = 0
        self.weights = np.zeros((0, 0))
        # Initialize number of features and number of data (line count) as 0 (since there is no data yet)
        self.num_features = 0
        self.num_data = 0
        # Initialize costs as an empty list for each cost to be appended through iterations
        self.costs = []

    # Define a method to fit the model to the provided data, taking data_x and data_y as arguments
    def fit(self, data_x, data_y):
        # Set the number of data and number of features attributes according to the shape of given data_x matrix
        self.num_data = data_x.shape[0]
        self.num_features = data_x.shape[1]
        # Reinitialize the weights of the initial model according to number of features in the data
        self.weights = np.zeros(self.num_features)
        # Update the data_x and data_y attributes with the given data
        self.data_x = np.array(data_x, dtype=np.float64)
        self.data_y = np.array(data_y, dtype=np.float64)
        # Call train model method to update weights
        self.train_model()

    # Define update weights function to update weights in each iteration using formulas below
    # https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc
    def update_weights(self):
        # Retrieve x and y matrices from self.data_x and self.data_y
        x = self.data_x
        y = self.data_y

        # Calculate a = sigmoid(weight * x + bias), use sigmoid function defined outside class
        a = sigmoid_function(x.dot(self.weights) + self.bias)
        # Calculate cost = -y*log(a)-(1-y)*log(1-a), divide it to num of data to retrieve specific y from all data_y
        # https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148
        self.costs.append((-1/self.num_data)*(np.sum((y.T*np.log(a)) + ((1-y.T)*(np.log(1-a))))))
        # Calculate dl/dz = a - y, transpose y in order to subtract from a
        dl_dz = np.reshape((a - y.T), self.num_data)
        # Calculate dl/dw = (a - y).x, use dot product in order to multiply a - y with x
        dl_dw = np.dot(x.T, dl_dz)
        # Calculate delta_w = by dividing dl/dw with total number of data
        delta_w = dl_dw / self.num_data
        # Calculate delta_b = by dividing sum of dl/dz with total number of data
        delta_b = np.sum(dl_dz) / self.num_data

        # Update weights using formula new_weight = current_weight - learning_rate * delta_weight
        self.weights = self.weights - self.learning_rate * delta_w
        # Update bias using formula new_bias = current_bias - learning_rate * delta_bias
        self.bias = self.bias - self.learning_rate * delta_b

    # Define function to train model with the given data
    def train_model(self):
        # Iterate over number of iterations
        for i in range(self.number_of_iterations):
            # Call update weights method to update weights in each iteration
            self.update_weights()

    # Define predict method to predict the y values given x
    def predict(self, x):
        # Calculate predicted_y = sigmoid(weight.x + bias)
        predicted_y = sigmoid_function(x.dot(self.weights) + self.bias)
        # Turn the predicted_y values into either 0 or 1 in order to use for classification, use classify function
        # predicted_classes = classify(predicted_y)
        # Return predicted classes values
        return predicted_y


# Define sigmoid function to be used within the class
def sigmoid_function(x):
    # Calculate y = 1 / (1 + e^(-x))
    y = 1 / (1 + np.exp(-x))
    # Return the calculated y value
    return y


# Define classify method to convert predicted y values into either 0 or 1
def classify(y):
    # Initialize a matrix of zeros with the same shape as input y
    predicted_class = np.zeros(y.shape)
    # Iterate n times n being the shape of input y matrix
    for i in range(y.shape[0]):
        # Check if value of y is greater than 0.5
        if y[i] > 0.5:
            # If it is the case, set the predicted class to 1
            predicted_class[i] = 1
    # Return the predicted class matrix consisting of 0 or 1 values
    return predicted_class
