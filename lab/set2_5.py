import pandas as pd

def read_excel_and_print_table(filename, sheet_name=0):
    try:
        # Read the Excel file
        df = pd.read_excel(filename, sheet_name=sheet_name)
        
        # Print the DataFrame in a tabular format
        print(df.to_string(index=False))
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def main():
    filename = input("Enter the Excel filename (with .xlsx extension): ")
    sheet_name_input = input("Enter the sheet name or index (leave blank for the first sheet): ")

    # Convert sheet_name_input to integer if it's a number, otherwise keep it as a string
    try:
        sheet_name = int(sheet_name_input)
    except ValueError:
        sheet_name = sheet_name_input if sheet_name_input else 0

    read_excel_and_print_table(filename, sheet_name)


if __name__ == "__main__":
    main()