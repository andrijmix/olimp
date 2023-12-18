import subprocess

# Path to the executable file (.exe)


def run_exe_with_arguments(exe_path, arguments):
    try:
        # Execute the .exe file
        process = subprocess.Popen(exe_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

        # Concatenate arguments into a single string separated by spaces
        args_str = ' '.join(str(arg) for arg in arguments)

        # Pass arguments through standard input
        process.stdin.write(args_str + '\n')
        process.stdin.flush()  # Clear the buffer

        # Get the result from the output
        output, _ = process.communicate()

        # Print the result
        # print("Execution Result:")
        # print(output)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)
    return output


def run_exe_with_arguments_from_file(exe_path, args_file):
    output_exe = ""

    try:
        with open(args_file, 'r') as file:
            arguments = [int(arg) for line in file.readlines() for arg in
                         line.strip().split()]  # Convert strings to integers

        if arguments:
            output_exe = run_exe_with_arguments(exe_path, arguments)
        else:
            output_exe = "Arguments file is empty."

    except FileNotFoundError as e:
        output_exe = f"Error: {e}"
    except ValueError as e:
        output_exe = f"Error converting string to integer: {e}"
    except Exception as e:
        output_exe = f"Error: {e}"

    return output_exe



# exe_path = 'variant1_A(1).exe'
#
# args_file_path = 'UserFiles\\A\\data1.txt'  # Path to the file with arguments
# print("Result: ", run_exe_with_arguments_from_file(exe_path, args_file_path))
