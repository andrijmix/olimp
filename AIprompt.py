from openai import OpenAI

def rate_code(code):

    api_key = ''

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be presented with a code, your task is to rate it on a scale from 1 to 10, "
                           "after scale , add your comment. Don't explain what the code does, I know it"
            },
            {
                "role": "user",
                "content": code
            }
        ],
        temperature=0.7,
        max_tokens=640,
        top_p=1
    )

    return response.choices[0].message.content


# sample_code = "your code here"
# result = rate_code(sample_code)
# print(result)
