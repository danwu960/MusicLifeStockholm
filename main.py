from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes.user import user_router

DIR_PATH = Path(__file__).resolve().parent
# print(DIR_PATH)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user_router)
templates = Jinja2Templates(directory=str(DIR_PATH / "templates"))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    # with open('/home/danwu960/Music/templates/about.html', encoding="utf-8") as file:
    #    html = file.read()
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/statistics", response_class=HTMLResponse)
async def statistics(request: Request):
    # with open('/home/danwu960/Music/templates/statistics.html', encoding="utf-8") as file:
    #    html = file.read()
    return templates.TemplateResponse("statistics.html", {"request": request})


@app.get("/links", response_class=HTMLResponse)
async def links(request: Request):
    # with open('/home/danwu960/Music/templates/about.html', encoding="utf-8") as file:
    #    html = file.read()
    return templates.TemplateResponse("links.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
