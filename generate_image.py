import openai

openai.api_key = "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"

def get_image_url(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return response['data'][0]['url']
