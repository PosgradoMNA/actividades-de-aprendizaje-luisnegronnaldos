''' Modulo para obtener estadisticos'''
import sys
import time
import math

def convert_to_float(data):
    ''' convierte los datos a puntos flotantes'''
    converted_data = []

    for idx, item in enumerate(data):
        try:
            converted_data.append(float(item))
        except ValueError:
            print(f"Invalid data at index {idx}: {item}")

    return converted_data

def compute_statistics(data):
    ''' calculos estadisticos solicitados'''
    n_1 = len(data)
    mean = sum(data) / n_1

    # Median
    sorted_data = sorted(data)
    if n_1 % 2 == 0:
        median = (sorted_data[n_1 // 2 - 1] + sorted_data[n_1 // 2]) / 2
    else:
        median = sorted_data[n_1 // 2]

    # Mode
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    b_1 ={}
    b_1 = max(frequency.values())
    if b_1 == 1:
        mode = "N/A"
    else:
        mode = [k for k, v in frequency.items() if v == max(frequency.values())]
    #mode = [k for k, v in frequency.items() if v == max(frequency.values())]

    # Variance
    variance = sum((item - mean) ** 2 for item in data) / n_1

    # Standard Deviation
    std_deviation = math.sqrt(variance)

    return n_1, mean, median, mode, std_deviation, variance

def main():
    ''' definición principal'''
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py fileWithData.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r') as file:
            data = file.read().split()
            data = convert_to_float(data)
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

    start_time = time.time()

    n_1, mean, median, mode, std_deviation, variance = compute_statistics(data)

    elapsed_time = time.time() - start_time

    with open("StatisticsResults.txt", 'w') as results_file:
        print(
            f"Count: {n_1}\nMean: {mean}\nMedian: {median}\nMode: {mode}\nStandard Deviation: {std_deviation}\nVariance: {variance}")
        results_file.write(
            f"Count: {n_1}\nMean: {mean}\nMedian:{median}\nMode: {mode}\nStandard Deviation: {std_deviation}\nVariance: {variance}\n")
        print(f"Execution time: {elapsed_time} seconds")
        results_file.write(f"\nExecution time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
    