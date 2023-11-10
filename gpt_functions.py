# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# iniating client object/communication with OpenAI
client = OpenAI()

# this is the prompt template
system_message="""As a baby name consultant, your expertise lies in crafting personalized suggestions. Your task is to generate 5 unique names for a
child, you'll need specific details such as cultural gender, background, theme preferences (e.g., classic, modern), sound preferences, religious
context, family heritage, personal meanings, sibling name compatibility, preferred name length, language, tribe and nationality.

You should give a 1-2 sentence summary below each name as for why each name would be suitable.
Avoid saying that the name is fitting or suitable for the child because of any of the specific details provided. 

Instead, provide unique insights into each name, considering all of the provided details. Not all of the above specific details might be provided so work with all of the user details given below.

your response should be in the format:

1. Name.\n

   Sentence 1.\n
   Sentence 2.

2. Name.\n

   Sentence 1.\n
   Sentence 2.

3. Name.\n

   Sentence 1.\n
   Sentence 2.

4. Name.\n

   Sentence 1.\n
   Sentence 2.

5. Name.\n

   Sentence 1.\n
   Sentence 2.
"""

input_template = """details from user:
cultural_background={},theme_preferences={},sound_preferences={},religious_context={},family_heritage={},personal_meaning={},
sibling_compatibility={},name_length={}, language={}, tribe={}, gender={}, nationality={}
"""


def create_prompt(cultural_background, theme_preferences, sound_preferences, religious_context, family_heritage, personal_meaning, sibling_compatibility, name_length, language, tribe, gender, nationality):
    # Replace the placeholders in the template with the provided values
    prompt = input_template.format(
        cultural_background,
        theme_preferences,
        sound_preferences,
        religious_context,
        family_heritage,
        personal_meaning,
        sibling_compatibility,
        name_length,
        language,
        tribe,
        gender,
        nationality
    )

    return prompt


def generate_name_suggestions(cultural_background="", theme_preferences="", sound_preferences="", religious_context="", family_heritage="", personal_meaning="", sibling_compatibility="", name_length="", language="", tribe="", gender="", nationality=""):
    user_prompt = create_prompt(cultural_background, theme_preferences, sound_preferences, religious_context, family_heritage, personal_meaning, sibling_compatibility, name_length, language, tribe, gender, nationality)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": system_message
            },
            {
            "role": "user",
            "content" : user_prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return [response, user_prompt]