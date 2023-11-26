import json
import unidecode
import numpy as np
from fuzzywuzzy import fuzz


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def preprocess_text(text: str) -> str:
    # Normalize text by removing accents and converting to lowercase
    return unidecode.unidecode(text.lower())

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    user_question_normalized = preprocess_text(user_question)
    
    # Use fuzzy matching to find the best match
    best_match = None
    best_score = 0
    
    for question in questions:
        question_normalized = preprocess_text(question)
        similarity_score = fuzz.ratio(user_question_normalized, question_normalized)
        
        if similarity_score > best_score:
            best_score = similarity_score
            best_match = question
    
    if best_score >= 70:  # Adjust the threshold as needed
        return best_match
    else:
        return None

def get_answers_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    print("Selecciona idioma/Selecciona idioma/Select language:")
    print("1. Català")
    print("2. Español")
    print("3. English")

    opcion = input("Elije una opción (1/2/3): ")

    if opcion == '1':
        print(f'Sóc l\'assistent virtual d\'INCASÒL, com et puc ajudar?')
        knowledge_base: dict = load_knowledge_base('knowledge_base_cat.json')
    elif opcion == '2':
        print(f'Soy el asistente virtual de INCASÒL, ¿cómo puedo ayudarte?')
        knowledge_base: dict = load_knowledge_base('knowledge_base_esp.json')
    elif opcion == '3':
        print(f'I am the virtual assistant of INCASÒL, how can I assist you?')
        knowledge_base: dict = load_knowledge_base('knowledge_base_eng.json')
    else:
        print("Opció no vàlida. Seleccionat Català per defecte.")
        knowledge_base: dict = load_knowledge_base('knowledge_base_cat.json')

    questions = [q["question"] for q in knowledge_base["questions"]]
    
    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, questions)

        if best_match:
            answer: str = get_answers_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print(f'No t\'he entes, repeteix la teva pregunta')
        '''
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer. lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                if opcion == '1':
                    save_knowledge_base('knowledge_base_cat.json', knowledge_base)
                elif opcion == '2':
                    save_knowledge_base('knowledge_base_esp.json', knowledge_base)
                elif opcion == '3':
                    save_knowledge_base('knowledge_base_eng.json', knowledge_base)
                else:
                    save_knowledge_base('knowledge_base_esp.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')
        '''        
        
if __name__ == '__main__':
    chat_bot()
