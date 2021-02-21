# Importing the needed dependencies
import pandas as pd
import numpy as np

data = pd.read_csv(r"diabetes.csv")
data.head()

# load data in a DataFrame object called dataframe now.
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)

# Converting the DataFrame object to a NumPy array
array = dataframe.values

# Segregating the data into separate variables so that the features and the labels are separated
X = array[:, 0:8]
Y = array[:, 8]

# Import the necessary libraries first
#
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)

# Summarize scores
np.set_printoptions(precision=3)
# print(fit.scores_)

features = fit.transform(X)
# displaying the selected features for certain number of records
# print(features[0:120, :])


# Selecting the given number of features
def select_k_features(X, Y, k):
    k_best = SelectKBest(score_func=chi2, k=k)
    fit = k_best.fit(X, Y)
    features = fit.transform(X)
    best_features = fit.scores_
    best_features.sort()
    print("Scores:")
    print(fit.scores_)
    print("Best {} selected features:".format(k))
    print(best_features[-k:])
    return features


# Writing the selected features to csv
def save_to_csv(file_to_save, name):
    np.savetxt(name, file_to_save, delimiter=",", fmt="%1.3g")


# Select and export the given number of features
def select_and_export_top_k_features(X, Y, k):
    features = select_k_features(X, Y, k)

    csv_name = "top_{}_features.csv".format(k)
    save_to_csv(features, csv_name)


select_and_export_top_k_features(X, Y, 2)
select_and_export_top_k_features(X, Y, 3)
select_and_export_top_k_features(X, Y, 5)