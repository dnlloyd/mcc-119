import os

# For Open AI, I'll alow you to use the OpenAI library in place of requests
from openai import OpenAI


# Read my API key from an environment variable
# ex: export MY_OPENAI_KEY=abcdefgthismyfakekey123
api_key = os.environ["MY_OPENAI_KEY"]

# Initialize the API client with my project, org, and API key
client = OpenAI(
  api_key=api_key,
  organization='org-oLSiLGf4uvhkmhyi3zUWtGGc',
  project='proj_OFRxxr9nwQzP0lGw2nwNBPmS',
)

# Define all my content modifier strings
neutral_modifier = "You are a helpful assistant."
sarcastic_modifier = "You are a helpful assistant that answers questions sarcastically and a bit snarky"
professional_modifier = "You are a helpful assistant that answers questions overly professional"
concise_modifier = "You are a helpful assistant that answers questions extremely concise and succinct"
emotional_modifier = "You are an emotionally unstable assistant that tends to be a little mean"
poetic_modifier = "You are an emotionally unstable assistant that answers all questions in the form of a poem"

# Prompt the user for type of modifier
phrase_modifier = input("How would you like me to paraphrase your content?\n1) sarcastic\n2) more professional\n3) more concise\n4) emotionally unstable\n5) more poetic\n> ")
# Prompt the user for content to be modified
user_content = input("Enter your sentence or paragraph:\n")

# Set modifier
match phrase_modifier:
  case "1":
    system_content = sarcastic_modifier
  case "2":
    system_content = professional_modifier
  case "3":
    system_content = concise_modifier
  case "4":
    system_content = emotional_modifier
  case "5":
    system_content = poetic_modifier
  case _:
    system_content = neutral_modifier

# Make the API call to Open AI
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": system_content},
    {"role": "user", "content": f"Rephrase the following paragraph: {user_content}"}
  ]
)

# Print the output
print("")
print(completion.choices[0].message.content)
