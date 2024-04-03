from groq import Groq
def draft_message(content,role='user'):
    return{
        "role":role,
        "content":content
    }
api_key="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"
client=Groq(api_key=api_key)
messages=[
    {
        'role':'system',
        'content':"just talk like a friend"
    }
]
prompt=input("what u want to speak:")
messages.append(draft_message(prompt))
chat_completion=client.chat.completions.create(
    temperature=1.0,
    model="mixtral-8x7b-32768",
    max_tokens=10000,
    messages=messages
)
chat_completion.usage.total_tokens
print(chat_completion.choices[0].message.content)
