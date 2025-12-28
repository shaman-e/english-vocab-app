from flask import Flask, render_template, request
import os
import json
import random

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDS_PATH = os.path.join(BASE_DIR, "words.json")

# JSONファイルから単語データを読み込む
with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    quiz_words = random.sample(words, 10)
    return render_template("quiz.html", quiz_words=quiz_words)

@app.route("/result", methods=["POST"])
def result():
    user_answers = request.form
    results = []

    for i in range(10):
        japanese = user_answers.get(f"japanese_{i}")
        correct = user_answers.get(f"correct_{i}")
        answer = user_answers.get(f"answer_{i}")

        results.append({
            "japanese": japanese,
            "correct": correct,
            "answer": answer,
            "is_correct": (correct.lower() == answer.lower())
        })

    return render_template("result.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)