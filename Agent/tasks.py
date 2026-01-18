from crewai import Task

def syntax_fix_task(agent, user_code):
    return Task(
        description=f"""
        You are a senior software engineer.

        Tasks:
        - Fix syntax errors
        - Fix indentation issues
        - Resolve undefined variables
        - Fix basic runtime errors

        Rules:
        - Do NOT optimize the code
        - Do NOT change the intended logic
        - Do NOT add new features

        Return ONLY the corrected code.

        Code:
        {user_code}
""",
        expected_output="Executable and stable version of the code.",
        agent=agent
    )



def logic_validation_task(agent, user_code):
    return Task(
        description=f"""
You are an expert algorithm engineer.

Tasks:
- Validate logical correctness
- Fix incorrect conditions and control flow
- Handle edge cases properly

Rules:
- Preserve original algorithm exactly
- Do NOT reduce time complexity
- Do NOT remove redundant loops
- Only fix incorrect conditions if they cause wrong execution

Return ONLY the logically correct code.

Code:
{user_code}
""",
        expected_output="Logically correct version of the code.",
        agent=agent
    )


def performance_optimization_task(agent, user_code):
    return Task(
        description=f"""
You are a performance optimization expert.

Tasks:
- Improve time and space efficiency
- Simplify logic where possible
- Remove redundant operations

Rules:
- Only micro-optimizations allowed (formatting, minor cleanup)
- Do NOT change loop boundaries
- Do NOT change algorithm structure



Return ONLY the optimized code.

Code:
{user_code}
""",
        expected_output="Optimized version of the code with identical output.",
        agent=agent
    )



from crewai import Task

def final_response_task(agent):
    return Task(
        description="""
You are a PROGRAM EXECUTION ANALYZER.

Your ONLY responsibilities:
1. Produce a FINAL, RUNNABLE version of the input code
2. Predict the EXACT output produced by the program (dry run)

RULES (VERY IMPORTANT):
- Preserve the original programming language
- Fix ONLY what is required to make the code run correctly
- DO NOT explain fixes
- DO NOT describe changes
- DO NOT add comments unless required for execution
- DO NOT hardcode outputs
- DO NOT invent behavior
- If code has print/printf/output → ALWAYS predict output
- If output repeats → repeat lines explicitly
- If infinite → say "Infinite output"

ABSOLUTELY FORBIDDEN:
- What was fixed
- Why it was fixed
- Best practices
- Explanations
- Generic text

RETURN OUTPUT IN THIS EXACT FORMAT ONLY:

<FINAL_CODE>
(correct runnable code)
</FINAL_CODE>

<EXPECTED_OUTPUT>
(exact output line by line)
</EXPECTED_OUTPUT>
""",
        expected_output="Runnable final code and exact predicted output",
        agent=agent
    )
