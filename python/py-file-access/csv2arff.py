# converting a csv file to a ARFF file
# usage: python3 'census_selected_header.csv' 'output.arff'

import csv

def csv_to_arff(input_file, output_file):
    """
    Convert a csv file to a ARFF file.
    
    Args:
        input_file (str): The input csv file.
        output_file (str): The output ARFF file.
    """ 

    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        arff_content = f"@Relation {input_file.split('.')[0]}\n\n"
    
        for h in header:
            arff_content += f"@ATTRIBUTE {h} String\n" 

        arff_content += "\n@DATA\n"

        for row in reader:
            arff_content += ','.join(row) + '\n'

    with open(output_file, 'w') as arff_file:
        arff_file.write(arff_content)

    print("The file has been converted successfully.")