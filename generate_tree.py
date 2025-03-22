import os

# Define folders to exclude
EXCLUDE_FOLDERS = {'.git', '.idea', '__pycache__', '.venv', 'venv', 'node_modules'}


def generate_tree_structure(root_dir, indent=""):
    structure = ""
    items = sorted(os.listdir(root_dir))

    for index, item in enumerate(items):
        path = os.path.join(root_dir, item)

        # Skip unwanted files and folders
        if item in EXCLUDE_FOLDERS or item.startswith('.'):
            continue

        is_last = (index == len(items) - 1)
        prefix = "└── " if is_last else "├── "

        structure += f"{indent}{prefix}{item}\n"

        if os.path.isdir(path):
            new_indent = indent + ("    " if is_last else "│   ")
            structure += generate_tree_structure(path, new_indent)

    return structure


# Set your framework root directory here
root_directory = "D:/python/PythonProject3"  # Change to your actual path

print(f"{os.path.basename(root_directory)}/")
print(generate_tree_structure(root_directory))
