from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

with open("questions.json", "r", encoding="utf-8") as f:
    questions_by_theme = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", themes=questions_by_theme.keys())

@app.route("/quiz", methods=["POST"])
def quiz():
    theme = request.form["theme"]
    question = random.choice(questions_by_theme[theme])
    return render_template("quiz.html", question=question, theme=theme)

@app.route("/answer", methods=["POST"])
def answer():
    selected = request.form["option"]
    correct = request.form["correct"]
    theme = request.form["theme"]
    result = "✅ Bonne réponse !" if selected == correct else f"❌ Mauvaise réponse. La bonne était : {correct}"
    return render_template("result.html", result=result, theme=theme)

if __name__ == "__main__":
    app.run(debug=True)
