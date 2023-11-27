from fastapi import FastAPI
from jinja2 import Template
from routes import router
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="RecSys API for Steam Games",
    version="0.2.0",
    description="This API allows you to access data from Steam, a leading video game platform, and get personalized game recommendations based on a machine learning model. With this API, you can query information about game genres, users, developers and reviews, as well as get suggestions of similar or suitable games for you or other users."
)

@app.get("/", tags=["Home"], status_code=200,  response_class=HTMLResponse)
def index():
  # Carga la plantilla HTML
  template = Template(open("index.html").read())

  # Renderiza la plantilla HTML
  return template.render()

app.include_router(router, tags=["Endpoints"])
