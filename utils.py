import pickle
from typing import Callable

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response

import schemas
from CONSTANTS import CATEGORIES_COLNAMES
from logger import get_logger
from model_tokenize import tokenize

logger = get_logger(__name__)


class ErrorHandlerRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except RequestValidationError as exc:
                # Default handler will handle this
                raise exc
            except HTTPException as exc:
                # Default handler will handle this
                raise exc
            except Exception as exc:
                logger.exception(f"Error occurred: {exc}")
                # Raise unknown exception
                raise exc

        return custom_route_handler


def predictions(results) -> list:
    loaded_model = pickle.load(open("./disaster_model.sav", "rb"))
    tweets = []
    for res in results:
        for tweet in res:
            try:
                if tweet:
                    final_tweet = schemas.TweetData(**tweet)
                    predictions = loaded_model.predict([final_tweet.text])
                    final_tweet.predictions = []
                    categories = return_categories(predictions=predictions)
                    for category in categories:
                        final_tweet.predictions.append(
                            schemas.PredictedLabels(label=category)
                        )
                    tweets.append(final_tweet)
            except Exception as e:
                logger.error(e)
    return tweets


def return_categories(predictions) -> list:
    categories = []
    for i in range(len(predictions[0])):
        if predictions[0][i] == 1:
            categories.append(CATEGORIES_COLNAMES[i])

    return categories
