from models import Message
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from database import get_game_recommender

recommender  = APIRouter()


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
