from models import Message
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from database import get_game_recommender, get_user_recommendation

recommender = APIRouter()


@recommender.get("/GameRecommender/{game}", responses={
    404: {"model": Message, "description": "The game was not found"},
    200: {
        "description": "Recommended games requested by item_name",
        "content": {
            "application/json": {
                "example": {1: 'Hotline Miami 2: Wrong Number',
                            2: 'Dino D-Day',
                            3: 'BattleBlock Theater®',
                            4: 'The Forest',
                            5: 'Yet Another Zombie Defense'}
            }
        },
    },
},)
async def game_recommender(game: str = Path(
        description="Enter game name",
        example="APB Reloaded")):
    """
        Returns 5 recommended games similar to a given game.
    """
    response = await get_game_recommender(game)
    if response is None:

        return JSONResponse(status_code=404, content={
            "message": f"Game {game} not found. Please try again."})
    return response


@recommender.get("/UserRecommender/{user_id}", responses={
    404: {"model": Message, "description": "User not found"},
    200: {
        "description": "Recommended games requested by user_id",
        "content": {
            "application/json": {
                "example": {1: '8BitMMO',
                            2: 'A Story About My Uncle',
                            3: 'Aliens vs. Predator™',
                            4: 'ARMA: Cold War Assault',
                            5: 'APB Reloaded'}
            }
        },
    },
},)
async def user_recommender(user_id: str = Path(
        description="Enter user id",
        example="yoshipowerz")):
    """
        Returns the 5 games with the highest predicted rating for the user.
    """
    response = await get_user_recommendation(user_id)
    if response is None:

        return JSONResponse(status_code=404, content={
            "message": f"User {user_id} not found. Please try again."})
    return response
