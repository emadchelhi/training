import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_file, csv_file):
    """
    Convert XML file in CSV file

    Args:
        xml_file (str): XML file path
        csv_file (str): CSV file path   
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # get complete list of columns
    first_element = root[0]
    columns = [child.tag for child in first_element]
    rows = []

    for element in root:
        row = []
        for column in columns:
            child = element.find(column)
            value = child.text if child is not None else ''
            row.append(value)
        rows.append(row)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)
    
    print("Conversion was successfully completed.")


xml_to_csv('census_elements.xml', 'data.csv')