# CTCNA ClimateNatureAI API starter

This is a minimal FastAPI scaffold only. It is not a deployed service and does not load the supplied joblib model.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs

Before production: configure a managed PostgreSQL/PostGIS database, environment variables, authentication for write operations, restricted CORS origins, logging, backups, TLS and data-access controls. Do not expose stakeholder personal data, draft budgets, private registers or model binaries via a public static website.
