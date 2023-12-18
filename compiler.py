import os
import subprocess

from settings import directory_to_compile, сpp_compiler_path, number_of_test_cases, pas_compiler_path, cs_compiler_path


from showFile import read_text_files


def compile_cs_files_in_directory(directory_path, csc_path):
    try:
        # Iterate through all directories and subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".cs"):
                    cs_file_path = os.path.join(root, file)
                    exe_file_path = os.path.splitext(cs_file_path)[0] + ".exe"

                    # Compilation of .cs file into .exe
                    process = subprocess.run([csc_path, '/out:' + exe_file_path, cs_file_path],
                                             capture_output=True, text=True, shell=True)

                    # Checking the compilation result
                    if process.returncode == 0:
                        print(f"File {file} successfully compiled into {os.path.basename(exe_file_path)}")
                    else:
                        print(f"An error occurred during compilation of {file}:")
                        print(process.stderr)

    except FileNotFoundError:
        print("C# compiler not found.")
    except Exception as e:
        print("An error occurred:", e)


def create_compile_bat_pas(root_dir, compiler_path):
    with open('compile_files_pas.bat', 'w') as bat_file:
        for foldername, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.pas'):
                    abs_path = os.path.abspath(os.path.join(foldername, filename))
                    bat_file.write(f'"{compiler_path}" {abs_path}\n')


def create_compile_bat_cpp(root_dir, compiler_path):
    with open('compile_files_cpp.bat', 'w') as bat_file:
        for foldername, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.cpp'):
                    abs_path = os.path.abspath(os.path.join(foldername, filename))
                    bat_file.write(f'"{compiler_path}" {abs_path}\n')


def create_compile_bat_cs(root_dir, compiler_path):
    with open('compile_files_cs.bat', 'w') as bat_file:
        for foldername, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.cs'):
                    abs_path = os.path.abspath(os.path.join(foldername, filename))
                    bat_file.write(f'"{compiler_path}" {abs_path}\n')

folder_path = 'UserFiles\\' + number_of_test_cases

extensions_to_check = ('.cpp', '.cs', '.java', '.py')
read_text_files(folder_path, extensions_to_check)
    #
compile_cs_files_in_directory(directory_to_compile, cs_compiler_path)
create_compile_bat_cpp(directory_to_compile, сpp_compiler_path)
create_compile_bat_pas(directory_to_compile, pas_compiler_path)
create_compile_bat_cs(directory_to_compile, cs_compiler_path)
input("Created .bat files, please open it  ")
