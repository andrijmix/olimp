import os


def read_text_files(folder_path, extensions):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as f:
                        print(f"Content of {file_path}:")
                        print(f.read())
                        input("Press Enter to continue...")
                        print("\n\n\n\n==================================")


