import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def read_data():
    df = pd.read_csv('igdb_data.csv')
    keywords = df['keywords']
    names = df['slugs']
    df_sales = pd.read_csv('vgsales.csv')

    sales = df_sales['']

    return keywords, names, sales


def construct_dictionary(keywords):
    word_dict = {}
    index = 0
    for list in keywords:
        for word in list:
            if word not in word_dict:
                word_dict[word] = index
                index += 1

    return word_dict


def encode_features(word_dict, keywords):
    length = len(word_dict)
    X = []
    for list in keywords:
        feature = np.zeros(shape=(length,))
        for word in list:
            feature[word_dict[word]] = 1

        X.append(feature)

    return np.array(X)


def main():
    keywords, names, sales = read_data()
    word_dict = construct_dictionary(keywords)
    X = encode_features(word_dict, keywords)
    Y = extract_from_sales()
    X_train, Y_train, X_test, Y_test = train_test_split(X, Y, test_size=0.2)

    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)

    print(metrics.accuracy_score(Y_test, Y_pred))


if __name__ == '__main__':
    main()