import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_summary(resume_text):
    response = client.responses.create(
        model="gpt-6-luna",
        input=f"""
        Analyze this resume and provide a short professional summary.

        Resume:
        {resume_text}
        """
    )

    return response.output_text