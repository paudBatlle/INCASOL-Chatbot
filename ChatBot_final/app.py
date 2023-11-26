from flask import Flask, render_template, request, jsonify
import json
import unidecode
from fuzzywuzzy import fuzz

app = Flask(__name__)

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data

def preprocess_text(text: str) -> str:
    return unidecode.unidecode(text.lower())

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    user_question_normalized = preprocess_text(user_question)
    best_match = None
    best_score = 0
    
    for question in questions:
        question_normalized = preprocess_text(question)
        similarity_score = fuzz.ratio(user_question_normalized, question_normalized)
        
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = question
    
    if best_score >= 70:
        return best_match
    else:
        return None

def get_answers_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    opcion = request.form['opcion']

    if opcion == '1':
        knowledge_base: dict = load_knowledge_base('knowledge_base_cat.json')
    elif opcion == '2':
        knowledge_base: dict = load_knowledge_base('knowledge_base_esp.json')
    elif opcion == '3':
        knowledge_base: dict = load_knowledge_base('knowledge_base_eng.json')
    else:
        knowledge_base: dict = load_knowledge_base('knowledge_base_cat.json')

    questions = [q["question"] for q in knowledge_base["questions"]]
    best_match: str | None = find_best_match(user_message, questions)

    if best_match:
        bot_response: str = get_answers_for_question(best_match, knowledge_base)
    else:
        if opcion == '1':
            bot_response = "Ho sento, no t'he entès. Repeteix la teva pregunta d'una altra forma"
        elif opcion == '2':
            bot_response = "Lo siento, no te he entendido. Repite tu pregunta de otra forma"
        elif opcion == '3':
            bot_response = "I'm sorry, I cannot understand you"
        else:
            bot_response = "No t'he entès, repeteix la teva pregunta"

        

    user_photo = "https://example.com/user_photo.jpg"
    bot_photo = "https://example.com/bot_photo.jpg"

    response_data = {
        'user_message': user_message,
        'bot_response': bot_response,
        'user_photo': user_photo,
        'bot_photo': bot_photo
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

