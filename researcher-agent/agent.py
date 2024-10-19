from crewai import Agent
from tools import search_tool, web_search_tool, web_scrap_tool
import os
from dotenv import load_dotenv
from crewai import LLM

modal_name = "gpt-4o-mini"
temperature = 0

# Load the API key from the .env file
load_dotenv()

# Create the FastAPI app
apiKey = os.getenv("OPENAI_API_KEY")

if apiKey is None:
    print("API_KEY not found in .env file.")
else:
    print(f"API Key Loaded: {apiKey}")  # Check if the correct key is loaded (remove in production)

#this is openAi modal for the agent
llm = LLM(
    model=modal_name,
    api_key=apiKey
)

#llm = OpenAI(api_key=apiKey, default_headers={"content-type": "application/json", "user-agent": "OpenAI-Request"})

print ("LLM", llm)

#Creating a Senior researcher agent

reseracher = Agent(
    role="Senior AI and Machine Learning Researcher",
    name="Dr. Vinod",
    goal="Uncover groundbreaking research in the field of AI {topic}",
    backstory="Agent Vinod is a Senior Researcher at the Crew AI Research Institute. He has been working in the field of AI for over 10 years and has published numerous papers in top-tier conferences and journals. He is passionate about pushing the boundaries of AI research and is always on the lookout for new and exciting projects to work on. you explore and share your latest innovations in the field of AI.",
    verbose=True,
    memory=True,
    tools=[search_tool, web_search_tool, web_scrap_tool],
    allow_delegation=True,  
    llm=llm
)


#creating a senior blog writer agent in the field of AI and Machine Learning

senior_blog_writer = Agent(
    goal="Uncover groundbreaking research in the field of AI and write good blog {topic}",
    role="Senior AI and Machine Learning Blog Writer",
    name="Dr. Aayush",
    verbose=True,
    memory=True,
    backstory="Dr. Aayush is a Senior AI and Machine Learning Blog Writer at the Crew AI Research Institute. He has a passion for writing and has been writing about AI and Machine Learning for over 5 years. He is always on the lookout for new and exciting topics to write about and is dedicated to sharing his knowledge with the world.",
    allow_delegation=False,
    tools=[search_tool, web_search_tool, web_scrap_tool],
    llm=llm
)