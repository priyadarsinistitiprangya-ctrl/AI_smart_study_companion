import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
st.set_page_config(
    page_title="AI Smart Study Companion",
    page_icon="📚",
    layout="wide"
)

# Gemini Configuration
genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# App Title
st.title("AI Smart Study Companion")
st.markdown(
    "Upload study material and generate summaries, flashcards, MCQs and important questions."
)
with st.sidebar:
    st.header("About")
    st.write(
        "AI-powered study assistant for students."
    )

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
difficulty = st.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

if uploaded_file is not None:

    # Read PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.success("PDF uploaded successfully!")
    word_count = len(text.split())

    st.metric("Words in PDF", word_count)
    st.metric("Characters", len(text))

    st.subheader("Extracted Text")
    st.text_area("PDF Content", text, height=300)

    # Generate Summary
    if st.button("Generate Summary"):

        prompt = f"""
You are an expert teacher.

Summarize the following study material.

Provide:

1. Executive Summary
2. Key Concepts
3. Important Points

Study Material:

{text}
"""

        with st.spinner("Generating summary..."):
            response = model.generate_content(prompt)

        st.subheader("AI Summary")
        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)

    # Generate Flashcards
if st.button("Generate Flashcards"):

        prompt = f"""
Generate 15 study flashcards.

Format:

Question:
Answer:

Study Material:

{text}
"""

        with st.spinner("Generating flashcards..."):
            response = model.generate_content(prompt)

        st.subheader("Flashcards")
        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)
    
    # Generate MCQs
if st.button("Generate MCQs"):

        prompt = f"""
Generate 10 {difficulty} level multiple choice questions.

For each question provide:

Question
A
B
C
D
Correct Answer

Study Material:

{text}
"""

        with st.spinner("Generating MCQs..."):
            response = model.generate_content(prompt)

        st.subheader("MCQs")
        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)

    # Important Questions
if st.button("Important Questions"):

        prompt = f"""
You are a university examiner.

Generate:

5 Short Questions
5 Long Questions

Based on:

{text}
"""

        with st.spinner("Generating questions..."):
            response = model.generate_content(prompt)

        st.subheader("Important Questions")
        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)

    # Revision Plan
if st.button("Revision Plan"):

        prompt = f"""
Create a 7-day revision plan.

Include:
Day Number
Topics
Study Time
Revision Activity

Study Material:

{text}
"""

        with st.spinner("Creating revision plan..."):
            response = model.generate_content(prompt)

        st.subheader("Revision Plan")
        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)

    # Chat With PDF
st.subheader("Chat With PDF")

user_question = st.text_input(
        "Ask a question about the uploaded PDF"
    )

if st.button("Ask AI"):

        prompt = f"""
Answer the question using ONLY the uploaded document.

If the answer is not found, say:

Information not found in uploaded document.

Question:
{user_question}

Document:
{text}
"""

        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)

        st.write(response.text)
        st.download_button(
    "Download Result",
    response.text,
    file_name="study_output.txt"
)