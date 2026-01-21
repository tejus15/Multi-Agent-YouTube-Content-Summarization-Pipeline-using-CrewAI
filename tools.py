from crewai import Agent, Task, Crew
from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool for general YouTube channel searches
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='youtube.com/channel/UC6c1z7bA__85CIWZ_jpCK-Q')
