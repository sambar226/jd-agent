import os
import google.genai as genai
from google.genai import types
from schemas import AgentResponse
from dotenv import load_dotenv
load_dotenv()

#to use async we use client.aio
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Extract the async client for FastAPI integration
aclient=client.aio

async def analyse_jd(job_text: str)-> AgentResponse:
    prompt = f"""
    You are an expert technical recruiter and AI engineering manager. 
    Analyze the following job description. Extract the primary tech stack, 
    the top 3 most critical skills, and generate 3 highly probable technical 
    interview questions based on these requirements.
    
    Job Description: {job_text}
    """
    # Enforce structured JSON output matching our Pydantic model
    
    #now we are using async so we added "await" keyword below to run this in new thread
    response= await aclient.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AgentResponse,
            temperature=0.2 
        )
    )

    return response.parsed

# Assuming your previous code is in a file (e.g., analyzer.py) or you append this to the bottom:
"""

if __name__ == "__main__":
    sample_job = 
    We are looking for a Senior Backend Engineer to join our team. 
    You must have 5+ years of experience with Python, Django, and PostgreSQL. 
    Experience with AWS and Docker is a big plus. You will be building scalable APIs.
    
    
    print("Analyzing job description...")
    result = analyse_jd(sample_job)
    
    print("\n--- Analysis Result ---")
    print(f"Tech Stack: {result.primary_tech_stack}")
    print(f"Top 3 Skills: {result.top_three_skills}")
    print("\nInterview Questions:")
    for i, q in enumerate(result.practice_questions, 1):
        print(f"{i}. Concept: {q.concept_tested}")
        print(f"   Q: {q.question}")
        print(f"   A: {q.expected_answer_summary}\n")
"""