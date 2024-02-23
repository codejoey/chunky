from openai import OpenAI
import key_param
import os
os.environ['OPENAI_API_KEY'] = key_param.openai_api_key

client = OpenAI()

def generate_embedding(text_chunk):
    response = client.embeddings.create(input=text_chunk, model="text-embedding-ada-002")
    print(response)  # Temporarily add this to inspect the structure
    # Adjust the attribute access based on the structure you observe
    embedding_vector = response.data[0].embedding
    return embedding_vector


from openai import OpenAI

text = """Older adults form a fast-increasing proportion of the world population. However, gains in increasing quantity of life have not been accompanied by similar gains in quality of life. Older people frequently experience frailty, memory problems, and chronic diseases including cardiovascular disease (CVD) and neurodegenerative diseases. Recent trials have demonstrated the efficacy of anti-hypertensive therapy in older populations but failed to show benefits for aspirin. Statins clearly reduce CVD events in middle-aged populations. There seems to be evidence that the effect is similar in primary prevention older populations based on meta-analyses mainly from sub-groups in large trials, but this becomes less clear with increasing age. However, given differences in drug metabolism and possibly efficacy, competing co-morbidities, their effects on mortality, disability, and dementia in this age group remain to be determined."""
system = [{"role": "system", "content": "You are Summary AI."}]
user = [{"role": "user", "content": f"Summarize this briefly:\n\n{text}"}]
chat_history = []  # past user and assistant turns, for AI memory

chat_completion = client.chat.completions.create(
  messages = system + chat_history + user,
  model="gpt-3.5-turbo",
  max_tokens=500, top_p=0.9,
  )
print(chat_completion.choices[0].message.content)


def generate_summary(text_chunk):
    system = [{"role": "system", "content": "You are Summary AI."}]
    user = [{"role": "user", "content": f"Summarize this briefly:\n\n{text_chunk}"}]
    chat_history = []  # past user and assistant turns, for AI memory

    chat_completion = client.chat.completions.create(
    messages = system + chat_history + user,
    model="gpt-3.5-turbo",
    max_tokens=500, top_p=0.9,
    )
    return(chat_completion.choices[0].message.content)

