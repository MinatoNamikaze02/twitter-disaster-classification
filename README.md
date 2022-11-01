# twitter-disaster-classification
An application that scrapes tweets off of Twitter based on given tags and uses a trained classification model to predict disasters.

## How to get started
- Get yourself a Twitter Developer API key by signing up [here](https://developer.twitter.com/en).
- Copy the contents from the `sample.env` file into a `.env` file and fill its contents.
- The `AUTH_TOKEN` can be anything (your own name if you're a narcissist). It is used for validation purposes.

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

## Hooks
- pre-commit is used to run `black`, `autoflake` and `isort` before every commit.
- pre-push is used to run `pytest` before every push.
- Note: These hooks do not work by default. Firstly, you need to add these hooks to git by running `git config core.hooksPath hooks` in the root directory            of the project.
- Then, you need to install the dependencies for these hooks by running `pip install -r test-requirements.txt` (if you haven't already).
- You also would need to give execute permissions to the hooks by running `chmod +x hooks/*`.
- You can use the `--no-verify` flag to ignore the hooks.


## Tests

## Demos

## Further Scope

## Bugs?
- Feel free to open an issue/PR
