"""
Ejercicio de Programación 3: Count Words.
Programa CL para contar la freecuencia de las palabras en un archivo.
"""
# pylint: disable=invalid-name

import sys # librería necesaria para leer argumentos desde línea de comandos
import time # librería necesaria para medir el tiempo de ejecución

DATE_FORMAT = "%b %d, %Y %H:%M:%S"

def read_file(file_name):
    """Leer el contenido (palabras) de un archivo, conteo y validación de registros.
    Gestionar datos inválidos."""
    data = []
    total_records = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    clean_word = word.strip('.,"?!():;¿¡=[]{}<>#$%&/\\\'`´^~*-_')
                    if clean_word.isalpha():
                        total_records += 1
                        data.append(clean_word.lower())
                    else:
                        print(f'ERROR: [{word}] no es una palabra.')
    except FileNotFoundError:
        print(f'ERROR: El archivo {file_name} no existe.')
        sys.exit(1)
    return data, total_records


def count_word_frequency(data):
    """Contar la frecuencia de cada palabra en una lista de palabras."""
    frequency = {}
    for word in data:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def save_results(total_records, data, times_data):
    """
    Guardar los datos procesados en un archivo:
    palabra y su frecuencia
    """
    results_file_name = "WordCountResults.txt"

    start_str, end_str, exec_time_str = calculate_format_time(times_data)

    table_rows = ""
    for word, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
        table_rows += f"{word:<15} | {count:<10}\n"


    results = (
        f'====Inicio del procesamiento====\n'
        f'Inicio de ejercución: {start_str}\n'
        f'Registros totales: {total_records}\n'
        f'====Resultados de conversión====\n'
        f'Palabra         | Frecuencia \n'
        f'{table_rows}'
        f'====Fin del procesamiento====\n'
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


def main():
    """Función principal para ejecutar el conteo por cada palabra en el archivo."""
    if len(sys.argv) < 2:
        print('ERROR: Debe proporcionar el nombre del archivo como parámetro.')
        return
    start_time = time.time()
    file_name = sys.argv[1]
    data, total_records = read_file(file_name)
    frequencies = count_word_frequency(data)

    end_time = time.time()
    times_data = (start_time, end_time)
    save_results(total_records, frequencies, times_data)


if __name__ == "__main__":
    main()
