# twitter-disaster-classification
An application that scrapes tweets off of Twitter based on given tags and uses a trained classification model to predict disasters.

## How to get started
- Get yourself a Twitter Developer API key by signing up [here](https://developer.twitter.com/en).
- Copy the contents from the `sample.env` file into a `.env` file and fill its contents.
- The `AUTH_TOKEN` can be anything. It is used for validation purposes.

## Dependencies
- Download all the dependencies by running 
  `$ pip install -r requirements.txt`
  
## Training
- You can train the model by running 
  `$ python model_setup.py`
- Once this is done, you will be able to see a `disaster_model.sav` file.

## Server
- You can run the server by running
  `$ python main.py`

## Client
- Run the client manually and interact with the application there.

## Tests
- You can run the tests by running
  ```$ python test_main.py```
  
## Demos

https://user-images.githubusercontent.com/85065053/200167204-eef0cae8-b196-49f6-82b2-e7f13e274b58.mov


## Further Scope
- First and foremost, the model needs to be trained on a better and/or larger dataset.
- The UI needs to be improved (I'm not a UI/UX guy).
- Add data visualization in the client side.
- Heatmaps (need to get location information).
- Get more useful information out of the scraping process (will work on this).
- **Please do open issues if you can think of any!**

## Bugs?
- Feel free to open an issue.
