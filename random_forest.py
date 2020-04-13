import pandas as pd
import keras
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier


def load_data():
    df1 = pd.read_csv('vgsales.csv')
    y = df1['Global_Sales']
    df2 = pd.read_csv('igdb_data.csv')
    X = df2['keywords']

    return X, y


def main():
    split = 0.2

    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(metrics.accuracy_score(y_test, y_pred))



if __name__ == '__main__':
    main()