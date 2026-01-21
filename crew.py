from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from datetime import date, timedelta
from tools import yt_tool

today = date.today()
tomorrow = today + timedelta(days=1)


crew=Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

yt_tool.cache_function = lambda *args, **kwargs: False
inputs = {
    "youtube_channel_handle": "@ESPN",
    "search_query": "ESPN FC calls for ACTION after 'lawless nonsense' at AFCON final + Man City's struggles continue"
}
result = crew.kickoff(inputs=inputs)
