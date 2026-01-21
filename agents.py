from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
# os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")
# os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

llm = LLM(
    model="openai/gpt-4o",
    api_key=os.environ["OPENAI_API_KEY"],  # Or set OPENAI_API_KEY
    temperature=0.7,
    max_tokens=4000
)
#llm = LLM(
#    model="ollama/llama3:70b",
#    base_url="http://localhost:11435"
#)

# Create a senior blog content researcher.
blog_researcher=Agent(
    role='Blog Researcher from YouTube Videos',
    goal='Get the relevant video content for the topic {search_query} from YT Channel {youtube_channel_handle}',
    verbose=True,
    memory=True,
    backstory=(
        'Expert in understanding videos about Soccer News'
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True,
)

# Create a senior blog writer agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling stories about the video {search_query} from YT Channel {youtube_channel_handle}',
    verbose=True,
    memory=True,
    backstory=(
        'Create an engaging narrative that captures Soccer News in an accessible manner'
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False,
)