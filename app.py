from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    openai.api_type = "azure"
    openai.api_base = os.getenv("OPENAI_API_BASE")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        engine=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        messages=[{"role": "user", "content": user_message}]
    )
    return jsonify({'response': response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run()