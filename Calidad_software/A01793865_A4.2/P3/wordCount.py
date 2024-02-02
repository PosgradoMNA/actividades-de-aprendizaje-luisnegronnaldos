import sys
import time

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def count_words(words):
    word_count = {}
    for word in words:
        # Consider only alphanumeric characters and convert to lowercase
        cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
        if cleaned_word:
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
    return word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]

    start_time = time.time()

    words = process_file(input_file_path)
    word_count = count_words(words)

    elapsed_time = time.time() - start_time

    with open("WordCountResults.txt", 'w') as results_file:
        print("Word\tFrequency")
        results_file.write("Word\tFrequency\n")
        for word, frequency in word_count.items():
            print(f"{word}\t{frequency}")
            results_file.write(f"{word}\t{frequency}\n")
        print(f"Execution time: {elapsed_time} seconds")
        results_file.write(f"\nExecution time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
