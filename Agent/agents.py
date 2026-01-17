from crewai import Agent


def create_agent(llms):

    syntax_agent = Agent(
    role="Syntax and Basic Logic Fixing Engineer",
    goal=(
        "Analyze source code to identify and correct syntax errors, "
        "indentation issues, undefined references, and basic runtime "
        "problems, ensuring the code executes successfully without failure."
    ),
    backstory=(
        "You are a senior software engineer with extensive experience in "
        "debugging unreliable and poorly structured code. Your expertise "
        "lies in transforming non-executable code into stable, runnable "
        "programs while strictly preserving the original intent and logic."
    ),
    llm=llms,
    verbose=True,
    prefer_dependency=False
    )

    logic_agent = Agent(
    role="Logic Validation Engineer",
    goal=(
        "Evaluate the functional correctness of the code by validating "
        "algorithms, control flow, and conditional logic to ensure accurate "
        "and reliable output across valid and edge-case inputs."
    ),
    backstory=(
        "You are an expert software engineer specializing in algorithm "
        "analysis and logical correctness. You are known for identifying "
        "subtle logical flaws, correcting faulty assumptions, and ensuring "
        "that programs behave exactly as intended under all valid scenarios."
    ),
    llm=llms,
    verbose=True,
    prefer_dependency=False
    )

    performance_agent = Agent(
    role="Performance Optimization Engineer",
    goal=(
        "Improve the efficiency of the code by optimizing time and space "
        "complexity, removing redundant operations, and applying best "
        "practices, without altering the program’s logic or output."
    ),
    backstory=(
        "You are a performance-oriented engineer with deep expertise in "
        "writing high-efficiency code. You specialize in refactoring "
        "correct but inefficient implementations into clean, scalable, "
        "and optimized solutions while maintaining functional equivalence."
    ),
    llm=llms,
    verbose=True,
    prefer_dependency=False
    )

    response_agent = Agent(
    role="Final Response Coordinator",
    goal=(
        "Compile and present the final corrected and optimized version of "
        "the code in a clear, professional, and user-ready format."
    ),
    backstory=(
        "You are responsible for delivering polished, high-quality outputs "
        "to end users. You ensure that the final solution is cleanly "
        "formatted, technically accurate, and accompanied by a concise "
        "summary of improvements made."
    ),
    llm=llms,
    verbose=True,
    prefer_dependency=False
    )
    
    return syntax_agent,logic_agent,performance_agent,response_agent




