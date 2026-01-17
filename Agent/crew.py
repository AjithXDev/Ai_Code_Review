from crewai import Crew
from agents import create_agent
from tasks import (
    syntax_fix_task,
    logic_validation_task,
    performance_optimization_task,
    final_response_task
)

def run_pipeline(llms, user_code):
    syntax_agent, logic_agent, performance_agent, response_agent = create_agent(llms)

    tasks = [
        syntax_fix_task(syntax_agent, user_code),
        logic_validation_task(logic_agent, user_code),
        performance_optimization_task(performance_agent, user_code),
        final_response_task(response_agent)
    ]

    crew = Crew(
        agents=[
            syntax_agent,
            logic_agent,
            performance_agent,
            response_agent
        ],
        tasks=tasks,          
        verbose=True
    )

    return crew.kickoff()
