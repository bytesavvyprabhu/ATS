import streamlit as st
from resume_text import pdf_text
from prompt_for_ATS import prompt
from Gemini_AI import genai_function

st.title("**Resume Analyzer**")
 
# Upload Resume
st.header("Upload Resume:")
resume_file = st.file_uploader("Choose Your Resume", type=["pdf", "docx"])

# Upload Job Description
st.header("Upload Job Description:")
job_desc_file = st.file_uploader("Choose Your Job Description or ", type=["pdf", "docx"])

job_desc_text = st.text_area("Enter your Job Description here:")

if st.button("Analyze"):
    if resume_file is not None and job_desc_file is not None:
        resume_text = pdf_text(resume_file,'rb')
        jd_text_file = pdf_text(job_desc_file,'rb')
        prompt = prompt(resume_text, jd_text_file)
        response = genai_function(prompt)
        st.text_area(response)
    elif resume_file is not None and job_desc_text is not None:
        resume_text = pdf_text(resume_file,'rb')
        prompt = prompt(resume_text, job_desc_text)
        response = genai_function(prompt)
        st.text_area(response)
    else:
        st.warning("Please upload both resume and job description files.")

