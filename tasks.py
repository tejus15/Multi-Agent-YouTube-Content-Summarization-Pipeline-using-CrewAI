from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research task
research_task=Task(
    description=(
        'Identify the video {search_query} in the channel {youtube_channel_handle}.'
        'Get detailed information about the video from the channel {youtube_channel_handle}.'
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {search_query} of video",
    tools=[yt_tool],
    agent=blog_researcher
)

# Writing task with language model configuration
write_task=Task(
    description=(
        'get the info from the YouTube channel {youtube_channel_handle} on the topic {search_query}'
    ),
    expected_output="Summarize the info in the video on the topic {search_query} from {youtube_channel_handle} and create the content for the blog.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False, # To ensure sequential execution
    output_file='new-blog-post.md'
)