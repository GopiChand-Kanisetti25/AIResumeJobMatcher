# AI-Powered Resume Screening & Job Matching System

An AI-powered application built with Python and FastAPI to analyze resumes, extract skills, compare resumes with job descriptions, identify skill gaps, and generate AI-based resume summaries.

## Features

- Resume PDF upload
- Resume text extraction
- Skill extraction
- Job description analysis
- Resume and job matching
- Matched skills identification
- Missing skills identification
- AI-generated resume summary
- REST API endpoints
- Swagger API documentation

## Technologies

- Python
- FastAPI
- REST API
- NLP
- spaCy
- Pandas
- PostgreSQL
- OpenAI API
- GitHub

## Project Flow

Resume PDF → Text Extraction → Skill Extraction → Job Description Analysis → Resume & Job Matching → Skill Gap Analysis → AI-Generated Summary

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/upload-resume` | Upload and analyze a resume |
| POST | `/job-description` | Analyze a job description |
| POST | `/job-match` | Compare resume skills with job requirements |
| POST | `/ai-summary` | Generate an AI resume summary |

## How to Run

Install the required packages:

    pip install -r requirements.txt

Start the FastAPI application:

    uvicorn main:app --reload

Open Swagger API documentation:

    http://127.0.0.1:8000/docs

## Security

API keys and uploaded resumes are excluded from GitHub using `.gitignore`.

## Author

Kavya Sri
