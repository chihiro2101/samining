import os

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

def detect_insufficient_readme_files(folder_path):
    insufficient_files = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            readme_content = file.read()
            if not is_sufficient_for_architecture_extraction(readme_content):
                insufficient_files.append(file_path)
                print("File name:", file_name)
                print("README Content:")
                print(readme_content)
                print("===============================================================================================================================================================")
                print()
                print()

    return insufficient_files

folder_path = "readmefiles"
insufficient_files = detect_insufficient_readme_files(folder_path)

if insufficient_files:
    print("The following README files may not contain enough information for architecture extraction:")
    for file_path in insufficient_files:
        print(file_path)
else:
    print("All README files seem to contain sufficient information for architecture extraction.")
