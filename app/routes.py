from fastapi import APIRouter, status, HTTPException, Path
from database import *

router = APIRouter()


@router.get("/PlayTimeGenre/{genre}")
async def play_time_genre(genre: str = Path(...,
                                            description="Enter a genre",
                                            example='Simulation')):
    """
        Returns the year with the most hours played for a given genre.
    """
    response = await PlayTimeGenre(genre)
    if response is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genre {genre} not found")
    return response


@router.get("/UserForGenre/{genre}")
async def user_for_genre(genre: str = Path(
        description="Enter a genre",
        example='RPG')):
    """
        Returns the user who accumulates the most hours played for a given genre.
    """
    response = await UserForGenre(genre)
    if response is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Genre {genre} not found")
    return response


@router.get("/UsersRecommend/{year}")
async def users_recommend(year: int = Path(
        description="Enter a year",
        example=2013)):
    """
    Returns the top 3 MOST recommended games by users for the given year.
    """
    response = await UsersRecommend(year)
    if response is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Year {year} not found")
    return response


@router.get("/UsersWorstDeveloper/{year}")
async def users_worst_developer(year: int = Path(
        description="Enter a year",
        example=2011)):
    """
    Returns the top 3 developers with the LEAST recommended games by users for the given year.
    """
    response = await UsersWorstDeveloper(year)
    if response is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Year {year} not found")
    return response


@router.get("/SentimentAnalysis/{developer}", response_description="Get the sentiment analysis by developer")
async def sentiment_analysis(developer: str = Path(
        description="Enter developer's name",
        example="Ubisoft")):
    """
    Returns a developer with the total number of users reviews records categorized with a sentiment analysis.
    """

    response = await get_sentiment_by_developer(developer)
    if response is None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Developer {developer} not found")
    return response
