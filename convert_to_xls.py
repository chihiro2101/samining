import os
import pandas as pd


def read_file_in_folder(folder_path, file_name):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory.")
        return ""
    
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path):
        print(f"Reading file: {file_path}")
        
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    else:
        return ""


readme_folder_path = "readmefiles"
chatgpt_folder_path = "chatgpt_answers"
input_file_name = "URLs.txt"
df = pd.DataFrame(columns=['URL', 'README', 'ChatGPTAnswer'])

with open(input_file_name, 'r') as f:
    urls = f.readlines()


for url in urls:
    github_url = url.split(",")[0].strip("\"")
    parts = github_url.split('/')
    if len(parts) < 2:
        continue
    # repo_owner = parts[-2]
    repo_name = parts[-1]
    readme_file_name = f'{repo_name}_README.txt'
    answer_file_name = f'{repo_name}_answer.txt'
    # import pdb;pdb.set_trace()
    readme_file = read_file_in_folder(readme_folder_path,readme_file_name)
    answer_file = read_file_in_folder(chatgpt_folder_path,answer_file_name)
    new_row = {'URL' : github_url, 'README' : readme_file, 'ChatGPTAnswer' : answer_file}
    # df = df.append(new_row, ignore_index=True)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# determining the name of the file
file_name = 'SAMining_Report.csv'
df.to_csv(file_name, index=False)
print('DataFrame is written to CSV File successfully.')
