import subprocess

# Створення та компіляція проекту .NET
subprocess.run(['dotnet', 'new', 'console', '-o', 'MyProject', '--force'])
subprocess.run(['copy', 'C:/Users/Andrii/PycharmProjects/olimpiada/Etalon.cs', 'MyProject/Program.cs'], shell=True)
subprocess.run(['dotnet', 'build', 'MyProject'])

# Шлях до скомпільованого DLL файлу
compiled_dll = 'MyProject/bin/Debug/net6.0/MyProject.dll'

# Вхідні дані, які будуть передані у програму
input_data = '2 5\n'

# Виконання скомпільованої програми з передачею вхідних даних
result = subprocess.run(['dotnet', compiled_dll], input=input_data, capture_output=True, text=True)

# Виведення результату
print(result.stdout)
