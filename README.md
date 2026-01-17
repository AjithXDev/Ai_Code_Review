# AI Code Review & Output Predictor

An intelligent code analysis system that **detects bugs, fixes errors, explains exact changes, and predicts program output** using AI agents.  
This project is designed to correctly analyze **intentionally wrong programs**, not just valid code.

Supports **C, C++, Java, Python, and C#**.



## Key Features

- Detects syntax, logical, and runtime errors  
- Handles array out-of-bounds, wrong conditions, infinite loops, division by zero  
- Produces fully corrected working code  
- Explains **exact bug → fix → reason**  
- Predicts exact program output (dry-run analysis)  
- Strict analysis (no fake “No errors found”)  
- Clean and minimal Streamlit UI  
- Multi-agent reasoning using CrewAI  



## Technology Stack

- Python  
- Streamlit (UI)  
- CrewAI (Multi-Agent Framework)  
- Groq LLM (LLaMA 3.3)  
- Pydantic  
- dotenv  



## How the System Works

1. User pastes any code (even heavily wrong code)
2. Programming language is auto-detected
3. Multiple AI agents analyze the code:
   - Syntax Fix Agent  
   - Logic Validation Agent  
   - Runtime Error Agent  
   - Optimization Agent  
   - Final Response Coordinator  
4. System generates:
   - Fully corrected code  
   - Exact expected output  
   - Detailed explanation of every fix  
   

## Use Cases

- Debugging student programs  
- Learning why code fails  
- Interview preparation  
- Testing edge cases  
- AI code reasoning demonstrations  
- Academic / final year projects  


## Notes

- Code is not executed  
- Output is predicted via logical dry-run  
- Designed to work with wrong and unsafe programs  
- Clear button resets input and output cleanly  


## Future Enhancements

- Support for more languages  
- Step-by-step execution visualization  
- Code complexity analysis  
- Cloud deployment  
- Voice-based code input  

