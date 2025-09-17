import google.generativeai as genai

API_KEY = "AIzaSyASrFtvkpaPzEYFVlol-H7k51b-XQ6vAdI"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
response = chat.send_message("Hello")
print("Gemini:", response.text)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
import google.generativeai as genai

API_KEY = "AIzaSyASrFtvkpaPzEYFVlol-H7k51b-XQ6vAdI"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
response = chat.send_message("Hello")
print("Gemini:", response.text)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
