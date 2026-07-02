from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import engine, Base
from app.routes import shm, datasets

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mohammad Shamsi — SHM Platform",
    description="Hybrid Physics-Informed Neural Networks for Structural Health Monitoring",
    version="0.1.0",
)

# ---- API Routes ----
app.include_router(shm.router, prefix="/api/shm", tags=["SHM Analysis"])
app.include_router(datasets.router, prefix="/api/datasets", tags=["Datasets"])

# ---- Static Files ----
# Mount /static for CSS, JS, images if you split them later
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---- Serve Website ----
@app.get("/")
async def serve_website():
    """Serve the main personal website"""
    return FileResponse("static/index.html")

@app.get("/cv")
async def download_cv():
    """Download CV"""
    return FileResponse(
        "static/papers/cv_shamsi.pdf",
        media_type="application/pdf",
        filename="Mohammad_Shasmi_CV.pdf"
    )

@app.get("/papers/{filename}")
async def download_paper(filename: str):
    """Download a paper by filename"""
    return FileResponse(
        f"static/papers/{filename}",
        media_type="application/pdf"
    )

@app.get("/code/{filename}")
async def download_code(filename: str):
    """Download a code package by filename"""
    return FileResponse(
        f"static/code/{filename}",
        media_type="application/octet-stream"
    )

# ---- Health Check ----
@app.get("/api/health")
async def health_check():
    return {
        "status": "running",
        "service": "SHM Platform",
        "author": "Mohammad Shamsi",
        "version": "0.1.0"
    }