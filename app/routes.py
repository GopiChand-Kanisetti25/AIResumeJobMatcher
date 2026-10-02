from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from app.skills import extract_skills
from app.ai_service import generate_ai_summary
from database import connection
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

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO resumes (filename, resume_text, ai_summary)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (file.filename, text, ai_summary)
    )

    resume_id = cursor.fetchone()[0]

    for skill in skills:
        cursor.execute(
            """
            INSERT INTO resume_skills (resume_id, skill)
            VALUES (%s, %s)
            """,
            (resume_id, skill)
        )

    connection.commit()
    cursor.close()

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "resume_text": text,
        "skills": skills,
        "ai_summary": ai_summary
    }


@router.get("/resumes")
def get_resumes():

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, filename, resume_text, ai_summary, uploaded_at
        FROM resumes
        ORDER BY id DESC
        """
    )

    resumes = cursor.fetchall()

    cursor.close()

    return {
        "resumes": resumes
    }


@router.get("/resumes/{resume_id}/skills")
def get_resume_skills(resume_id: int):

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT skill
        FROM resume_skills
        WHERE resume_id = %s
        """,
        (resume_id,)
    )

    skills = cursor.fetchall()

    cursor.close()

    return {
        "resume_id": resume_id,
        "skills": skills
    }
