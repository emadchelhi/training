from typing import Dict

def InnerJoin(table1: Dict, table2: Dict, key1, key2) -> Dict:
    """This function takes as input 2 datasets, implemented as dictionaries 
    of dictionaries and merge them based on a common column."""
    with open(table1, 'r')
