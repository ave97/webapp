from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # WebSockets για real-time επικοινωνία

# Ερωτήσεις του Quiz
questions = [
    {"question": "Ποια είναι η πρωτεύουσα της Γαλλίας;", "options": ["Λονδίνο", "Παρίσι", "Ρώμη"], "answer": "Παρίσι"},
    {"question": "Πόσα πόδια έχει μια γάτα;", "options": ["2", "4", "6"], "answer": "4"},
]

@app.route("/")
def index():
    return render_template("main.html")  # Στέλνει το HTML στους χρήστες

@socketio.on("get_question")
def send_question(data):
    question_id = data["id"]
    if 0 <= question_id < len(questions):
        socketio.emit("new_question", questions[question_id])  # Στέλνουμε νέα ερώτηση σε όλους

if __name__ == "__main__":
    socketio.run(app, debug=True)
