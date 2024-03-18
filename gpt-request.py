# import openai
# Get the key from the OpenAI web site
openai.api_key = "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"
model_id = "gpt-3.5-turbo"


# file_path = 'readmefiles/aadl-translator_README.txt'
# # Open the file in read mode ('r') and read its contents
# with open(file_path, 'r') as file:
#   content = file.read()

# # Instruct ChatGPT to use this file to answer the question
# question = "Below is the README file of a repository. From the README file content, please indicate the software architectures used in this repository. " + content
# messages = []
# # # Set the question to answer
# # cresponse = GetMessageMemory(question, messages)
# messages.append({"role": "user", "content": question})


# # messages = [ {"role": "user", "content": "Where was the last olympics held? Just tell me the year & country?"} ]

# # Call the API
# completion = openai.ChatCompletion.create(model=model_id, messages=messages)

# # Print the answer we received for the 1st question
# print(completion.choices[0].message.content)



# Function to save README content to a text file
def save_answer_to_file(repo_name, answer):
    # Creating directory if not exists
    if not os.path.exists('chatgpt_answers'):
        os.makedirs('chatgpt_answers')


    # Writing content to file
    with open(f'chatgpt_answers/{repo_name}_answer.txt', 'w') as file:
        file.write(answer)

# =====================================================================================
# =====================================================================================
# =====================================================================================


import os

def read_files_in_folder(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory.")
        return

    # Iterate over each file in the directory
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the current item is a file
        if os.path.isfile(file_path):
            print(f"Reading file: {file_path}")
            
            # Open and read the file
            with open(file_path, 'r') as file:
                content = file.read()
                question = "Below is the README file of a repository. From the README file content, please indicate the software architectures used in this repository. " + content
                messages = []
                # # Set the question to answer
                messages.append({"role": "user", "content": question})
                completion = openai.ChatCompletion.create(model=model_id, messages=messages)
                answer = completion.choices[0].message.content
                print(answer)
                file_name = file_name.split("_README.txt")[0]
                save_answer_to_file(file_name, answer)


folder_path = "readmefiles"
read_files_in_folder(folder_path)

