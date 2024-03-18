import openai
# Get the key from the OpenAI web site
openai.api_key = "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"
model_id = "gpt-3.5-turbo"


file_path = 'samining/readmefiles/aadl-translator_README.txt'
# Open the file in read mode ('r') and read its contents
with open(file_path, 'r') as file:
  content = file.read()

# Instruct ChatGPT to use this file to answer the question
question = "Below is the README file of a repository. From the README file content, please indicate the software architectures used in this repository. " + content
messages = []
# # Set the question to answer
# cresponse = GetMessageMemory(question, messages)
messages.append({"role": "user", "content": question})


# messages = [ {"role": "user", "content": "Where was the last olympics held? Just tell me the year & country?"} ]

# Call the API
completion = openai.ChatCompletion.create(
model=model_id,
messages=messages
)

# Print the answer we received for the 1st question
print(completion.choices[0].message.content)
