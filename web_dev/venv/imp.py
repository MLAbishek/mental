from groq import Groq
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(__file__), "..", "templates")

@app.route('/')
def start():
    return render_template('start.html')

def draft_message(content, role='user'):
    return {
        "role": role,
        "content": content
    }

api_key = "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"
client = Groq(api_key=api_key)

messages = [
    {
        'role': 'system',
        'content': "talk like he is your best friend dont tell him you are an ai dont speak for too long"
    }
]

@app.route('/ask', methods=['POST'])
def predict():
    prompt = request.form['messageText']
    messages.append(draft_message(prompt))
    chat_completion = client.chat.completions.create(
        temperature=1.0,
        model="mixtral-8x7b-32768",
        max_tokens=10000,
        messages=messages
    )
    response = chat_completion.choices[0].message.content
    return jsonify({'answer': response})

if __name__ == "__main__":
    app.run(debug=True)