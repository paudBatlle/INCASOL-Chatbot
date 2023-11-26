import json
import os
import sys

# Get input from the user
arxiu = input("Escriu en nom de l'arxiu/Enter the filename (e.g., test.json): ")

# Check if the file exists
if not os.path.isfile(arxiu):
    print(f"Error: The file {arxiu} does not exist/L'arxiu no existeix.")
    sys.exit()
else:  
    codi_de_resposta = input("Escriu el codi de pregunta/ Enter the response code (e.g., 0): ")
    nova_resposta = input("Escriu la nova resposta/Enter the new answer: ")

    # Check if the response code is a number
    if not codi_de_resposta.isdigit():
        print("Error: El codi ha de ser un número/The response code should be a number.")
        sys.exit()
    else:
        codi_de_resposta = int(codi_de_resposta)

        # Read JSON data from the file
        with open(arxiu, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        # Update answer for the specified code
        code_exists = False
        for question in json_data["questions"]:
            if question["code"] == str(codi_de_resposta):
                question["answer"] = nova_resposta
                code_exists = True

        if not code_exists:
            print(f"Error: El codi {codi_de_resposta} no s'ha trobat / Response code {codi_de_resposta} not found in the file.")
            sys.exit()

        # Write the updated data back to the file
        with open(arxiu, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2)

        print("Update completed. Check the file:", arxiu)
