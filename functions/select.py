import csv

def get_columns(input_file, output_file, columns_to_keep):
    """
    Get the columns from the input file
    Args:
        input_file: the file to read from
        output_file: the file to write to
        columns_to_keep: the columns to write in the output file
    """
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        result = [{col: row[col] for col in columns_to_keep} for row in reader]

    with open(output_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=columns_to_keep)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
    
    print(f"The columns {columns_to_keep} have been written to {output_file}")