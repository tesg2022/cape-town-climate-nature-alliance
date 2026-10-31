from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json

app = FastAPI(title="CTCNA ClimateNatureAI API", version="0.1.0",
              description="Research-stage environmental assessment API")

# Replace with the final dashboard origin once deployed.
ALLOWED_ORIGINS = [
    "https://tesg2022.github.io",
    "https://ctcna.org",
    "https://www.ctcna.org",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

@app.get("/health")
def health():
    return {"status": "ok", "service": "ctcna-climatenatureai", "stage": "starter"}

@app.get("/api/v1/assessment/summary")
def summary():
    path = DATA_DIR / "26_CIEIF_Assessment_Summary.json"
    if not path.exists():
        return {"status": "not_configured", "message": "Place approved assessment summary in backend/data"}
    return json.loads(path.read_text(encoding="utf-8"))
