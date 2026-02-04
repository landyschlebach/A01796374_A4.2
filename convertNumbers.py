"""
Ejercicio de Programación 2: Converter.
Programa CL para convertir un número a base binaria y hexadecimal.
"""

import sys # librería necesaria para leer argumentos desde línea de comandos
import time # librería necesaria para medir el tiempo de ejecución

DATE_FORMAT = "%b %d, %Y %H:%M:%S"

def read_file(file_name):
    """Leer el contenido (números) de un archivo, conteo y validación de registros.
    Gestionar datos inválidos."""
    data = []
    total_records = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line_idx, line in enumerate(file, start=1):
                total_records += 1
                row = line.strip()
                if not row:
                    continue
                try:
                    value = int(float(row))
                    data.append(value)
                except ValueError as value_error:
                    print(f'ERROR [Fila {line_idx}]: {value_error}')
    except FileNotFoundError:
        print(f'ERROR: El archivo {file_name} no existe.')
        sys.exit(1)
    return data, total_records


def to_binary_base(decimal_number):
    """Convertir un número decimal a su base binaria."""
    if decimal_number == 0:
        return "0"
    num = decimal_number & 0xFFFFFFFF
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    if decimal_number < 0:
        return binary[-10:]
    return binary


def to_hexadecimal_base(decimal_number):
    """Convertir un número a base hexadecimal."""
    if decimal_number == 0:
        return "0"
    num = decimal_number & 0xFFFFFFFF
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        hexadecimal = hex_chars[num % 16] + hexadecimal
        num //= 16
    return hexadecimal


def save_results(total_records, data, conversions, times_data):
    """
    Generar una tabla con los resultados de las conversiones.
    Guardar la tabla y datos de procesamiento en un archivo.
    """
    results_file_name = "ConvertionResults.txt"

    start_str, end_str, exec_time_str = calculate_format_time(times_data)

    table_content = format_table(data, conversions)

    results = (
        f'====Inicio del procesamiento====\n'
        f'Inicio de ejercución: {start_str}\n'
        f'Registros totales: {total_records}\n'
        f'====Resultados de conversión====\n'
        f'{table_content}'
        f'====Fin del procesamiento====\n'
        f'Registros convertidos: {len(data)}\n'
        f'Registros con errores/no procesados: {total_records - len(data)}\n'
        f'Duración del procesamiento: {exec_time_str}\n'
        f'Fin de ejecución: {end_str}\n'
    )

    print(results)

    try:
        with open(results_file_name, 'w', encoding='utf-8') as f_out:
            f_out.write(results)
    except IOError as file_error:
        print(f'ERROR al guardar resultados en {results_file_name}: {file_error}')


def calculate_format_time(times_data):
    """Calcular el tiempo de ejecución.
    Convertir tiempo en un formato legible HH:MM:SS.mmmm."""
    start_time, end_time = times_data
    start_str = time.strftime(DATE_FORMAT, time.localtime(start_time))
    end_str = time.strftime(DATE_FORMAT, time.localtime(end_time))

    time_passed = end_time - start_time

    hours = int(time_passed // 3600)
    minutes = int((time_passed % 3600) // 60)
    seconds = time_passed % 60

    duration_str = f'{hours:02}:{minutes:02}:{seconds:07.4f}'
    return start_str, end_str, duration_str


def format_table(data, conversions):
    """Generar tabla de resultados de conversiones."""
    header = f"{'ITEM':<5} | {'DECIMAL':<10} | {'BINARIO':<15} | {'HEX':<10}\n"
    separator = "-" * 60 + "\n"
    rows = ""
    for index, value in enumerate(data):
        bin_val, hex_val = conversions[index]
        rows += f"{index+1:<5} | {value:<10} | {bin_val:<15} | {hex_val:<10}\n"
    return f"{separator}{header}{separator}{rows}{separator}"


def main():
    """Función principal para ejecutar la conversión de base decimal 
    a binario y hexadecimal."""
    if len(sys.argv) < 2:
        print('ERROR: Debe proporcionar el nombre del archivo como parámetro.')
        return
    start_time = time.time()
    file_name = sys.argv[1]
    data, total_records = read_file(file_name)
    conversions = []

    for number in data:
        conversions.append((to_binary_base(number), to_hexadecimal_base(number)))

    end_time = time.time()
    times_data = (start_time, end_time)
    save_results(total_records, data, conversions, times_data)


if __name__ == "__main__":
    main()
