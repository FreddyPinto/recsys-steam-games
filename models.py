from pydantic import BaseModel
# from typing import Optional, Dict, List


# class SentimentCount(BaseModel):
#     Negative: int
#     Neutral: int
#     Positive: int


# class SentimentAnalysis(BaseModel):
#     Dict[str, SentimentCount]

class Message(BaseModel):
    message: str