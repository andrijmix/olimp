def compare_results(actual_result, expected_result):
    # Розділяємо рядок на елементи (числа або тексти)
    actual_elements = actual_result.split()
    expected_elements = expected_result.split()

    # Перевіряємо, чи всі елементи з expected_elements є в actual_elements
    if all(elem in actual_elements for elem in expected_elements):
        return "Passed"
    else:
        return "Failed"

# Приклад використання функції
result_status = compare_results("****", "****")
print(result_status)