from fastapi import APIRouter
from app.skills import extract_skills
from app.ai_service import generate_ai_summary

router = APIRouter()


@router.post("/job-match")
def job_match(resume_text: str, job_description: str):

    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
@router.post("/ai-summary")
def ai_summary(resume_text: str):

    summary = generate_ai_summary(resume_text)

    return {
        "summary": summary
    }