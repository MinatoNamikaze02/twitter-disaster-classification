import os
from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi import status as http_status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

import schemas
import utils
from CONSTANTS import MAX_WORKERS
from invoke_scraper import invoke
from logger import get_logger
from utils import ErrorHandlerRoute

logger = get_logger(__name__)
auth_token = os.environ["AUTH_TOKEN"]

app = FastAPI(
    title="Twitter Disaster",
    description="",
    version="0.1",
)
app.router.route_class = ErrorHandlerRoute

# TODO: This needs to be tuned
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def status():
    return {"status": "OK"}


@app.get("/tweets", response_model=List[schemas.TweetData])
async def get_tweets_by_tag(request: schemas.TweetRequest, token=Depends(HTTPBearer())):
    creds = token.credentials
    if creds != auth_token:
        raise HTTPException(
            status_code=http_status.HTTP_403_FORBIDDEN, detail="Invalid auth token"
        )
    if request.count < 10:
        raise HTTPException(
            status_code=http_status.HTTP_400_BAD_REQUEST, detail="Count should be >= 10"
        )
    results = invoke(request.tags, max_workers=MAX_WORKERS, no_of_tweets=request.count)
    results = [*results]
    tweets = utils.predictions(results)

    return tweets


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"][
        "fmt"
    ] = "%(asctime)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"][
        "fmt"
    ] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
