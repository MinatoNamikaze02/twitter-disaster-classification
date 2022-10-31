import pickle

from CONSTANTS import categories_colnames
from model_tokenize import tokenize


def load_model():
    loaded_model = pickle.load(open("./disaster_model.sav", "rb"))
    return loaded_model


def predict(text):
    model = load_model()
    predictions = model.predict([text])
    return predictions


if __name__ == "__main__":
    text = "USGS reports a M2.1 earthquake, 23 km SSE of Chickaloon, Alaska on 10/30/22 @ 21:46:09 UTC https://t.co/r8riT6kBTD #earthquake"
    predictions = predict(text)
    for i in range(len(predictions[0])):
        if predictions[0][i] == 1:
            print(categories_colnames[i])
