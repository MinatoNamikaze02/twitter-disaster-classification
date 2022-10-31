import datetime
import json
import os
from typing import List

import tweepy
from dotenv import load_dotenv

from CONSTANTS import DUMP_PATH
from logger import get_logger
from schemas import TweetData

load_dotenv()
logger = get_logger(__name__)


def twitter_scraper(tag, no_of_tweets) -> List[TweetData]:
    bearer_token = os.getenv("BEARER_TOKEN")
    # print(bearer_token)
    client = tweepy.Client(bearer_token=bearer_token, return_type=dict)

    query = f"#{tag} -is:retweet lang:en"
    try:
        tweets = client.search_recent_tweets(
            query=query,
            tweet_fields=["context_annotations", "created_at"],
            max_results=no_of_tweets,
        )
    except Exception as e:
        logger.error(f"Error while fetching tweets for {tag}: {e}")
        return None

    if tweets["meta"]["result_count"] == 0:
        return None

    to_write_dir = os.path.join(DUMP_PATH, tag)
    if not os.path.exists(to_write_dir):
        os.makedirs(to_write_dir)

    # write to json file with timestamp
    # print(tweets)
    for tweet in tweets["data"]:
        to_write_path = os.path.join(to_write_dir, f"{datetime.datetime.utcnow()}.json")
        with open(to_write_path, "w") as f:
            json.dump(tweet, f)

    return tweets["data"]
