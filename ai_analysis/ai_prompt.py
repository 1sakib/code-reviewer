"""OpenAI Module for AI Analysis and Review."""
from openai import OpenAI

APIKEY = (
    "ENTER OPENAI API KEY HERE"
)

client = OpenAI(api_key=APIKEY)


def ai_prompt(user_input, prompt, temp, model):
    """Generate AI response based on user input, system prompt, AI model, and
    temperature of the response."""
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=temp
    )
    return completion.choices[0].message.content
