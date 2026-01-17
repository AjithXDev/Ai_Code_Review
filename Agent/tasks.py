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


def final_response_task(agent):
    return Task(
        description="""
You are a STRICT program analyzer.

Your responsibilities:
1. Provide the FINAL corrected FULL code
2. Predict the EXACT program output (dry run)
3. Explain EVERY fix clearly

MANDATORY RULES:
- NEVER use generic sentences
- NEVER say "No errors were found" if ANYTHING changed
- NEVER invent fixes
- If code was already correct, explicitly say: "No changes were required" AND explain WHY
- ALWAYS show exact:
  bug → fixed line → reason
- Preserve original programming language

 If corrected code differs from input in ANY way,
  you MUST list at least one fix.
- It is FORBIDDEN to say "No changes were required"
  if syntax, names, or structure were modified.

Return output in EXACT format ONLY:

<FINAL_CODE>
(corrected full code)
</FINAL_CODE>

<EXPECTED_OUTPUT>
(exact output after dry run)
</EXPECTED_OUTPUT>

<WHAT_WAS_FIXED>
1. Problem:
   (exact original wrong line)

   Fixed to:
   (exact corrected line)

   Reason:
   (why it was wrong – syntax / runtime / logic)

(Repeat for EVERY issue)

If NO issues:
- Write "No changes were required" and explain why code is correct.
</WHAT_WAS_FIXED>
""",
        expected_output="Strict corrected code, exact output, and detailed fix explanation",
        agent=agent
    )