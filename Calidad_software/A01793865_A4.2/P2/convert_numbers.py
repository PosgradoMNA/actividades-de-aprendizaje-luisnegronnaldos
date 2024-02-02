
''' Modulo que convierte los datoa a binarios y a hex'''
import sys
import time

def convert_to_binary_hex(data):
    ''' convierte a binarios y a hex'''
    binary_results = []
    hex_results = []

    for item in data:
        try:
            num = int(item)
            binary_results.append(bin(num)[2:])
            hex_results.append(hex(num)[2:])
        except ValueError:
            print(f"Invalid data: {item}")

    return binary_results, hex_results

def main():
    ''' funcion principal'''
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

    start_time = time.time()

    binary_results, hex_results = convert_to_binary_hex(data)

    elapsed_time = time.time() - start_time

    with open("ConversionResults.txt", 'w') as results_file:
        for binary, hex_value in zip(binary_results, hex_results):
            print(f"Binary: {binary} | Hexadecimal: {hex_value}")
            results_file.write(f"Binary: {binary} | Hexadecimal: {hex_value}\n")

    print(f"Execution time: {elapsed_time} seconds")
    results_file.write(f"\nExecution time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
    