import csv

def read_csv_and_calculate_average(filename, column_index):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip the header row if it exists
            headers = next(reader, None)
            if headers is not None:
                print(f"Headers: {headers}")
            
            total = 0
            count = 0
            
            for row in reader:
                try:
                    value = float(row[column_index])
                    total += value
                    count += 1
                except (ValueError, IndexError):
                    print(f"Skipping invalid or missing data in row {count + 1}: {row}")
            
            if count == 0:
                print("No valid data found in the specified column.")
                return None
            
            average = total / count
            return average
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file '{filename}'.")
        return None


def main():
    filename = input("Enter the CSV filename: ")
    column_index = input("Enter the index of the column to calculate the average (0-based index): ")

    try:
        column_index = int(column_index)
    except ValueError:
        print("Error: Column index must be an integer.")
        return

    average = read_csv_and_calculate_average(filename, column_index)

    if average is not None:
        print(f"The average of the values in column {column_index} is: {average:.2f}")


if __name__ == "__main__":
    main()