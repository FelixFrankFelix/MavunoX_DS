from openai import OpenAI

client = OpenAI(api_key='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')


#value = random.randint(0,5)
def rec_gen(factor, min,max,value,unit, crop):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a recommender for rural farmers. only use block of text in 55 words strictly and make responses dynamic"},
        {"role": "user", "content": f"Provide a recommendation to improve yield based on {factor}. The recommended {factor} is {min}-{max} {unit}, and the farm is currently at {value} {unit}. In just 55 words, assess if the current {factor} is suitable for optimal yield and add strategies to improve yield specific for the crop {crop}, recommendation should be block of text and simplified, approximate to 2 decimal places for all numbers in responds"},
    ]

    )
    return completion.choices[0].message.content

