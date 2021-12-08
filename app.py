from get_response import *
from flask import Flask, render_template, request

from lang_pred import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get', methods=['POST'])
def get_bot_response():
    userMessage = request.get_data().decode("utf-8")

    language = predict(userMessage)

    print(language)

    if(language == "English"):
        return get_response(userMessage)
    if(language == "French"):
        return get_response_1(userMessage)

    return get_response_1(userMessage) 


if __name__ == "__main__":
    app.run(debug=True)
      