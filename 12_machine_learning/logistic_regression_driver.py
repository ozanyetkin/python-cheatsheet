# Ozan Yetkin | 1908227
# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# Import LogisticRegression class from the LogisticRegression.py
from logistic_regression import LogisticRegression

# Define a function to read the data from provided text files, get file name from the user
def read_input_file(file_name):
    # Open the file with provided file name input
    with open(file_name) as file:
        # Use read lines method to handle multiple lines
        lines = file.readlines()
        # Close the file after reading process finished
        file.close()
    # Return the lines to be handled with another function
    return lines

# Define a function both to convert strings provided in dataset and handle missing data
def convert_data(input_data):
    # Use try except to handle value error since not every data can be converted to float
    try:
        # If the data can be converted into a float without an error, convert it to float
        converted_data = float(input_data)
    # If conversion from string to float fails, catch the error and enter except state
    except ValueError:
        # If conversion fails, check the possibilities one by one; first check if it is equal to "yes"
        if input_data == "yes":
            # If it is the case, set the converted data to True (which can also be evaluated as 1)
            converted_data = True
        # Check the possibilities one by one; check if it is equal to "no"
        elif input_data == "no":
            # If so, set the converted data to False (which can also be evaluated as 0)
            converted_data = False
        # Check the possibilities one by one; check if it is equal to "NA"
        elif input_data == "NA":
            # If so, set the converted data to pandas NA (which is pandas equivalent to None)
            converted_data = pd.NA
        # If none of the possibilities above occur, enter else state
        else:
            # Leave the data as it is, code will enter this state for names, which will inevitably be a string
            converted_data = input_data
    # Return whatever the converted data is
    return converted_data

# Define a function to convert dataset lines into pandas dataframe, take lines as input
def convert_to_dataframe(lines):
    # Initialize an empty list for raw data
    raw_data = []
    # Iterate through lines provided in the input
    for line in lines:
        # Remove newline characters and quotes in each line, then split the items with space character
        line = line.replace("\n", "").replace("\"", "").split(" ")
        # Convert each item in row using convert data function above, use list comprehension to create another list
        data = [convert_data(ln) for ln in line]
        # Append the list consisting of converted data for each row to main raw data list
        raw_data.append(data)
    # Separate the headers from raw data list by taking the first row, prepend "name" since it is missing in dataset
    headers = ["name"] + raw_data[0]
    # Separate genie data from raw data list by taking all rows except the first row
    genie_data = raw_data[1:]
    # Construct the dataframe using pandas dataframe class, pass genie data as data itself and headers as columns
    dataframe = pd.DataFrame(genie_data, columns=headers)
    # Return the constructed dataframe
    return dataframe

# Define a function to normalize the values in dataframe, take dataframe and normalization method as input
# This is used since using the dataframe as it is caused overflows and zero divisions logistic regression
def normalize_dataframe(dataframe, method="mean"):
    # https://stackoverflow.com/questions/26414913/normalize-columns-of-pandas-data-frame
    # Check if the requested normalization method is mean normalization
    if method == "mean":
        # If it is the case, calculate normalized dataframe by (original - mean) / standard deviation
        normalized_dataframe = (dataframe - dataframe.mean()) / dataframe.std()
    # Check if the requested normalization method is min-max normalization
    elif method == "minmax":
        # If it is the case, calculate normalized dataframe by (original - min) / (max - min)
        normalized_dataframe = (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())
    # If none of the cases above fits the situation, enter the else state
    else:
        # Inform the user that requested method is not defined and leave the dataframe as it is
        print("Unknown method requested for normalization")
        normalized_dataframe = dataframe
    # Return the normalized version of the dataframe
    return normalized_dataframe

# Initialize the training lines and test lines by calling read input file function with provided files
training_lines = read_input_file("data_ready_for_ML_GENIE.txt")
test_lines = read_input_file("data_ready_for_ML_TCGA.txt")

# Convert the lines to dataframe both for training and test sets by using convert to dataframe function above
training_dataframe = convert_to_dataframe(training_lines)
# Use fill na method of pandas since test set contains NA values, use the pad method for filling
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
test_dataframe = convert_to_dataframe(test_lines).fillna(method="pad")

# Initialize the training x data by masking name and driver mutation labels, normalize the dataframe with mean method
x_train = normalize_dataframe(training_dataframe.iloc[:, 1:-1], method="mean")
# Initialize the training y data by only getting the driver mutation labels, use replace method to convert strings
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
y_train = training_dataframe.iloc[:, -1].replace({"driver": 1, "passenger": 0})

# Initialize the test x data by masking name and driver mutation labels, normalize the dataframe with mean method
x_test = normalize_dataframe(test_dataframe.iloc[:, 1:-1], method="mean")
# Initialize the test y data by only getting the driver mutation labels, use replace method to convert strings
y_test = test_dataframe.iloc[:, -1].replace({"driver": 1, "passenger": 0})

# Initialize the model object by calling logistic regression class, set learning rate and number of iterations
model = LogisticRegression(learning_rate=0.001, number_of_iterations=100)
# Fit the model object to training data by calling fit method of logistic regression
model.fit(x_train, y_train)

# Get the predicted y values by calling the predict method of logistic regression with test data
y_prediction = model.predict(x_test)

# Define a function to plot the cost vs iterations graph, take trained model as input
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html
def plot_cost(trained_model):
    # Initialize figure and axis with matplotlib subplots method
    fig, ax = plt.subplots()
    # Pass a series from zero to number of iterations and costs as x and y data of plot method
    ax.plot(range(trained_model.number_of_iterations), trained_model.costs)
    # Call show method to visualize the graph
    plt.show()

# Define a function to print the final weights of a trained model in descending order
def print_weights(trained_model):
    # Initialize a dictionary for adding features and weights as key-value pairs
    weight_dictionary = {}
    # Iterate n times, n being total number of features
    for i in range(trained_model.num_features):
        # Create an item in dictionary using training dataframe column (i+1 to skip "name") as key and weight as value
        weight_dictionary[training_dataframe.columns[i + 1]] = model.weights[i]
    # Use sorted method to sort the dictionary keys according to their values, set reverse to true for descending
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_keys = sorted(weight_dictionary, key=weight_dictionary.get, reverse=True)
    # Iterate through each key in sorted keys to get corresponding value of that key in unsorted one
    for key in sorted_keys:
        # Print the key that shows feature name, also print the value of that key that shows the weight
        print(f"Weight for {key} is: {weight_dictionary[key]}")

# Call plot cost function with already trained model to show cost vs iterations graph
plot_cost(model)
# Call print weights function with already trained model to print each weight and corresponding feature
print_weights(model)

# Define a function to create confusion matrix using actual y values and predicted y values
# https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
def create_confusion_matrix(y_actual, y_predicted):
    # Initialize a confusion matrix with true positive, true negative, false positive, and false negative as 0
    confusion_matrix = {
        "TP": 0,
        "TN": 0,
        "FP": 0,
        "FN": 0
    }
    # Iterate n times n being total number of actual y values
    for i in range(len(y_actual)):
        # Check if both actual and predicted value is 1
        if y_actual[i] == 1 and y_predicted[i] == 1:
            # If it is the case, increase true positive by 1
            confusion_matrix["TP"] += 1
        # Check if both actual and predicted value is 0
        elif y_actual[i] == 0 and y_predicted[i] == 0:
            # If it is the case, increase true negative by 1
            confusion_matrix["TN"] += 1
        # Check if actual value is 0 while predicted value is 1
        elif y_actual[i] == 0 and y_predicted[i] == 1:
            # If it is the case, increase false positive by 1
            confusion_matrix["FP"] += 1
        # Check if actual value is 1 while predicted value is 0
        elif y_actual[i] == 1 and y_predicted[i] == 0:
            # If it is the case, increase false negative by 1
            confusion_matrix["FN"] += 1
        # If none of the cases above occurs, enter the else state
        else:
            # Inform the user that an invalid data (neither 1 nor 0) is encountered
            print("Invalid data encountered for classification")
    # Return the updated confusion matrix dictionary
    return confusion_matrix

# Define a function to evaluate the model according to requested metric by taking its confusion matrix
# https://medium.com/analytics-vidhya/how-to-select-performance-metrics-for-classification-models-c847fe6b1ea3
def evaluate_model(confusion_matrix, metric):
    # Check if the requested metric is accuracy
    if metric == "accuracy":
        # If it is the case, calculate accuracy by (TP + TN) / (TP + TN + FP + FN) and print
        accuracy = (confusion_matrix["TP"] + confusion_matrix["TN"]) / sum(confusion_matrix.values())
        print(f"Accuracy of the model is: {accuracy}")
    # Check if the requested metric is specificity
    elif metric == "specificity":
        # If it is the case, calculate specificity by TN / (TN + FP) and print
        specificity = confusion_matrix["TN"] / (confusion_matrix["TN"] + confusion_matrix["FP"])
        print(f"Specificity of the model is: {specificity}")
    # Check if the requested metric is sensitivity
    elif metric == "sensitivity":
        # If it is the case, calculate sensitivity by TP / (TP + FN) and print
        sensitivity = confusion_matrix["TP"] / (confusion_matrix["TP"] + confusion_matrix["FN"])
        print(f"Sensitivity of the model is: {sensitivity}")
    # Check if the requested metric is precision
    elif metric == "precision":
        # If it is the case, calculate precision by TP / (TP + FP) and print
        precision = confusion_matrix["TP"] / (confusion_matrix["TP"] + confusion_matrix["FP"])
        print(f"Precision of the model is: {precision}")
    # If none of the cases above occurs, enter else state
    else:
        # Inform the user that requested metric is not defined
        print("Unknown evaluate metric requested")

# Create the confusion matrix by calling create confusion matrix, use test y and predicted y values and print
c_matrix = create_confusion_matrix(y_test, y_prediction)
print(f"Confusion matrix of the model is: {c_matrix}")

# Call evaluate model function with all metrics to print all the requested metrics of the trained model
evaluate_model(c_matrix, "accuracy")
evaluate_model(c_matrix, "specificity")
evaluate_model(c_matrix, "sensitivity")
evaluate_model(c_matrix, "precision")

# Create a function to compare locally defined logistic regression with logistic regression from scikit learn
# https://pythonguides.com/scikit-learn-logistic-regression/
def compare_sklearn(training_data_x, training_data_y, test_data_x):
    # Import the logistic regression from sklearn, do not import way above since class name is same with ours
    from sklearn.linear_model import LogisticRegression
    # Initialize the model by calling logistic regression class
    sklearn_model = LogisticRegression()
    # Use fit method and pass training data
    sklearn_model.fit(training_data_x, training_data_y)
    # Get the predicted y values using predict method
    sklearn_prediction = sklearn_model.predict(test_data_x)
    # Create the confusion matrix and print
    sklearn_c_matrix = create_confusion_matrix(y_test, sklearn_prediction)
    print(f"Confusion matrix of the sklearn is: {sklearn_c_matrix}")

    # Call evaluate model function with all metrics to print all the requested metrics of the trained model
    evaluate_model(sklearn_c_matrix, "accuracy")
    evaluate_model(sklearn_c_matrix, "specificity")
    evaluate_model(sklearn_c_matrix, "sensitivity")
    evaluate_model(sklearn_c_matrix, "precision")

# Call the compare sklearn function with the same data for comparison
compare_sklearn(x_train, y_train, x_test)
