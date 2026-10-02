from fastapi import APIRouter
from app.skills import extract_skills
from app.ai_service import generate_ai_summary, generate_interview_questions

router = APIRouter()


@router.post("/job-description")
def add_job_description(job_description: str):

    required_skills = extract_skills(job_description)

    return {
        "message": "Job description received successfully",
        "job_description": job_description,
        "required_skills": required_skills
    }


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


@router.post("/interview-questions")
def interview_questions(resume_text: str):

    questions = generate_interview_questions(resume_text)

    return {
        "interview_questions": questions
    }
