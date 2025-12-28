from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# 仮の単語データ（後で高校入試レベルに差し替える）
# words = [
#     {"english": "apple", "japanese": "りんご"},
#     {"english": "study", "japanese": "勉強する"},
#     {"english": "run", "japanese": "走る"},
#     {"english": "book", "japanese": "本"},
#     {"english": "water", "japanese": "水"},
#     {"english": "music", "japanese": "音楽"},
#     {"english": "friend", "japanese": "友達"},
#     {"english": "school", "japanese": "学校"},
#     {"english": "happy", "japanese": "幸せな"},
#     {"english": "fast", "japanese": "速い"}
# ]

# JSONファイルから単語データを読み込む
with open("words.json", "r", encoding="utf-8") as f:
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