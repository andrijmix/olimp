import glob
import os
import xml.etree.ElementTree as ET

from AIprompt import rate_code
from C import run_exe_with_arguments_from_file
from DB import write_to_csv, save_to_database, conn, \
    update_successful_tests_amount  # Assuming 'save_to_database' is a function to save data to DB
from compiler import compile_cs_files_in_directory, create_compile_bat_cpp, create_compile_bat_pas, \
    create_compile_bat_cs
from fileFTP import download_folder_ftp
from settings import ftp_host, ftp_username, ftp_password, ftp_folder_path, local_folder_path, directory_to_compile, \
     сpp_compiler_path, pas_compiler_path, number_of_test_cases
from showFile import read_text_files


def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.

    :param file_path: Path to the file to be read
    :return: Content of the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def input_generator(data):
    """
    Yields each line from the provided data as a separate input.

    :param data: Multi-line string data
    """
    for item in data.splitlines():
        yield item


import io
import contextlib


def execute_code(code, input_data):
    """
    Executes a given Python code with provided input data and captures its output.

    :param code: Python code to execute
    :param input_data: Input data for the code
    :return: Output from the code execution or error message
    """
    inputs = input_data.split(' ')
    gen = iter(inputs)

    def mock_input():
        try:
            return next(gen)
        except StopIteration:
            return ""  # Return empty string instead of None

    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        exec_globals = {'__builtins__': __builtins__, 'input': mock_input}
        try:
            exec(code, exec_globals)
        except Exception as e:
            return "Error: " + str(e)  # Return the error message if an exception occurs

        output = buf.getvalue()

    return output.strip()


def execute_code2(code, input_data):
    """
    Executes a given Python code with provided input data and captures its output.

    :param code: Python code to execute
    :param input_data: Input data for the code
    :return: Output from the code execution
    """
    inputs = input_data.split(' ')

    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        exec_globals = {'__builtins__': __builtins__}

        # Mock input function that simulates user input
        def mock_input(prompt):
            return inputs.pop(0)

        # Override the input function
        builtins = __builtins__
        builtins.input = mock_input

        # Execute the code
        try:
            exec(code, exec_globals)
        except Exception as e:
            return str(e)  # Return any exceptions as string

        output = buf.getvalue()  # Get output

    return output.strip()


def main():
    report_data = []
    base_path = 'UserFiles\\' + number_of_test_cases
    root = ET.Element("Report")

    for task_folder in os.listdir(base_path):
        task_path = os.path.join(base_path, task_folder)

        if os.path.isdir(task_path):
            solution_files = glob.glob(os.path.join(task_path, 'Solutions', '*.exe')) + glob.glob(
                os.path.join(task_path, 'Solutions', '*.py'))

            for solution_file in solution_files:

                data_files = glob.glob(os.path.join(task_path, 'data*.txt'))
                result_files = glob.glob(os.path.join(task_path, 'result*.txt'))
                code_rating = ''
                if solution_file.endswith('.py'):
                    code_rating = rate_code(read_file(solution_file))
                for data_file, result_file in zip(sorted(data_files), sorted(result_files)):
                    print(f"Processing file pair: {data_file}, {result_file}")
                    print('solution_file', solution_file)
                    if solution_file.endswith('.py'):
                        program_code = read_file(solution_file)
                    else:
                        program_code = solution_file
                        # continue
                    input_data = read_file(data_file)
                    expected_result = read_file(result_file)

                    try:
                        actual_result = ""
                        print(solution_file)
                        if solution_file.endswith('.py'):
                            actual_result = execute_code(program_code, input_data)
                            if "Error" in actual_result:
                                actual_result = execute_code2(program_code, input_data)

                        else:
                            actual_result = run_exe_with_arguments_from_file(program_code, data_file)
                        # print("actual_result: ", actual_result)
                        testcase = ET.SubElement(root, "TestCase")
                        ET.SubElement(testcase, "TaskFolder").text = task_folder
                        ET.SubElement(testcase, "SolutionFile").text = solution_file
                        ET.SubElement(testcase, "DataFile").text = data_file
                        ET.SubElement(testcase, "ResultFile").text = result_file
                        if solution_file.endswith('.exe'):
                            status = "Passed" if int(actual_result) == int(expected_result) else "Failed"
                        else:
                            status = compare_results(actual_result,expected_result)
                        print("actual_result: ", actual_result)
                        print("expected_result: ", expected_result)
                        print(status)

                    except Exception as e:
                        print(f"Error executing {solution_file}: {e}")
                        testcase = ET.SubElement(root, "TestCase")
                        ET.SubElement(testcase, "TaskFolder").text = task_folder
                        ET.SubElement(testcase, "SolutionFile").text = solution_file
                        ET.SubElement(testcase, "Status").text = "Error"
                        ET.SubElement(testcase, "ErrorMessage").text = str(e)
                        status = "Error"

                    report_item = {
                        'file_name': solution_file,
                        'input_params': input_data,
                        'expected_result': expected_result,
                        'actual_result': actual_result,
                        'status': status,
                        'rate_ai': code_rating
                    }
                    report_data.append(report_item)

                    # Save report item to database
                    save_to_database(report_item)

    # Write data to CSV and XML
    write_to_csv(report_data, file_name='report.csv')
    # tree = ET.ElementTree(root)
    # tree.write('report.xml', encoding='utf-8', xml_declaration=True)


import re


def compare_results(actual_result, expected_result):
    # Розділяємо рядок на елементи (числа або тексти)
    actual_elements = actual_result.split()
    expected_elements = expected_result.split()

    # Перевіряємо, чи всі елементи з expected_elements є в actual_elements
    if all(elem in actual_elements for elem in expected_elements):
        return "Passed"
    else:
        return "Failed"


if __name__ == "__main__":

    # download_folder_ftp(ftp_host, ftp_username, ftp_password, ftp_folder_path, local_folder_path)

    main()

# if conn:
#     update_successful_tests_amount(conn)
