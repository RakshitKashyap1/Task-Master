def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")
        return None

    # Split the text into words using whitespace as the delimiter
    words = text.split()

    # Count the number of words
    word_count = len(words)

    return word_count


def main():
    filename = input("Enter the filename: ")
    word_count = count_words_in_file(filename)

    if word_count is not None:
        print(f"The file '{filename}' contains {word_count} words.")


if __name__ == "__main__":
    main()