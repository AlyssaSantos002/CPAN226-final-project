from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

# #To load from .env
load_dotenv()

#API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

#function
def ask_ai(request):
    response_text = ""

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful AI assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                response_text = response['choices'][0]['message']['content']
                print(f"\nQuestion: {prompt}")
                print(f"Answer: {response_text}\n")

            except Exception as e:
                response_text = f"Error: {e}"
                print(f"\n Error: {e}")


        return render(request, "home.html", {"response_text": response_text})


