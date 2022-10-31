from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from typing import List

from logger import get_logger
from scraper import twitter_scraper

logger = get_logger(__name__)


def invoke(tags: List[str], max_workers: int = 4, no_of_tweets: int = 10):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        logger.debug(f"Invoking scraper for {tags}")
        results = executor.map(twitter_scraper, tags, repeat(no_of_tweets))
    return results
