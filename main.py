from flask import Flask
import requests
from flask import request

API_URL = "https://api-inference.huggingface.co/models/aychang/roberta-base-imdb"
API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def index():
    input_json = request.get_json(force=True)
    print('input_json')

    text = request.args.get("text")
    print(text)
    output = query({
            "inputs": str(text)
        })
    return output


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)