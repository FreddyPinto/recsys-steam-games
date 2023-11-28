from models import Message
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from database import PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, get_sentiment_by_developer

router = APIRouter()


@router.get("/PlayTimeGenre/{genre}", responses={
    404: {"model": Message, "description": "The genre was not found"},
    200: {
        "description": "Year requested by genre",
        "content": {
            "application/json": {
                "example": {
                    "Year with the most hours played for Genre X”": 2013
                }
            }
        },
    },
},
)
async def play_time_genre(genre: str = Path(...,
                                            description="Enter a genre",
                                            example='Simulation')):
    """
        Returns the year with the most hours played for a given genre.
    """
    response = await PlayTimeGenre(genre)
    if response is None:
        return JSONResponse(status_code=404, content={
            "message": f"Genre {genre} not found. Please try again."})

    return response


@router.get("/UserForGenre/{genre}", responses={
    404: {"model": Message, "description": "The genre was not found"},
    200: {
        "description": "User requested by genre",
        "content": {
            "application/json": {
                "example": {
                    "User with most hours played for Genre X": "us213ndjss09sdf",
                    "Playtime": [
                        {
                            "Year": 2013,
                            "Hours": 203
                        },
                        {
                            "Year": 2012,
                            "Hours": 100
                        },
                        {
                            "Year": 2011,
                            "Hours": 23
                        }
                    ]
                }
            }
        },
    },
},
)
async def user_for_genre(genre: str = Path(
        description="Enter a genre",
        example='RPG')):
    """
        Returns the user who has accumulated the most played hours for the given genre and a list of accumulated playtime by release year.
    """
    response = await UserForGenre(genre)

    if response is None:
        return JSONResponse(status_code=404, content={
            "message": f"Genre {genre} not found. Please try again."})

    return response


@router.get("/UsersRecommend/{year}", responses={
    404: {"model": Message, "description": "The year was not found"},
    200: {
        "description": "Games requested by year",
        "content": {
            "application/json": {
                "example": [{
                    "Rank 1": "X",
                },
                    {
                    "Rank 2": "Y",
                },
                    {
                    "Rank 3": "Z",
                },]
            }
        },
    },
},
)
async def users_recommend(year: int = Path(
        description="Enter a year",
        example=2013)):
    """
    Returns the top 3 games MOST recommended by users for the given year.
    """
    response = await UsersRecommend(year)
    print(response)
    if response is None:
        return JSONResponse(status_code=404, content={
            "message": f"The year {year} has not reviews to calculate the ranking of the most recommended games. Please try another year."})
    return response


@router.get("/UsersWorstDeveloper/{year}", responses={
    404: {"model": Message, "description": "The year was not found"},
    200: {
        "description": "Developers requested by year",
        "content": {
            "application/json": {
                "example": [{
                    "Rank 1": "X",
                },
                    {
                    "Rank 2": "Y",
                },
                    {
                    "Rank 3": "Z",
                },]
            }
        },
    },
},)
async def users_worst_developer(year: int = Path(
        description="Enter a year",
        example=2011)):
    """
    Returns the top 3 developers with the LEAST recommended games by users for the given year.
    """
    response = await UsersWorstDeveloper(year)
    if response is None:

        return JSONResponse(status_code=404, content={
            "message": f"The year {year} has no reviews to calculate the developers' ranking with least recommended games. Please try another year."})
    return response


@router.get("/SentimentAnalysis/{developer}", responses={
    404: {"model": Message, "description": "The developer was not found"},
    200: {
        "description": "Sentiment analysis requested by developer",
        "content": {
            "application/json": {
                "example": {
                    "Valve": [
                        {
                            "Negative": 1352
                        },
                        {
                            "Neutral": 2202
                        },
                        {
                            "Positive": 4840
                        }
                    ]
                }
            }
        },
    },
},)
async def sentiment_analysis(developer: str = Path(
        description="Enter developer's name",
        example="Ubisoft")):
    """
    Returns a developer with the total number of users reviews records categorized with a sentiment analysis.
    """

    response = await get_sentiment_by_developer(developer)
    if response is None:

        return JSONResponse(status_code=404, content={
            "message": f"Developer {developer} not found. Please try again."})
    return response
