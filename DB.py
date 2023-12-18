import csv
import os

server = 'OlympProgDb.mssql.somee.com'
database = 'OlympProgDb'
username = 'mBoichura_SQLLogin_1'
password = 'RivneNUWEE2023'


def write_to_csv(report_data, file_name='report.csv'):
    headers = ['File Name', 'Input Parameters', 'Expected Result', 'Actual Result', 'Status', 'AI Rate']

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for data in report_data:
            writer.writerow([data['file_name'], data['input_params'], data['expected_result'],
                             data['actual_result'], data['status'], data['rate_ai']])


import pyodbc


def connect_to_mssql(server, database, username, password):
    """
    Establishes a connection to an MS SQL Server database.

    :param server: The name or IP address of the SQL server
    :param database: The name of the database
    :param username: The username for the database connection
    :param password: The password for the database connection
    :return: A connection object to the database
    """
    try:
        # Connection string formation
        # It uses the SQL Server ODBC driver, server name, database name, user ID, and password
        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        # Creating the connection using the connection string
        # pyodbc.connect() establishes the connection using the provided details
        connection = pyodbc.connect(connection_string)

        # Confirmation message on successful connection
        print("Successfully connected to SQL Server")
        return connection  # Returning the connection object to be used elsewhere

    except Exception as e:
        # Error handling in case connection fails
        print(f"Error connecting to SQL Server: {e}")
        return None  # Returning None if connection is not established


def test_insert_and_query(connection):
    """
    Executes a test insert and select query on the given database connection.

    :param connection: Active database connection
    """
    try:
        # Assuming a table named 'TestTable' with columns 'ID' (int) and 'Name' (varchar)
        cursor = connection.cursor()

        # Inserting test data
        cursor.execute("INSERT INTO TestTable (ID, Name) VALUES (?, ?)", (1, 'Test Name'))
        connection.commit()
        print("Test data inserted successfully.")

        # Retrieving test data
        cursor.execute("SELECT * FROM TestTable WHERE ID = ?", (1,))
        row = cursor.fetchone()
        while row:
            print(f"Retrieved data: ID = {row.ID}, Name = {row.Name}")
            row = cursor.fetchone()

    except Exception as e:
        print(f"Error during SQL operations: {e}")


import pyodbc


def save_to_database(report_item):
    try:
        connection = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = connection.cursor()

        # Convert 'ChatCompletionMessage' object to string if necessary
        ai_rating = str(report_item['rate_ai']) if report_item['rate_ai'] else None

        sql_insert_query = """INSERT INTO ReportTable (FileName, InputParams, ExpectedResult, ActualResult, Status, AI_Rating) 
                              VALUES (?, ?, ?, ?, ?, ?)"""
        values = (report_item['file_name'], report_item['input_params'], report_item['expected_result'],
                  report_item['actual_result'], report_item['status'], ai_rating)

        cursor.execute(sql_insert_query, values)
        connection.commit()
        print("Report item saved to database successfully.")

    except Exception as e:
        print(f"Error saving to database: {e}")

    finally:
        if connection:
            connection.close()


import os

import os

import os

def update_successful_tests_amount(connection):
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT FileName FROM ReportTable")
        distinct_files = cursor.fetchall()

        for file_tuple in distinct_files:
            file_name_full = file_tuple[0]  # Получаем полное имя файла из кортежа
            file_name_without_extension = os.path.splitext(os.path.basename(file_name_full))[0]  # Извлекаем имя без расширения

            cursor.execute("SELECT COUNT(*) FROM ReportTable WHERE FileName = ? AND Status = 'Passed'", (file_name_full,))
            passed_tests_count = cursor.fetchone()[0]

            try:
                # Обновляем SuccessfulTestsAmount в Evaluations для файла без расширения
                cursor.execute("UPDATE Evaluations SET SuccessfulTestsAmount = ? WHERE Path = ?",
                               (passed_tests_count, file_name_without_extension))
                connection.commit()
                print(f"SuccessfulTestsAmount updated for {file_name_without_extension} successfully.")
            except Exception as e:
                print(f"Error updating SuccessfulTestsAmount for {file_name_without_extension}: {e}")
                connection.rollback()

        print("All SuccessfulTestsAmount updated.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()



# # Example usage of the function
conn = connect_to_mssql('OlympProgDb.mssql.somee.com', 'OlympProgDb', 'mBoichura_SQLLogin_1', 'RivneNUWEE2023')
# # Make sure to replace the arguments with actual server details and credentials
# if conn:
#     test_insert_and_query(conn)

