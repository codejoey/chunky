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

