import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
#from dotenv import load_dotenv
#load_dotenv()

# Create the FastAPI app
#serper_key = os.getenv("OPENAI_API_KEY")

# Initialize the tool for internet searching capabilities
# search_tool = SerperDevTool(
#     api_key=serper_key,
#     search_url="https://google.serper.dev/scholar",
#      country="fr",
#     locale="fr",
#     location="Paris, Paris, Ile-de-France, France",
#     n_results=2,
#     save_file=True,
# )

web_scrap_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()
web_search_tool = WebsiteSearchTool()