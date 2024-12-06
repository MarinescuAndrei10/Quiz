from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('static/quiz.json') as f:
    quiz_data = json.load(f)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/question')
def question():
    question_id = int(request.args.get('id', 0))  
    if question_id < len(quiz_data['quiz']):
        question_data = quiz_data['quiz'][question_id]
        return render_template('question.html', question=question_data, question_id=question_id)
    else:
        return "Nu mai sunt întrebări!", 404

@app.route('/api/quiz')
def get_quiz():
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
