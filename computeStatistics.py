"""
Ejercicio de Programación 1: Compute Statistics.
Programa CL para calcular estadísticas descriptivas a partir de un archivo
como parámetro.
Incluye media, mediana, moda, desviación estándar y varianza.
"""

import sys # librería necesaria para leer argumentos desde línea de comandos
import time # librería necesaria para medir el tiempo de ejecución

DATE_FORMAT = "%b %d, %Y %H:%M:%S"

def read_file(file_name):
    """Leer el contenido (números) de un archivo y gestionar datos inválidos."""
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
                    value = float(row)
                    data.append(value)
                except ValueError as value_error:
                    print(f'ERROR [Fila {line_idx}]: {value_error}')
    except FileNotFoundError:
        print(f'ERROR: El archivo {file_name} no existe.')
        sys.exit(1)
    return data, total_records


def calculate_mean(data):
    """Calcular la media aritmética."""
    if not data:
        return 0
    total = 0.0
    for number in data:
        total += number
    return total / len(data)


def calculate_median(data):
    """Calcular la mediana."""
    if not data:
        return 0
    total_count = len(data)
    sorted_data = sorted(data)
    mid = total_count // 2
    if total_count % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def calculate_mode(data):
    """Calcular la moda."""
    if not data:
        return [0]
    counts = {}
    for record in data:
        counts[record] = counts.get(record, 0) + 1
    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = count
    if max_count == 1:
        return "#N/A"
    modes = [val for val, count in counts.items() if count == max_count]
    return modes


def calculate_variance(data, mean):
    """Calcular la varianza."""
    if len(data) < 2:
        return 0
    sum_sq_diff = sum((x - mean) ** 2 for x in data)
    return sum_sq_diff / (len(data) - 1)


def calculate_std_dev(variance):
    """Calcular la desviación estándar"""
    std_dev = variance ** 0.5

    return std_dev


def save_results(total_records, data_len, stats_results, times_data):
    """
    Formatea, imprime en pantalla y guarda los resultados en un archivo.
    """
    results_file_name = "StatisticsResults.txt"

    start_str, end_str, exec_time_str = calculate_format_time(times_data)

    results = (
        f'====Inicio del procesamiento====\n'
        f'Inicio de ejecución: {start_str}\n'
        f'Registros totales: {total_records}\n'
        f'====Estadísticas Descriptivas====\n'
        f'Media: {stats_results[0]:.4f}\n'
        f'Mediana: {stats_results[1]:.4f}\n'
        f'Moda: {stats_results[2]}\n'
        f'Varianza: {stats_results[3]:.4f}\n'
        f'Desviación Estándar: {stats_results[4]:.4f}\n'
        f'====Fin del procesamiento====\n'
        f'Registros procesados: {data_len}\n'
        f'Registros con errores/no procesados: {total_records - data_len}\n'
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
    """Función principal para ejecutar el cálculo de estadísticas descriptivas."""
    if len(sys.argv) < 2:
        print('ERROR: Debe proporcionar el nombre del archivo como parámetro.')
        return

    start_time = time.time()
    file_name = sys.argv[1]
    data, total_records = read_file(file_name)

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(variance)
    end_time = time.time()
    stats_results = (mean, median, mode, variance, std_dev)
    times_data = (start_time, end_time)
    save_results(total_records, len(data), stats_results, times_data)


if __name__ == "__main__":
    main()
