from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DataFellas API",
    description="Workflow Orchestrator untuk Automasi Riset Kualitatif",
    version="0.1.0"
)

# CORS middleware untuk komunikasi dengan frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "DataFellas API - ResTech 2026"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
