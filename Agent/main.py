import streamlit as st
from crew import run_pipeline
from crewai import LLM
import os

os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"


def detect_language(code: str) -> str:
    c = code.lower()

    if "#include" in c and "printf" in c:
        return "c"
    if "#include" in c and ("std::" in c or "cout" in c):
        return "cpp"
    if "public static void main" in c:
        return "java"
    if "using system" in c or "namespace" in c:
        return "csharp"
    if "def " in c or "import " in c:
        return "python"

    return "text"


st.set_page_config(
    page_title="AI Code Review & Output Predictor",
    
    layout="wide"
)

st.markdown("""
<style>
.title {
    font-size: 34px;
    font-weight: 700;
}
.subtitle {
    color: #6b7280;
    margin-bottom: 20px;
}
.section {
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">AI Code Review & Output Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'Supports C, C++, Java, Python, and C#. '
    'Fixes bugs, explains exact changes, and predicts program output.'
    '</div>',
    unsafe_allow_html=True
)

if "input_code" not in st.session_state:
    st.session_state.input_code = ""

if "result" not in st.session_state:
    st.session_state.result = ""

st.subheader("Input Code")

st.text_area(
    label="Paste code",
    height=300,
    key="input_code",
    placeholder="Paste ANY wrong code here..."
)

col1, col2 = st.columns([1, 1])

with col1:
    run_btn = st.button("Analyze Code", use_container_width=True)

with col2:
    clear_btn = st.button("Clear", use_container_width=True)

if clear_btn:
    st.session_state.clear()
    st.rerun()

if run_btn:
    if not st.session_state.input_code.strip():
        st.warning("Please paste some code.")
    else:
        try:
            llm = LLM(
                model="groq/llama-3.3-70b-versatile",
                api_key=os.getenv("GROQ_API_KEY")
            )

            with st.spinner("Analyzing code..."):
                crew_output = run_pipeline(llm, st.session_state.input_code)

            st.session_state.result = str(crew_output)

        except Exception as e:
            st.error(e)

if st.session_state.result:
    lang = detect_language(st.session_state.input_code)

    st.markdown("### Analysis Result")
    st.caption(f"Detected Language: **{lang.upper()}**")

    result_text = st.session_state.result

    def extract(tag):
        if tag in result_text:
            return result_text.split(tag)[1].split(f"</{tag[1:]}")[0].strip()
        return ""

    final_code = extract("<FINAL_CODE>")
    expected_output = extract("<EXPECTED_OUTPUT>")
    what_fixed = extract("<WHAT_WAS_FIXED>")

    if final_code:
        st.subheader("Final Corrected Code")
        st.code(final_code, language=lang)

    if expected_output:
        st.subheader("Expected Output")
        st.code(expected_output)

    if what_fixed:
        st.subheader("What was fixed (Exact changes)")
        st.markdown(what_fixed)
