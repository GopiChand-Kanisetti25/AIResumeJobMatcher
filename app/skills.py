SKILLS = [
    "Python",
    "SQL",
    "FastAPI",
    "Django",
    "Flask",
    "PostgreSQL",
    "MySQL",
    "Docker",
    "AWS",
    "Git",
    "GitHub",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "NLP",
    "REST API",
    "Java",
    "C++",
    "HTML",
    "CSS"
]


def extract_skills(text):
    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills