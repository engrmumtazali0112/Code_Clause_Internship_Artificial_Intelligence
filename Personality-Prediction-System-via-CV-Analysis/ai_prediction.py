import google.generativeai as genai

from prediction import personality_traits

# Ensure NLTK resources are downloaded


genai.configure(api_key="AIzaSyBt_NvKYLO0LbpV1l75HlVTgXXBv-tFJzo")
# proceed here for api key  https://makersuite.google.com/app/apikey

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

def chat(query):
    for _ in range(3):  # Retry up to 3 times
        try:
            response = model.generate_content([query])
            return response.text
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
    return "Sorry, I'm unable to assist at the moment."

def say(text):
    print(f"Luna: {text}")

def takeCommand():
    try:
        query = "Describe a candidate's personality if their traits are: " + ', '.join(f"{k}: {v}" for k, v in personality_traits.items())
        return query
    except Exception as e:
        return "Some error occurred. Sorry from Luna."

if __name__ == '__main__':
    query = takeCommand()
    response = chat(query)
    print(f"Luna: {response}")