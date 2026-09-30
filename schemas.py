from pydantic import BaseModel, Field

"""

BaseModel is core pydantic class used for data validation, parsing, serialization etc.
There is RootModel also, which is used when the data you are working is a single non-nested vaklue like list or scalar value, 
    to avoid unnecessary wrapping in attributes 

FUN-FACT: str_output---> this is snake_case wwriting and strOutput---> this is camelCase writing

"""
class JDInput(BaseModel):
    job_description: str = Field(..., min_length=50, description="The raw job description text")

class InterviewQuestion(BaseModel):
    question: str
    concept_tested: str
    expected_answer_summary: str

class AgentResponse(BaseModel):
    primary_tech_stack: list[str]
    top_three_skills: list[str]
    practice_questions: list[InterviewQuestion]
