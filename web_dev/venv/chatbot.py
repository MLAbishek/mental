from groq import Groq
import os
from flask import Flask,render_template,request
app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(__file__), "..", "templates")
@app.route('/')
def start():
    return render_template('start.html')
def predict():
    pass
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
    run=True
    while run:
        prompt=input("what u want to speak:")
        if prompt.lower()!="bye":

            messages.append(draft_message(prompt))
            chat_completion=client.chat.completions.create(
                temperature=1.0,
                model="mixtral-8x7b-32768",
                max_tokens=10000,
                messages=messages
            )
            chat_completion.usage.total_tokens
            print(chat_completion.choices[0].message.content)
        else:
            run=False
            print("Thank you!")
if __name__=="__main__":
    app.run(debug=True)
