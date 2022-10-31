import pickle

import pandas as pd

from model_tokenize import tokenize

datasetX = pd.read_csv("../dataset/disaster_messages.csv")
datasetY = pd.read_csv("../dataset/disaster_categories.csv")

final = pd.merge(datasetX, datasetY, how="left", on="id")

categories = final["categories"].str.split(";", expand=True)

row = categories.iloc[0]

# use this row to extract a list of new column names for categories.
# one way is to apply a lambda function that takes everything
# up to the second to last character of each string with slicing
category_colnames = row.apply(lambda string: string[0:-2])

categories.columns = category_colnames
for column in categories:
    # set each value to be the last character of the string
    categories[column] = categories[column].astype(str).str[-1:]

    # convert column from string to numeric
    categories[column] = pd.to_numeric(categories[column])
final.drop(axis=1, columns="categories", inplace=True)
final = pd.concat([final, categories], axis="columns")
final.drop_duplicates(inplace=True)

X = final["message"]
text = X[0]
Y = final.iloc[:, 4:]


from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline

# instantiate Pipeline
pipeline = Pipeline(
    [
        # text tokenizer & tfidf transformer
        (
            "text_pipeline",
            Pipeline(
                [
                    ("vect", CountVectorizer(tokenizer=tokenize)),
                    ("tfidf", TfidfTransformer()),
                ]
            ),
        ),
        # estimator
        ("clf", MultiOutputClassifier(RandomForestClassifier(random_state=42))),
    ]
)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0
)
model = pipeline.fit(X_train, Y_train)
Y_pred = pipeline.predict(X_test)

filename = "disaster_model.sav"
pickle.dump(model, open(filename, "wb"))
