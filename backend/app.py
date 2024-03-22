from flask import Flask, render_template, request, session, jsonify
import os
import openai
from flask_cors import CORS
from llm_agent import get_llm_response

app = Flask(__name__)
CORS(app)


@app.route("/generate-text", methods=["POST"])
def generate_text():
    data = request.get_json()
    topic = data["topic"]
    description = data["description"]
    wordcount = data["wordCount"]
    isLiveSearchEnabled = data["isLiveSearchEnabled"]
    result = get_llm_response(topic, description, wordcount, isLiveSearchEnabled)
    print(result)
    return jsonify({"result": result})


@app.route("/post-social", methods=["POST"])
def post_social():
    data = request.get_json()
    # RPA code here

    # return jsonify({"result": result})


if __name__ == "__main__":
    app.run()
