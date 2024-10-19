
from crewai import Process, Crew
from agent import senior_blog_writer, reseracher
from task import research_task, write_blog_task


my_crew = Crew(
    agents=[
        reseracher,
        senior_blog_writer
        
    ],
    tasks=[
        research_task,
        write_blog_task
    ],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    sharp_crew=True
)

# def kickoff(topic:str):
#     crew.memory = topic
#     return crew.kickoff(inputs={"topic":topic})

# kickoff("AI and Machine Learning")

inputs = {'topic': 'AI in healthcare'}
async_result = my_crew.kickoff(inputs=inputs)
print(async_result)