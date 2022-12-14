import os
import openai

openai.api_key = os.environ.get('OPENAPIKEY')


def get_response_openai(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response["choices"]
