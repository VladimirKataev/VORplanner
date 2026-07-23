import csv

"""
    we need the following:
        paths = [{fromGlobalId, toGlobalId, altitude, name, direction}]
            - NOTE: a->b is different from b->a. Odd people fly East.
        neighbors[globalID] = pathsTouching[]
        getPointID[VRP] = globalID
"""

def loadData(filename : str) -> tuple[dict, dict, dict]:
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file);
        for row in reader:
            print(row)