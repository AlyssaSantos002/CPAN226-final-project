from django.shortcuts import render, redirect
import openai
import os
from dotenv import load_dotenv

# #To load from .env
load_dotenv()

# API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


# function
def ask_ai(request):
    response_text = ""
    question = ""


    if request.method == "POST":
        if "clear" in request.POST:
            return render(request, "home.html", {"response_text": "", "question":""})

        prompt = request.POST.get("prompt", "").strip()
        question = prompt

        if not prompt:
            response_text = "Please enter a question."
        elif len(prompt) > 1000:
            response_text = "Your question is too long. Try to shorten it."
        else:
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

    return render(request, "home.html", {"response_text": response_text, "question":question})
