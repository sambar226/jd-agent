import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google.genai.errors import APIError

from schemas import JDInput, AgentResponse
from agent import analyse_jd

#Configure logging for production observability
logging.basicConfig(level=logging.INFO) # this lets you adjust how much detailed log you need , DEBUG, INFO, ERROR
logger=logging.getLogger(__name__)

app=FastAPI(
    title="JD Prep Agent API", 
    version="1.0.0",
    description="Extracts insights and interview questions from Job Descriptions."
)

# Allow frontend clients to call your API (configure origins securely in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status":"healthy","service":"JD Prep Agent"}

@app.post("/api/v1/analyse", response_model=AgentResponse, tags=["Agent"])
async def analyse_job(payload: JDInput):
    try:
        logger.info("Processing New JD analysis request")
        # Await the async function so the event loop is free while Gemini thinks
        result=await analyse_jd(payload.job_description)
        return result
    except APIError as api_err:
        # Catch specific Google GenAI errors (like quota limits or bad requests)
        logger.error(f"Upstream API Error: {api_err}")
        raise HTTPException(status_code=502, detail="Upstream AI provider error")
        
    except Exception as e:
        # Catch everything else
        logger.error(f"Internal processing failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal AI processing error")
