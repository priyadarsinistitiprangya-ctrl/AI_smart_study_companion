import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JdOCXyYQUJf6KspIxvRmvyeuYJ_ox2zdAigTevE1zX9A")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Explain Ohm's Law in simple words"
)

print(response.text)