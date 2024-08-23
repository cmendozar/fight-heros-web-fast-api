import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from main import simulate_battle
from app.sender import send_mail

app = FastAPI()

static_directory = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_directory), name="static")

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/simulate", response_class=HTMLResponse)
async def send_simulate_battle(
    request: Request,
    email: str = Form(...),
    team1_name: str = Form(...),
    team2_name: str = Form(...)
):
    simulate_battle(team1_name, team2_name)
    with open("fight.txt", "r") as f:
        battle_result = f.read()
    
    subject = f"FIGHT DETAIL {team1_name} v/s {team2_name}"
    send_mail(email, subject, battle_result)
    
    return RedirectResponse("/", status_code=303)
