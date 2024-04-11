import openai
import os
openai.api_key = "api-key"
model_id = "gpt-3.5-turbo"


def is_sufficient_for_architecture_extraction(readme_content):
    # Heuristic 1: Minimum length threshold
    if len(readme_content) > 100:  # Adjust threshold as needed
        return True

    # Heuristic 2: Presence of keywords
    architecture_keywords = ["architecture", "design", "component", "module", "layer", "pattern", "framework"]
    if any(keyword in readme_content.lower() for keyword in architecture_keywords):
        return True

    # Heuristic 3: Linking to external resources
    if "http" in readme_content:
        return True

    return False

def save_answer_to_file(repo_name, answer):
    if not os.path.exists('chatgpt_answers'):
        os.makedirs('chatgpt_answers')

    with open(f'chatgpt_answers/{repo_name}_answer.txt', 'w') as file:
        file.write(answer)


def read_files_in_folder(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory.")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            print(f"Reading file: {file_path}")
            
            with open(file_path, 'r') as file:
                content = file.read()
                if is_sufficient_for_architecture_extraction(content):
                    # question = "Below is the README file of a repository. Is it following a model-view-controller (MVC) architecture, a layered architecture, a microservices architecture, a service-oriented architecture (SOA), or another architecture? From the README file content, please indicate the software architectures used in this repository. Skip explanations and use a comma-separated format like this: software architecture, another software architecture, another software architecture, etc. \n" + content
                    question = "Below is the README file of a repository. From the README file content, please indicate the software architectures used in this repository. Skip explanations and use a comma-separated format like this: software architecture, another software architecture, another software architecture, etc. \n" + content                    
                    messages = []
                    messages.append({"role": "user", "content": question})
                    completion = openai.ChatCompletion.create(model=model_id, messages=messages, max_tokens=20)
                    answer = completion.choices[0].message.content
                    print(answer)
                    file_name = file_name.split("_README.txt")[0]
                    save_answer_to_file(file_name, answer)


folder_path = "readmefiles"
read_files_in_folder(folder_path)

