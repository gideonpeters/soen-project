from openai import OpenAI

OPENAI_API_KEY='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'

client = OpenAI(
  api_key=OPENAI_API_KEY 
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt }]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # temperature=1,
    )
    return response.choices[0].message.content

text = f"""
	
def greatest_common_divisor(a: int, b: int) -> int: 
    
Return a greatest common divisor of two integers a and b >>> greatest_common_divisor(3, 5) 1 >>> greatest_common_divisor(25, 15) 5

"""

prompt = f"""
Generate the code for the description below:

```{text}```
"""

response = get_completion(prompt)
print(response)