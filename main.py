import os
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from database.db_helper import get_all_lead, get_single_lead_by_lead_id
from database.db_query import get_all_record, single_record
#from crew_result import kickoff

#print("Data from the database",table_created)

print("Data from the database", get_all_record(get_all_lead))
print("Data from the database single", single_record(get_single_lead_by_lead_id))

modal_name = "gpt-4o-mini"
temperature = 0

# # Load the API key from the .env file
load_dotenv()

# # Create the FastAPI app
apiKey = os.getenv("OPENAI_API_KEY")

# Check if the API key is not found in the environment variables
# if not apiKey:
#     raise ValueError("Missing API key for OpenAI. Please set the OPENAI_API_KEY environment variable.")

# Define 
llm = OpenAI(api_key=apiKey, default_headers={"content-type": "application/json", "user-agent": "OpenAI-Request"})

# Create the FastAPI app
app = FastAPI()

# # Allow requests from your React app (adjust this if your frontend runs elsewhere)
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5003",
    "http://127.0.0.1:5003"
]

# Define the request body
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/api/generate")
async def root(message: str):
    prompt = "What is the meaning of life?"
    
    try: 
        messages = [{"role": "user", "content": message + " " + prompt}]
        response = llm.chat.completions.create( model=modal_name, temperature=temperature, messages=messages)
        generated_response = response.choices[0]
        content = generated_response.message.content
        
        return {
            "role": "system",
            "content": content
        }
        
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))

# @app.post("/api/generate")
# async def root(message: str):
#     result = kickoff(message)
#     print("Result from the crew", result)
#     return result
   
   
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    