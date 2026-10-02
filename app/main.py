from fastapi import FastAPI
from app.routes import router
from app.job_routes import router as job_router

app = FastAPI(
    title="AI-Powered Resume Screening & Job Matching System"
)

app.include_router(router)
app.include_router(job_router)


@app.get("/")
def home():
    return {
        "message": "AI Resume Job Matcher API is running"
    }