from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="RecSys API for Steam Games",
    version="0.2.0",
    description="This API allows you to access data from Steam, a leading video game platform, and get personalized game recommendations based on a machine learning model. With this API, you can query information about game genres, users, developers and reviews, as well as get suggestions of similar or suitable games for you or other users."
)

app.include_router(router, tags=["Endpoints"])
