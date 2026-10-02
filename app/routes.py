from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from app.skills import extract_skills
from app.ai_service import generate_ai_summary
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    skills = extract_skills(text)
    ai_summary = generate_ai_summary(text)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "resume_text": text,
        "skills": skills,
        "ai_summary": ai_summary
    }