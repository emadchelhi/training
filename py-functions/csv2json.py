import csv

def csv_to_json(csv_file, json_file):
    """
    Convert CSV file in JSON file.
    Args:
        csv_file (str): CSV file path
        json_file (str): JSON file path
    """
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    with open(json_file, 'w') as file:
        file.write('[')
        for i, row in enumerate(rows):
            file.write('{')
            for j, (key, value) in enumerate(row.items()):
                file.write(f'"{key}": "{value}"')
                if j < len(row) - 1:
                    file.write(', ')
            file.write('}')
            if i < len(rows) - 1:
                file.write(', ')
        file.write(']')
    
    print("Conversion was successfully completed.") 