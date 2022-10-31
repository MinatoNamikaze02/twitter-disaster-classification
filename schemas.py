from typing import List, Optional

from pydantic import BaseModel


class Domain(BaseModel):
    id: str
    name: str
    description: Optional[str]


class Context(BaseModel):
    domain: Domain
    entity: Domain


class PredictedLabels(BaseModel):
    label: str


class TweetData(BaseModel):
    edit_history_tweet_ids: Optional[List[str]]
    id: str
    text: str
    created_at: str
    context_annotations: Optional[List[Context]]
    predictions: Optional[List[PredictedLabels]]

    class Config:
        orm_mode = True


class TweetRequest(BaseModel):
    tags: List[str]
    count: int
