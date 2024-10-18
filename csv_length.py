import csv

def count_rows_in_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        row_count = sum(1 for row in csv_reader)  # Count the number of rows
    print(f"Total number of rows: {row_count}")

# Example usage
csv_file_path = 'dataset/test.csv'  # Replace with your file path
count_rows_in_csv(csv_file_path)
