import google.generativeai as genai


GOOGLE_API_KEY=''

genai.configure(api_key=GOOGLE_API_KEY)

def genai_function(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

