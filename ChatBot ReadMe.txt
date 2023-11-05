===== ChatBot README =====

Introduction
This Python script implements a chatbot that provides answers to user questions using a knowledge base. The questions are based on the most common question/doubt received in the INCASÒL offices. The chatbot will support multiple languages, including Catalan, Spanish, and English (right now only Catalan is fully developed).

Users can interact with the chatbot by asking questions, and the chatbot will provide answers from the knowledge base. If the chatbot doesn't know the answer, it can provide 2 different answers:
For developers: The chatbot asks for the answer and saves them in the .json file.
For users: It provides a message telling that it didn't understand the question.

===== Prerequisites =====

- Python 3.x installed on your system.
- Import/Download numpy library.
- Import/Download unidecode library.
- Import/Download fuzzywuzzy library.
- Download the knowledge base JSON files for the desired languages (e.g., knowledge_base_cat.json, knowledge_base_esp.json, or knowledge_base_eng.json).

===== Getting Started =====

1. Clone or download the code from the repository.
2. Place your JSON files in the same directory as the script.
3. Open a terminal and navigate to the directory where the script is located.

===== Usage =====

- Run the script by executing in your terminal: python chatbot.py.
- The chatbot will ask you to select a language by typing 1, 2, or 3 for Catalan, Spanish, or English, respectively (right now only Catalan is fully developed).

  Selecciona idioma/Selecciona idioma/Select language:
  1. Català
  2. Español
  3. English
  Elije una opción (1/2/3):

- Once the language is selected, the chatbot will introduce itself and wait for your question/doubt.
- You can type questions, and the chatbot will attempt to find the best match in its knowledge base and provide a response.
- To exit the chatbot, type "quit."

===== Teaching the Chatbot =====

If the chatbot doesn't know the answer to your question, you can teach it a new response in the developer mode:

- When the chatbot says, "I don't know the answer. Can you teach me?" you can type a new answer.
- To skip teaching the chatbot, simply type "skip."
The new answer will be added to the knowledge base for future use. For the user mode, this is replaced by a message: "No te he entendido, formula nuevamente la pregunta de una forma distinta."

===== Important Notes =====

- Make sure to have the knowledge base JSON file for the selected language in the same directory.
- You can modify the knowledge base JSON files to add or edit questions and answers.
