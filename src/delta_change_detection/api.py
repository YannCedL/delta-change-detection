# API FastAPI pour le moteur Delta Change Detection
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .analyzer import detect_change

app = FastAPI(
    title="Delta Change Detection API",
    description="Moteur de Détection de Changements & Comparateur Temporel",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec comparateur de diffs
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Delta API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Delta", "version": "1.0.0"}

@app.get("/api/v1/detect", response_model=ResultContract)
def get_detect(lat: float = Query(48.8566), lon: float = Query(2.3522), date_start: str = Query("2026-01-01"), date_end: str = Query("2026-05-01")):
    return detect_change(lat, lon, date_start, date_end)
